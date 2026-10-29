"""Día 7: acotar `etsy_max` de B y tornado del catálogo BB.

Etsy bloquea la consulta automática (403/captcha), así que no hay recuento
directo de anuncios ni reseñas. Las señales indirectas (ver
../investigacion/09_ETSY_Y_SEGUNDO_SECTOR.md) indican que el comprador en
español de plantillas sectoriales compra sobre todo en Hotmart/Gumroad y casi
no aparece en Etsy. Por eso se prueba el rango v2 de `etsy_max` (20–800) frente
a uno más conservador (10–400, v3) y una prueba de estrés (5–200).

También calcula el tornado del catálogo BB (inmobiliarias + psicólogos, cota
correlacionada): cada parámetro se mueve a la vez en los dos productos.

Uso: python3 dia7.py [n_corridas] [semilla]
"""
import copy
import json
import sys
from pathlib import Path

import simulador as S
import ajustes as A

RANGOS_ETSY = {"v2": (20, 800), "v3": (10, 400), "estres": (5, 200)}


def con_etsy(cfg, rango):
    c = copy.deepcopy(cfg)
    c["params"]["etsy_max"] = ("log", *rango)
    return c


def registrar(k, cfg):
    S.IDEAS[k] = cfg
    S.ESTACIONALIDAD[k] = S.ESTACIONALIDAD["B"]


def piezas_bb(et):
    """Las dos piezas del catálogo BB con el rango de Etsy `et`."""
    kcs = []
    for i, f in enumerate((1.0, 0.5)):
        kc = f"BB_{et}_{i}"
        registrar(kc, A.pieza(con_etsy(A.VARIANTES["B_niv"], RANGOS_ETSY[et]), f))
        kcs.append(kc)
    return kcs


def neto_catalogo(kcs, qs):
    """Neto determinista del catálogo con cada parámetro en el cuantil qs[p] (por defecto 0,5)."""
    tot = S.COSTE_FIJO
    for kc in kcs:
        v = {}
        for p, d in S.IDEAS[kc]["params"].items():
            v[p] = S.cuantil(d, qs.get(p, 0.5))
        tot += S.simular(kc, v, 6)[0]
    return tot


def tornado_catalogo(kcs):
    base = neto_catalogo(kcs, {})
    filas = []
    for p in S.IDEAS[kcs[0]]["params"]:
        res = []
        for q_fav in (0.1, 0.9):
            q = 1 - q_fav if p in S.DESFAVORABLE_ALTO else q_fav
            res.append(neto_catalogo(kcs, {p: q}))
        filas.append((p, res[0], res[1], abs(res[1] - res[0])))
    filas.sort(key=lambda f: -f[3])
    return base, filas


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    semilla = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    out = Path(__file__).parent / "resultados"
    res = {}
    md = ["# Día 7 — `etsy_max` de B y tornado del catálogo BB", "",
          f"Monte Carlo: {n} corridas, semilla {semilla}, lanzamiento jun-2027, 12 meses.",
          "**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.**", "",
          "## 1. Sensibilidad al rango de visitas en Etsy", "",
          "| Rango `etsy_max` (visitas/mes) | Variante | Base | MC mediana | MC p10–p90 | **P(≥ 500 €)** |",
          "|---|---|---|---|---|---|"]
    for et, rango in RANGOS_ETSY.items():
        k = f"B_niv_{et}"
        registrar(k, con_etsy(A.VARIANTES["B_niv"], rango))
        netos, ventas, _ = S.monte_carlo(k, n, 6, semilla)
        r = A.resumir(netos, ventas)
        r["base"] = S.simular(k, S.valores_en(k, 0.5), 6)[0]
        res[k] = r
        md.append(f"| {et} {rango[0]}–{rango[1]} | B 17/29 € (un sector) | {r['base']:.0f} € | {r['mediana']:.0f} € | "
                  f"{r['p10']:.0f}–{r['p90']:.0f} € | **{r['prob_500']:.1%}** |")
        kcs = piezas_bb(et)
        r = A.resumir(*A.mc_catalogo(kcs, n, semilla, True))
        r["base"] = neto_catalogo(kcs, {})
        res[f"BB_cor_{et}"] = r
        md.append(f"| {et} {rango[0]}–{rango[1]} | BB inmobiliarias + psicólogos, correl. | {r['base']:.0f} € | "
                  f"{r['mediana']:.0f} € | {r['p10']:.0f}–{r['p90']:.0f} € | **{r['prob_500']:.1%}** |")

    base, filas = tornado_catalogo(piezas_bb("v3"))
    S.svg_tornado(base, filas, "BB (inmobiliarias + psicólogos), Etsy v3: p10 ↔ p90 en ambos productos",
                  out / "tornado_BB.svg")
    res["tornado_BB_v3"] = {"base": base, "filas": [{"param": p, "neto_p10": a, "neto_p90": b} for p, a, b, _ in filas]}
    md += ["", "## 2. Tornado del catálogo BB (rango Etsy v3, cota correlacionada)", "",
           f"Caso base determinista: **{base:.0f} €**. Cada fila mueve un parámetro de p10 a p90 en los dos productos a la vez.", "",
           "| Parámetro | Neto con p10 | Neto con p90 | Amplitud |", "|---|---|---|---|"]
    md += [f"| `{p}` | {a:.0f} € | {b:.0f} € | {d:.0f} € |" for p, a, b, d in filas]
    md += ["", "Gráfica: `tornado_BB.svg`."]
    (out / "dia7.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (out / "dia7.json").write_text(json.dumps({"n": n, "semilla": semilla, "resultados": res},
                                              indent=1, ensure_ascii=False), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
