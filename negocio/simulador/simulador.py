"""Simulador de Fase 2 — "gemelo digital" de las tres finalistas (v1, Día 5).

Implementa las ecuaciones de ../modelo/modelo.md: tráfico en tres canales
(SEO con retraso, redes del dueño con abandono, Etsy), embudo en dos etapas
para A y C, conversión directa para B, estacionalidad, comisiones e IVA.

Produce para cada idea: escenarios pesimista/base/optimista, Monte Carlo con
P(neto >= 500 €), sensibilidad (tornado + correlación de rangos) y la
comparación lanzamiento junio vs febrero de 2027.

Solo librería estándar (las sesiones no siempre tienen numpy). Gráficas en SVG.

Uso: python3 simulador.py [n_corridas] [semilla]
"""
import json
import math
import random
import statistics
import sys
from pathlib import Path

UMBRAL = 500.0
H = 12                     # meses simulados desde el lanzamiento
IVA = 0.21
COSTE_FIJO = 15.0          # dominio ≈ 12 €/año + margen [S]
REEMBOLSOS = 0.03          # [E]
P_ABANDONO = 0.06          # prob. mensual de que el dueño deje de publicar [E]
SIGMA_RED = 0.6            # ruido mensual del canal de redes [E]
Z90, Z95 = 1.2816, 1.6449

# Estacionalidad por mes del calendario (ene..dic), media 1 [E]
ESTACIONALIDAD = {
    "A": [1.3, 1.1, 1.0, 1.0, 0.9, 0.9, 0.8, 0.6, 1.4, 1.2, 1.0, 0.8],
    "B": [1.2, 1.0, 1.0, 1.0, 1.0, 0.9, 0.8, 0.7, 1.2, 1.1, 1.1, 1.0],
    "C": [1.2, 1.0, 1.0, 0.9, 1.0, 0.9, 0.4, 0.4, 1.8, 1.3, 1.1, 1.0],
}

# Parámetros inciertos: ("log", p5, p95) lognormal · ("uni", a, b) uniforme.
# El tercer elemento de cada tupla indica qué extremo es el desfavorable.
IDEAS = {
    "A": {
        "nombre": "Opositores (planificador + generador gratis)",
        "precio": 15, "embudo": "dos_etapas",
        "params": {
            "seo_max": ("log", 60, 3000),      # visitas/mes de Google en madurez [E]
            "red_base": ("log", 5, 400),       # visitas/mes desde redes del dueño [E]
            "p_uso": ("log", 0.05, 0.25),      # visita -> usa generador (ref. 13 % [S])
            "p_compra": ("log", 0.008, 0.08),  # usuario -> compra (ref. 2,6 % [S])
            "etsy_max": ("log", 15, 500),      # nicho pequeño en Etsy en español [E]
            "p_etsy": ("log", 0.005, 0.03),
            "retraso_seo": ("uni", 3, 6),      # meses sin Google [S]
            "tau_seo": ("uni", 3, 9),          # meses de crecimiento SEO [E]
            "tau_etsy": ("uni", 1, 4),
        },
    },
    "B": {
        "nombre": "Inmobiliarias (plantillas Canva)",
        "precio": 17, "embudo": "directa",
        "params": {
            "seo_max": ("log", 20, 800),
            "red_base": ("log", 2, 150),
            "etsy_max": ("log", 20, 800),      # visitas/mes a los anuncios de Etsy; comprador poco presente en Etsy-es [E]
            "p_directa": ("log", 0.003, 0.03), # visita web -> compra [S: 1–3 % típico]
            "p_etsy": ("log", 0.005, 0.04),    # visita Etsy -> compra (1–3 % [S])
            "retraso_seo": ("uni", 3, 6),
            "tau_seo": ("uni", 3, 9),
            "tau_etsy": ("uni", 1, 4),
        },
    },
    "C": {
        "nombre": "Estudiantes ESO/Bach (planner + generador)",
        "precio": 7, "embudo": "dos_etapas",
        "params": {
            "seo_max": ("log", 100, 6000),
            "red_base": ("log", 20, 1500),     # el dueño es del público objetivo
            "etsy_max": ("log", 20, 600),
            "p_uso": ("log", 0.08, 0.35),
            "p_compra": ("log", 0.003, 0.03),  # demanda muy orientada a "gratis" [M]
            "p_etsy": ("log", 0.005, 0.03),
            "retraso_seo": ("uni", 3, 6),
            "tau_seo": ("uni", 3, 9),
            "tau_etsy": ("uni", 1, 4),
        },
    },
}
# Parámetros en los que un valor ALTO es desfavorable
DESFAVORABLE_ALTO = {"retraso_seo", "tau_seo", "tau_etsy"}


def neto_web(precio):
    return precio / (1 + IVA) * (1 - 0.05 - 0.029) - 0.30          # Payhip


def neto_etsy(precio):
    return precio / (1 + IVA) * (1 - 0.065 - 0.04 - 0.15 * 0.2) - 0.30 - 0.19


def cuantil(dist, q):
    """Valor del parámetro en el cuantil q (0..1)."""
    tipo, a, b = dist
    if tipo == "uni":
        return a + (b - a) * q
    mu = (math.log(a) + math.log(b)) / 2
    sigma = (math.log(b) - math.log(a)) / (2 * Z95)
    return math.exp(mu + sigma * statistics.NormalDist().inv_cdf(q))


def muestrear(rng, dist):
    return cuantil(dist, min(max(rng.random(), 1e-9), 1 - 1e-9))


def poisson(rng, lam):
    if lam <= 0:
        return 0
    if lam > 50:
        return max(0, round(rng.gauss(lam, math.sqrt(lam))))
    lim, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= lim:
            return k
        k += 1


def simular(idea, v, mes_lanz, rng=None):
    """Una trayectoria de 12 meses. Con rng=None devuelve el valor esperado."""
    cfg = IDEAS[idea]
    est = ESTACIONALIDAD[idea]
    nw, ne = neto_web(cfg["precio"]), neto_etsy(cfg["precio"])
    activo = True
    total, ventas_tot, visitas_tot = 0.0, 0.0, 0.0
    for m in range(1, H + 1):
        s = est[(mes_lanz - 1 + m - 1) % 12]
        d = v["retraso_seo"]
        seo = 0.0 if m <= d else v["seo_max"] * (1 - math.exp(-(m - d) / v["tau_seo"]))
        if rng is None:
            red = v["red_base"] * (1 - P_ABANDONO) ** (m - 1)
        else:
            if activo and m > 1 and rng.random() < P_ABANDONO:
                activo = False
            ruido = rng.lognormvariate(-SIGMA_RED ** 2 / 2, SIGMA_RED)
            red = v["red_base"] * ruido if activo else 0.0
        etsy = v.get("etsy_max", 0) * (1 - math.exp(-m / v["tau_etsy"])) if "etsy_max" in v else 0.0
        web = s * (seo + red)
        etsy *= s
        if cfg["embudo"] == "dos_etapas":
            lam_web = web * v["p_uso"] * v["p_compra"]
        else:
            lam_web = web * v["p_directa"]
        lam_etsy = etsy * v.get("p_etsy", 0)
        if rng is None:
            vw, ve = lam_web, lam_etsy
        else:
            vw, ve = poisson(rng, lam_web), poisson(rng, lam_etsy)
        total += vw * nw + ve * ne
        ventas_tot += vw + ve
        visitas_tot += web + etsy
    neto = total * (1 - REEMBOLSOS) - COSTE_FIJO
    return neto, ventas_tot, visitas_tot


def valores_en(idea, q_fav):
    """Todos los parámetros en el cuantil 'favorable' q_fav (0.1 = pesimista)."""
    out = {}
    for k, dist in IDEAS[idea]["params"].items():
        q = 1 - q_fav if k in DESFAVORABLE_ALTO else q_fav
        out[k] = cuantil(dist, q)
    return out


def tornado(idea, mes_lanz):
    base_v = valores_en(idea, 0.5)
    base = simular(idea, base_v, mes_lanz)[0]
    filas = []
    for k in IDEAS[idea]["params"]:
        res = []
        for q_fav in (0.1, 0.9):
            v = dict(base_v)
            v[k] = valores_en(idea, q_fav)[k]
            res.append(simular(idea, v, mes_lanz)[0])
        filas.append((k, res[0], res[1], abs(res[1] - res[0])))
    filas.sort(key=lambda f: -f[3])
    return base, filas


def rangos(xs):
    orden = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0] * len(xs)
    for pos, i in enumerate(orden):
        r[i] = pos
    return r


def spearman(xs, ys):
    rx, ry = rangos(xs), rangos(ys)
    return statistics.correlation(rx, ry)


def monte_carlo(idea, n, mes_lanz, semilla):
    rng = random.Random(semilla)
    netos, muestras, ventas = [], {k: [] for k in IDEAS[idea]["params"]}, []
    for _ in range(n):
        v = {k: muestrear(rng, d) for k, d in IDEAS[idea]["params"].items()}
        neto, vt, _ = simular(idea, v, mes_lanz, rng)
        netos.append(neto)
        ventas.append(vt)
        for k in v:
            muestras[k].append(v[k])
    corr = {k: spearman(muestras[k], netos) for k in muestras}
    return netos, ventas, corr


# ---------------------------------------------------------------- gráficas SVG
def svg_histograma(netos, titulo, ruta):
    w, h, pad = 640, 300, 50
    tope = sorted(netos)[int(0.98 * len(netos))]
    tope = max(tope, UMBRAL * 1.3)
    nb = 40
    ancho = (tope + COSTE_FIJO) / nb
    cuentas = [0] * nb
    for x in netos:
        i = min(nb - 1, max(0, int((x + COSTE_FIJO) / ancho)))
        cuentas[i] += 1
    cmax = max(cuentas)
    bw = (w - 2 * pad) / nb
    partes = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" font-family="sans-serif" font-size="12">',
              '<rect width="100%" height="100%" fill="#fff"/>',
              f'<text x="{pad}" y="20" font-size="14" font-weight="bold">{titulo}</text>']
    for i, c in enumerate(cuentas):
        bh = (h - 2 * pad) * c / cmax
        x0 = -COSTE_FIJO + i * ancho
        color = "#2a9d8f" if x0 >= UMBRAL else "#9aa5b1"
        partes.append(f'<rect x="{pad + i * bw:.1f}" y="{h - pad - bh:.1f}" width="{bw - 1:.1f}" height="{bh:.1f}" fill="{color}"/>')
    xu = pad + (UMBRAL + COSTE_FIJO) / ancho * bw
    partes.append(f'<line x1="{xu:.1f}" y1="{pad - 10}" x2="{xu:.1f}" y2="{h - pad}" stroke="#d62828" stroke-dasharray="4"/>')
    partes.append(f'<text x="{xu + 4:.1f}" y="{pad}" fill="#d62828">500 €</text>')
    for t in range(0, int(tope) + 1, max(100, int(tope / 5 / 100) * 100)):
        xt = pad + (t + COSTE_FIJO) / ancho * bw
        partes.append(f'<text x="{xt:.1f}" y="{h - pad + 16}" text-anchor="middle">{t} €</text>')
    partes.append(f'<text x="{w / 2}" y="{h - 8}" text-anchor="middle">Neto en 12 meses (corridas; último tramo incluye la cola)</text></svg>')
    ruta.write_text("\n".join(partes), encoding="utf-8")


def svg_tornado(base, filas, titulo, ruta):
    w, fila_h, pad_l, pad = 640, 28, 120, 40
    h = pad * 2 + fila_h * len(filas)
    lo = min(min(f[1], f[2]) for f in filas + [("", base, base, 0)])
    hi = max(max(f[1], f[2]) for f in filas + [("", base, base, 0)] + [("", UMBRAL, UMBRAL, 0)])
    esc = (w - pad_l - 30) / (hi - lo)
    X = lambda v: pad_l + (v - lo) * esc
    partes = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" font-family="sans-serif" font-size="12">',
              '<rect width="100%" height="100%" fill="#fff"/>',
              f'<text x="10" y="20" font-size="14" font-weight="bold">{titulo}</text>']
    for i, (k, a, b, _) in enumerate(filas):
        y = pad + i * fila_h
        x1, x2 = sorted((X(a), X(b)))
        partes.append(f'<text x="{pad_l - 6}" y="{y + 17}" text-anchor="end">{k}</text>')
        partes.append(f'<rect x="{x1:.1f}" y="{y + 4}" width="{max(1, x2 - x1):.1f}" height="{fila_h - 8}" fill="#457b9d"/>')
    partes.append(f'<line x1="{X(base):.1f}" y1="{pad - 6}" x2="{X(base):.1f}" y2="{h - pad + 6}" stroke="#000"/>')
    partes.append(f'<text x="{X(base):.1f}" y="{h - pad + 20}" text-anchor="middle">base {base:.0f} €</text>')
    partes.append(f'<line x1="{X(UMBRAL):.1f}" y1="{pad - 6}" x2="{X(UMBRAL):.1f}" y2="{h - pad + 6}" stroke="#d62828" stroke-dasharray="4"/>')
    partes.append(f'<text x="{X(UMBRAL):.1f}" y="{pad - 10}" text-anchor="middle" fill="#d62828">500 €</text></svg>')
    ruta.write_text("\n".join(partes), encoding="utf-8")


# ----------------------------------------------------------------------- main
def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    semilla = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    out = Path(__file__).parent / "resultados"
    out.mkdir(exist_ok=True)
    resumen = {"n": n, "semilla": semilla, "ideas": {}}
    md = ["# Resultados del simulador de Fase 2 (v1)", "",
          f"Monte Carlo: {n} corridas por idea y lanzamiento, semilla {semilla}, 12 meses desde el lanzamiento.",
          "**Son estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.** Ecuaciones: `../../modelo/modelo.md`.", "",
          "## Resumen", "",
          "| Idea | Neto/venta web | Pesimista | Base | Optimista | MC mediana | MC p10–p90 | P(≥ 500 €) jun-27 | P(≥ 500 €) feb-27 |",
          "|---|---|---|---|---|---|---|---|---|"]
    detalle = []
    for idea, cfg in IDEAS.items():
        r = {}
        esc = {nom: simular(idea, valores_en(idea, q), 6) for nom, q in
               (("pesimista", 0.1), ("base", 0.5), ("optimista", 0.9))}
        for mes, et in ((6, "jun27"), (2, "feb27")):
            netos, ventas, corr = monte_carlo(idea, n, mes, semilla)
            s = sorted(netos)
            dec = statistics.quantiles(s, n=10)
            r[et] = {"mediana": statistics.median(s), "p10": dec[0], "p90": dec[-1],
                     "media": statistics.fmean(s), "prob_500": sum(x >= UMBRAL for x in s) / n,
                     "prob_0_ventas": sum(v == 0 for v in ventas) / n,
                     "ventas_mediana": statistics.median(ventas), "spearman": corr}
            if et == "jun27":
                svg_histograma(netos, f"{idea}: {cfg['nombre']} — lanzamiento jun-2027", out / f"hist_{idea}.svg")
        base, filas = tornado(idea, 6)
        svg_tornado(base, filas, f"{idea}: sensibilidad (p10 ↔ p90, resto en mediana)", out / f"tornado_{idea}.svg")
        r["escenarios"] = {k: {"neto": v[0], "ventas": v[1], "visitas": v[2]} for k, v in esc.items()}
        r["tornado"] = [{"param": k, "neto_p10": a, "neto_p90": b} for k, a, b, _ in filas]
        resumen["ideas"][idea] = r
        j, f = r["jun27"], r["feb27"]
        md.append(f"| {idea} {cfg['nombre']} | {neto_web(cfg['precio']):.2f} € | {esc['pesimista'][0]:.0f} € | "
                  f"{esc['base'][0]:.0f} € | {esc['optimista'][0]:.0f} € | {j['mediana']:.0f} € | "
                  f"{j['p10']:.0f}–{j['p90']:.0f} € | **{j['prob_500']:.1%}** | {f['prob_500']:.1%} |")
        detalle += [f"", f"## {idea}. {cfg['nombre']}", "",
                    f"- Escenario base: {esc['base'][2]:.0f} visitas y {esc['base'][1]:.1f} ventas en 12 meses → {esc['base'][0]:.0f} € netos.",
                    f"- Optimista: {esc['optimista'][2]:.0f} visitas, {esc['optimista'][1]:.1f} ventas → {esc['optimista'][0]:.0f} €.",
                    f"- Monte Carlo (jun-27): media {j['media']:.0f} €, mediana de ventas {j['ventas_mediana']:.0f}, "
                    f"P(0 ventas en 12 meses) = {j['prob_0_ventas']:.1%}.",
                    f"- Sensibilidad (tornado, de mayor a menor efecto): " +
                    ", ".join(f"`{k}` {a:.0f}↔{b:.0f} €" for k, a, b, _ in filas[:4]) + ".",
                    f"- Correlación de rangos con el neto (Monte Carlo): " +
                    ", ".join(f"`{k}` {c:+.2f}" for k, c in sorted(j["spearman"].items(), key=lambda x: -abs(x[1]))) + ".",
                    f"- Gráficas: `hist_{idea}.svg`, `tornado_{idea}.svg`."]
    md += detalle
    (out / "resultados_fase2.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (out / "resultados_fase2.json").write_text(json.dumps(resumen, indent=1, ensure_ascii=False), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
