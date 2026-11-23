"""Día 10: auditoría del supuesto P(0 ventas) ≈ 0 % → "canal muerto".

Problema detectado el Día 9: en todas las combinaciones el simulador casi nunca
produce 0 ventas en 12 meses, pero los datos externos dicen que es lo normal:
  · Gumroad: el 44 % de los productos no ha vendido nada [S, Día 1].
  · Ahrefs (2023, ~14.000 M de páginas): el 96,55 % de las páginas recibe 0
    visitas de Google; solo el 3,45 % recibe > 10/mes [S: ahrefs.com/blog/search-traffic-study].
  · Etsy: ≈ 65 % de las tiendas nunca vende [S débil: sellertoolshq.com, sin
    metodología; incluye tiendas abandonadas].
El modelo usaba lognormales cuyo p5 ya es "poco tráfico", pero nunca "cero".
En la realidad un canal nuevo suele ser binario: o arranca o no da nada.

Cambio: en cada corrida, cada CANAL puede estar "muerto" (tráfico 0 durante los
12 meses) con probabilidad p_muerto. Si está vivo, se usa la distribución de
siempre (que ya era conservadora). La muerte de un canal es COMÚN a todas las
piezas del catálogo (si Google no indexa la web, no la indexa para ningún sector).

Probabilidades [E, conservadoras, ver ../investigacion/13_CANAL_MUERTO.md]:
  canal      base   estrés   razonamiento
  seo        0.60   0.80     Ahrefs 96,5 % de páginas a 0; aquí hay ~10 páginas
                             de cola larga, sin enlaces. 0,60 por sitio, no por página.
  red        0.40   0.60     redes de un desconocido: lo habitual es alcance ≈ 0.
  etsy_es    0.50   0.70     65 % de tiendas sin venta (incluye abandonadas).
  etsy_en    0.40   0.60     mercado más grande, casos reales de tiendas nuevas que venden.
  hotmart    0.60   0.80     sin datos de tráfico orgánico; depende de afiliados.

Uso: python3 dia10.py [n_corridas] [semilla]
"""
import json
import math
import random
import sys
from pathlib import Path

import simulador as S
import ajustes as A
import dia7 as D7
import dia8 as D8

P_MUERTO = {
    "base":   {"seo": 0.60, "red": 0.40, "etsy_es": 0.50, "etsy_en": 0.40, "hotmart": 0.60},
    "estres": {"seo": 0.80, "red": 0.60, "etsy_es": 0.70, "etsy_en": 0.60, "hotmart": 0.80},
    "nada":   {"seo": 0.0, "red": 0.0, "etsy_es": 0.0, "etsy_en": 0.0, "hotmart": 0.0},
}


def canal_mkt(canal):
    return "etsy_en" if canal.startswith("etsy_en") else canal


def registrar(nombre, piezas, override_en=None):
    out = []
    for i, (f, canal, solo) in enumerate(piezas):
        c = D8.pieza(f, canal, solo)
        if override_en is not None and canal.startswith("etsy_en"):
            c["params"]["etsy_max"] = override_en
        kc = f"D10_{nombre}_{i}"
        D7.registrar(kc, c)
        out.append((kc, canal_mkt(canal)))
    return out


def mc(piezas, n, semilla, pm, vivo_forzado=()):
    """Como ajustes.mc_catalogo (cota correlacionada) + canales muertos."""
    rng = random.Random(semilla)
    netos, ventas = [], []
    for _ in range(n):
        muerto = {c: (c not in vivo_forzado) and rng.random() < p for c, p in pm.items()}
        u, tot, vt = {}, S.COSTE_FIJO, 0.0
        for kc, mkt in piezas:
            v = {}
            for p, d in S.IDEAS[kc]["params"].items():
                q = u[p] if p in u else u.setdefault(p, min(max(rng.random(), 1e-9), 1 - 1e-9))
                v[p] = S.cuantil(d, q)
            if muerto["seo"]:
                v["seo_max"] = 0.0
            if muerto["red"]:
                v["red_base"] = 0.0
            if muerto[mkt] and "etsy_max" in v:
                v["etsy_max"] = 0.0
            neto, vv, _ = S.simular(kc, v, 6, rng)
            tot += neto
            vt += vv
        netos.append(tot)
        ventas.append(vt)
    return A.resumir(netos, ventas) | {"media": sum(netos) / n}


COMBOS = {k: D8.COMBOS[k] for k in ("BB_etsyES", "BB+EN", "BB_todo", "BB+EN_estres", "B_EN_solo")}
COMBOS["BB+2EN"] = ("BB Etsy-ES + inmobiliarias y psicólogos en Etsy-EN",
                     [(1.0, "etsy_es", False), (0.5, "etsy_es", False), (1.0, "etsy_en", True), (0.5, "etsy_en", True)])
COMBOS = {"B_solo": ("Calibración: solo inmobiliarias (web + Etsy-ES)", [(1.0, "etsy_es", False)])} | COMBOS
VS = [50, 75, 100, 150, 200, 300, 500]
F_MES2 = 1 - math.exp(-2)


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    semilla = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    out = Path(__file__).parent / "resultados"
    res = {"combos": {}, "umbral": {}}
    md = ["# Día 10 — auditoría de P(0 ventas): canales muertos", "",
          f"Monte Carlo: {n} corridas, semilla {semilla}, lanzamiento jun-2027, 12 meses, cota correlacionada.",
          "**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.** Supuestos: cabecera de `dia10.py`.", "",
          "## 1. Combinaciones de canal (v4 sin canales muertos → v5 con ellos)", "",
          "| Combinación | P(≥500) v4 | **P(≥500) v5 base** | P(≥500) v5 estrés | P(0 ventas) v4 → v5 base | Mediana v4 → v5 | Media v5 |",
          "|---|---|---|---|---|---|---|"]
    for k, (nombre, piezas) in COMBOS.items():
        pz = registrar(k, piezas)
        r = {e: mc(pz, n, semilla, P_MUERTO[e]) for e in ("nada", "base", "estres")}
        res["combos"][k] = {"nombre": nombre, **r}
        a, b, c = r["nada"], r["base"], r["estres"]
        md.append(f"| `{k}` {nombre} | {a['prob_500']:.1%} | **{b['prob_500']:.1%}** | {c['prob_500']:.1%} | "
                  f"{a['prob_0_ventas']:.1%} → {b['prob_0_ventas']:.1%} | {a['mediana']:.0f} → {b['mediana']:.0f} € | {b['media']:.0f} € |")

    # Umbral de la validación: si la prueba de Etsy-EN MIDE V visitas, ese canal está vivo
    # (se fuerza vivo), pero SEO, redes y Etsy-ES siguen pudiendo morir.
    md += ["", "## 2. Regla de la prueba Etsy-EN, recalculada", "",
           "La prueba de 5 anuncios **observa** el tráfico de Etsy-EN, así que en estas filas ese canal está vivo; "
           "los demás canales siguen pudiendo morir (probabilidades base).", "",
           "| Techo Etsy-EN V | Visitas vistas en el mes 2 | P(≥500) v4 (Día 9) | **P(≥500) v5** | P(0 ventas) v5 | Mediana v5 |",
           "|---|---|---|---|---|---|"]
    d9 = {f["V"]: f["prob_500"] for f in json.loads((out / "dia9.json").read_text())["filas"]}
    piezas_en = D8.COMBOS["BB+EN"][1]
    filas = []
    for V in VS:
        pz = registrar(f"V{V}", piezas_en, ("log", V * 0.9, V * 1.1))
        r = mc(pz, n, semilla, P_MUERTO["base"], vivo_forzado=("etsy_en",)) | {"V": V}
        filas.append(r)
        md.append(f"| {V} | ≈ {V * F_MES2:.0f} | {d9.get(V, float('nan')):.1%} | **{r['prob_500']:.1%}** | "
                  f"{r['prob_0_ventas']:.1%} | {r['mediana']:.0f} € |")
    u50 = next((f["V"] for f in filas if f["prob_500"] >= 0.5), None)
    res["umbral"] = {"filas": filas, "V_p50": u50}
    md += ["", f"- Primer V con P(≥ 500 €) ≥ 50 % (v5): **{u50}** visitas/mes en madurez "
           f"(≈ {u50 * F_MES2:.0f} visibles en el mes 2)." if u50 else "- Ningún V probado llega al 50 %."]
    (out / "dia10.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (out / "dia10.json").write_text(json.dumps({"n": n, "semilla": semilla, "p_muerto": P_MUERTO, **res},
                                               indent=1, ensure_ascii=False), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
