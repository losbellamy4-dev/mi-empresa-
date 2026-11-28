"""Día 20 (2026-11-28): punto de control — oferta de UN SOLO NIVEL (sin Pack Agencia 29 €).

Cambio real construido el Día 19: la web oculta la tarjeta del Pack Agencia (29 €) porque
prometía contenido que no existe. Hasta hoy TODAS las piezas del catálogo BB+2EN suponían
que un 10–30 % de los compradores elegía ese nivel de 29 € (f_premium), lo que subía el
ticket medio. Aquí se quita ese supuesto para que la probabilidad refleje la oferta real:
  · web (Payhip) y Etsy-ES: un solo pack a 17 €;
  · Etsy-EN: ancla = pack completo a 22 $ (≈ 20,24 €), sin nivel agencia;
  · opcional: sueltos a 5 $ con cuota 30 % (casos caníbal / aditivo, como el Día 14).
Base: escenario `oferta_grande` del Día 13 (p_muerto Etsy-EN 0,35, conversión Etsy-EN ×0,9).

Uso:  python3 dia20.py [n] [semilla]  → resultados/dia20.md y .json
Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.
"""
import json
import sys
from pathlib import Path

import simulador as S
import dia10 as D10
import dia14 as D14

PM_EN, CONV = 0.35, 0.9
P_ANCLA = 22 * D14.USD
S_SUELTOS = 0.3


def piezas(etiqueta, sin_premium, precio_en=None, mult_ventas=1.0):
    _, pzs = D10.COMBOS["BB+2EN"]
    pz = D10.registrar(f"d20_{etiqueta}", pzs)
    for kc, mkt in pz:
        cfg = S.IDEAS[kc]
        if sin_premium:
            cfg["params"].pop("f_premium", None)
        if mkt == "etsy_en":
            t, a, b = cfg["params"]["p_etsy"]
            m = CONV * mult_ventas
            cfg["params"]["p_etsy"] = (t, a * m, b * m)
            if precio_en is not None:
                cfg["precio"] = cfg["premium"] = cfg["precio_ref"] = precio_en
    return pz


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    semilla = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    out = Path(__file__).parent / "resultados"
    pm = dict(D10.P_MUERTO["base"], etsy_en=PM_EN)
    # neto medio de una venta de Etsy-EN mezclando ancla y sueltos (sin agencia)
    nm_mix = (1 - S_SUELTOS) * S.neto_etsy(P_ANCLA) + S_SUELTOS * S.neto_etsy(D14.P_SUELTO)
    p_mix = D14.precio_equivalente(nm_mix)
    casos = [
        ("ref_dia13", "Referencia Día 13/14: 17/29 € en todos los canales", piezas("ref", False)),
        ("un_nivel_17", "Un nivel: 17 € web/Etsy-ES, Etsy-EN también 17 €", piezas("u17", True)),
        ("un_nivel_ancla", "Un nivel: 17 € web/Etsy-ES, ancla 22 $ en Etsy-EN", piezas("ua", True, P_ANCLA)),
        ("ancla+sueltos_canibal", "Igual + 30 % sueltos 5 $ que sustituyen ventas del pack",
         piezas("uc", True, p_mix)),
        ("ancla+sueltos_aditivo", "Igual + 30 % sueltos 5 $ como ventas extra",
         piezas("uad", True, p_mix, 1 / (1 - S_SUELTOS))),
    ]
    res = {}
    md = ["# Día 20 — punto de control: oferta de un solo nivel (sin Pack Agencia 29 €)", "",
          f"Monte Carlo: {n} corridas, semilla {semilla}, catálogo `BB+2EN`, escenario `oferta_grande` "
          f"(p_muerto Etsy-EN {PM_EN}, conversión Etsy-EN ×{CONV}; resto de canales muertos en su valor base).",
          "**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.**", "",
          "| Caso | Descripción | **P(≥ 500 €)** | P(0 ventas) | Mediana | Media |", "|---|---|---|---|---|---|"]
    for k, desc, pz in casos:
        r = D10.mc(pz, n, semilla, pm)
        res[k] = {"desc": desc, **r}
        md.append(f"| `{k}` | {desc} | **{r['prob_500']:.1%}** | {r['prob_0_ventas']:.1%} | "
                  f"{r['mediana']:.0f} € | {r['media']:.0f} € |")
    d = res["un_nivel_ancla"]["prob_500"] - res["ref_dia13"]["prob_500"]
    md += ["", f"- Quitar el Pack Agencia y usar el ancla de 22 $ en Etsy-EN mueve P(≥ 500 €) **{d * 100:+.1f} pp** "
           f"({res['ref_dia13']['prob_500']:.1%} → {res['un_nivel_ancla']['prob_500']:.1%}).",
           f"- Neto por venta: web 17 € → {S.neto_web(17):.2f} € · Etsy 17 € → {S.neto_etsy(17):.2f} € · "
           f"Etsy-EN ancla 22 $ → {S.neto_etsy(P_ANCLA):.2f} € · mezcla ancla+30 % sueltos → {nm_mix:.2f} €.",
           "- La nueva cifra de referencia del proyecto es `un_nivel_ancla` (la oferta que existe hoy de verdad)."]
    (out / "dia20.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (out / "dia20.json").write_text(json.dumps({"n": n, "semilla": semilla, **res}, indent=1, ensure_ascii=False),
                                    encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
