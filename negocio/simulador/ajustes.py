"""Ajustes de idea (v2, Día 6): vuelta parcial a Fase 1 con el simulador.

El VEREDICTO v1 dice que ninguna finalista llega a 500 € en el caso base.
Aquí se prueban, sin coste real, los ajustes candidatos sobre A y B:

  - Subir el ticket (con elasticidad precio-conversión, rango conservador).
  - Nivel premium opcional junto al pack normal (sube el ticket medio).
  - Producto escalera en Etsy (barato, lleva al pack completo en la web).
  - Catálogo A+B (dos públicos; el tiempo del dueño en redes se reparte).

Supuestos nuevos en ../modelo/modelo.md §7. Reutiliza simulador.py.
Uso: python3 ajustes.py [n_corridas] [semilla]
"""
import copy
import json
import random
import statistics
import sys
from pathlib import Path

import simulador as S

# Elasticidad de la conversión al precio: conv ∝ (P/P_ref)^-e.
# Regla práctica "+10 % precio → −20 % conversión" en mercados saturados [S, blog SaaS]
# → e ≈ 2 como extremo desfavorable; productos diferenciados, menos [E].
ELAST = ("uni", 1.0, 2.0)


def variante(base, nombre, precio=None, extra=None, **cfg_extra):
    cfg = copy.deepcopy(S.IDEAS[base])
    cfg["nombre"] = nombre
    if precio is not None:
        cfg["precio_ref"] = cfg["precio"]
        cfg["precio"] = precio
        cfg["params"]["elast"] = ELAST
    cfg.update(cfg_extra)
    cfg["params"].update(extra or {})
    return cfg


VARIANTES = {
    "A_v1": variante("A", "A tal cual (v1)"),
    "A_21": variante("A", "A con pack a 21 €", precio=21),
    "A_niv": variante("A", "A 15 € + premium 24 € (2 oposiciones + plantillas extra)",
                      premium=24, extra={"f_premium": ("uni", 0.10, 0.30)}),
    "B_v1": variante("B", "B tal cual (v1)"),
    "B_29": variante("B", "B con pack a 29 €", precio=29),
    "B_niv": variante("B", "B 17 € + pack agencia 29 €",
                      premium=29, extra={"f_premium": ("uni", 0.10, 0.30)}),
    "B_esc": variante("B", "B con escalera en Etsy (4 € → pack 17 €)", tripwire=4,
                      extra={"mult_tw": ("uni", 1.5, 3.0),          # lo barato convierte más [E]
                             "p_upsell": ("log", 0.02, 0.12)}),     # vendedores citan 2–8 % y hasta 50 % en checkout [S]; conservador [E]
    "B_niv_esc": variante("B", "B 17 €/29 € + escalera en Etsy", premium=29, tripwire=4,
                          extra={"f_premium": ("uni", 0.10, 0.30), "mult_tw": ("uni", 1.5, 3.0),
                                 "p_upsell": ("log", 0.02, 0.12)}),
}
for k, cfg in VARIANTES.items():
    S.IDEAS[k] = cfg
    S.ESTACIONALIDAD[k] = S.ESTACIONALIDAD[k[0]]

# Catálogos: dos productos a la vez; el dueño reparte sus redes (red_base a la
# mitad en cada uno) y paga un solo dominio. "BB" = el producto de B para un
# segundo sector profesional (p. ej. clínicas/estética), con la mitad de tráfico
# porque su demanda en español no está medida [E].
# Cada catálogo se simula de dos formas:
#   indep.  → el éxito de un producto no dice nada del otro (cota optimista);
#   correl. → mismos cuantiles de sorteo en los parámetros comunes: si el
#             vendedor/Etsy funciona mal en uno, funciona mal en el otro (cota conservadora).
CATALOGOS = {
    "AB": ((("A_niv", 1.0), ("B_niv", 1.0)), "Catálogo A (15/24 €) + B (17/29 €)"),
    "BB": ((("B_niv", 1.0), ("B_niv", 0.5)), "Catálogo B en dos sectores (17/29 €; 2.º sector con mitad de tráfico)"),
}
TRAFICO = ("seo_max", "etsy_max")


def pieza(cfg, f_trafico):
    c = copy.deepcopy(cfg)
    for k, f in [("red_base", 0.5)] + [(k, f_trafico) for k in TRAFICO]:
        t, a, b = c["params"][k]
        c["params"][k] = (t, a * f, b * f)
    return c


def mc_catalogo(kcs, n, semilla, correlado):
    rng = random.Random(semilla)
    netos, ventas = [], []
    for _ in range(n):
        u, tot, vt = {}, S.COSTE_FIJO, 0.0          # el dominio se paga una sola vez
        for kc in kcs:
            v = {}
            for p, d in S.IDEAS[kc]["params"].items():
                if correlado and p in u:
                    q = u[p]
                else:
                    q = u[p] = min(max(rng.random(), 1e-9), 1 - 1e-9)
                v[p] = S.cuantil(d, q)
            neto, vv, _ = S.simular(kc, v, 6, rng)
            tot += neto
            vt += vv
        netos.append(tot)
        ventas.append(vt)
    return netos, ventas


def resumir(netos, ventas):
    s = sorted(netos)
    dec = statistics.quantiles(s, n=10)
    n = len(s)
    return {"mediana": statistics.median(s), "p10": dec[0], "p90": dec[-1],
            "prob_500": sum(x >= S.UMBRAL for x in s) / n,
            "prob_0_ventas": sum(v == 0 for v in ventas) / n,
            "ventas_mediana": statistics.median(ventas)}


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    semilla = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    out = Path(__file__).parent / "resultados"
    res = {}
    for k in VARIANTES:
        netos, ventas, _ = S.monte_carlo(k, n, 6, semilla)
        r = resumir(netos, ventas)
        r["base"] = S.simular(k, S.valores_en(k, 0.5), 6)[0]
        r["pesimista"] = S.simular(k, S.valores_en(k, 0.1), 6)[0]
        r["optimista"] = S.simular(k, S.valores_en(k, 0.9), 6)[0]
        res[k] = r

    nombres = {k: v["nombre"] for k, v in VARIANTES.items()}
    for cat, (piezas, nombre) in CATALOGOS.items():
        kcs, esc = [], [S.COSTE_FIJO] * 3
        for i, (k, f) in enumerate(piezas):
            kc = f"{k}_{cat}_{i}"
            S.IDEAS[kc] = pieza(S.IDEAS[k], f)
            S.ESTACIONALIDAD[kc] = S.ESTACIONALIDAD[k]
            kcs.append(kc)
            for j, q in enumerate((0.5, 0.1, 0.9)):
                esc[j] += S.simular(kc, S.valores_en(kc, q), 6)[0]
        for correlado, et in ((False, "indep."), (True, "correl.")):
            r = resumir(*mc_catalogo(kcs, n, semilla, correlado))
            r["base"], r["pesimista"], r["optimista"] = esc
            res[f"{cat}_{'cor' if correlado else 'ind'}"] = r
            nombres[f"{cat}_{'cor' if correlado else 'ind'}"] = f"{nombre}, {et}"

    md = ["# Ajustes de idea — resultados del simulador (v2, Día 6)", "",
          f"Monte Carlo: {n} corridas por variante, semilla {semilla}, lanzamiento jun-2027, 12 meses.",
          "**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.** Supuestos nuevos: `../../modelo/modelo.md` §7.", "",
          "| Variante | Pesimista | Base | Optimista | MC mediana | MC p10–p90 | P(0 ventas) | **P(≥ 500 €)** |",
          "|---|---|---|---|---|---|---|---|"]
    for k, r in res.items():
        md.append(f"| `{k}` {nombres[k]} | {r['pesimista']:.0f} € | {r['base']:.0f} € | {r['optimista']:.0f} € | "
                  f"{r['mediana']:.0f} € | {r['p10']:.0f}–{r['p90']:.0f} € | {r['prob_0_ventas']:.1%} | **{r['prob_500']:.1%}** |")
    (out / "ajustes_v2.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (out / "ajustes_v2.json").write_text(json.dumps({"n": n, "semilla": semilla, "variantes": res},
                                                    indent=1, ensure_ascii=False), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
