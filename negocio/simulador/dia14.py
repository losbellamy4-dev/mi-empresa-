"""Día 14 (2026-11-22): punto de control de la oferta v2 de Etsy-EN.

Cambio construido hoy (`producto/ANUNCIOS_PRUEBA.md` v2):
  · ancla = pack base completo (34 diseños × 3 paletas, ES+EN, + calendario de 30 días) a 22 $;
  · 4 anuncios sueltos a 4–6 $ (media ≈ 5 $) que enlazan al pack.
El modelo hasta el Día 13 suponía que cada venta de Etsy-EN era el pack B (17 € + 10–30 % pack
agencia 29 €). Con sueltos baratos el ticket medio baja y las comisiones FIJAS de Etsy
(0,20 $ de publicación + 0,30 € de pago ≈ 0,49 €/venta en `neto_etsy`) pesan más.

Supuestos [E] (no hay dato; se barren):
  · s = cuota de ventas de Etsy-EN que son sueltos: 0,3 / 0,45 / 0,6.
  · Dos casos extremos para los sueltos:
      canibal  → las ventas totales no cambian; parte de ellas pasan a ser sueltos (peor caso).
      aditivo  → las ventas del pack no cambian y los sueltos son ventas EXTRA (mejor caso).
  · Pack agencia en Etsy-EN: se mantiene (10–30 % de las ventas de pack a 29 € ≈ 31 $).
  · Cambio USD→EUR: 1 $ = 0,92 € [E, aprox. 2026].
Base: escenario `oferta_grande` del Día 13 (p_muerto Etsy-EN 0,35, conversión ×0,9).

Uso:  python3 dia14.py [n] [semilla]  → resultados/dia14.md y .json
Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.
"""
import json
import sys
from pathlib import Path

import simulador as S
import dia10 as D10

USD = 0.92
P_ANCLA = 22 * USD
P_SUELTO = 5 * USD
P_AGENCIA = 29.0
F_PREM = 0.20            # punto medio de ("uni", 0.10, 0.30)
S_SUELTOS = (0.3, 0.45, 0.6)
PM_EN, CONV = 0.35, 0.9


def neto_medio(s):
    """Neto medio por venta de Etsy-EN con cuota s de sueltos."""
    pack = (1 - F_PREM) * S.neto_etsy(P_ANCLA) + F_PREM * S.neto_etsy(P_AGENCIA)
    return (1 - s) * pack + s * S.neto_etsy(P_SUELTO)


def precio_equivalente(neto):
    """Precio bruto p con neto_etsy(p) = neto (neto_etsy es lineal en p)."""
    a, b = S.neto_etsy(10.0), S.neto_etsy(20.0)
    pend = (b - a) / 10.0
    return 10.0 + (neto - a) / pend


def piezas(etiqueta, p_eq=None, mult_ventas=1.0):
    """Catálogo BB+2EN; las piezas de Etsy-EN con precio equivalente y conversión ajustada."""
    _, pzs = D10.COMBOS["BB+2EN"]
    pz = D10.registrar(f"d14_{etiqueta}", pzs)
    for kc, mkt in pz:
        if mkt == "etsy_en":
            cfg = S.IDEAS[kc]
            t, a, b = cfg["params"]["p_etsy"]
            m = CONV * mult_ventas
            cfg["params"]["p_etsy"] = (t, a * m, b * m)
            if p_eq is not None:     # el ticket ya incluye el pack agencia: quitar el premium
                cfg["precio"] = cfg["premium"] = p_eq
                cfg["params"].pop("f_premium", None)
                cfg["precio_ref"] = p_eq
    return pz


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    semilla = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    out = Path(__file__).parent / "resultados"
    pm = dict(D10.P_MUERTO["base"], etsy_en=PM_EN)
    modelo_ant = (1 - F_PREM) * S.neto_etsy(17) + F_PREM * S.neto_etsy(29)
    filas, res = [], {}
    ref = D10.mc(piezas("ref"), n, semilla, pm)
    res["ref_dia13"] = {"neto_venta": modelo_ant, **ref}
    for s in S_SUELTOS:
        nm = neto_medio(s)
        peq = precio_equivalente(nm)
        for caso in ("canibal", "aditivo"):
            if caso == "canibal":
                r = D10.mc(piezas(f"{caso}{s}", peq), n, semilla, pm)
                nv = nm
            else:   # pack igual + sueltos extra: ventas ×1/(1-s), neto medio = nm
                r = D10.mc(piezas(f"{caso}{s}", peq, 1 / (1 - s)), n, semilla, pm)
                nv = nm
            res[f"{caso}|{s}"] = {"s": s, "caso": caso, "neto_venta": nv, "precio_eq": peq, **r}
            filas.append((s, caso, nv, r))
    md = ["# Día 14 — punto de control: oferta v2 de Etsy-EN (ancla 22 $ + sueltos 4–6 $)", "",
          f"Monte Carlo: {n} corridas, semilla {semilla}, catálogo `BB+2EN`, escenario base `oferta_grande` "
          f"(p_muerto Etsy-EN {PM_EN}, conversión ×{CONV}). Cambio 1 $ = {USD} €.",
          "**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.**", "",
          f"- Neto por venta de Etsy-EN que suponía el modelo (pack 17 € / 29 €): **{modelo_ant:.2f} €**.",
          f"- Neto del ancla 22 $ ({P_ANCLA:.2f} €): {S.neto_etsy(P_ANCLA):.2f} € · de un suelto 5 $ "
          f"({P_SUELTO:.2f} €): **{S.neto_etsy(P_SUELTO):.2f} €** (las comisiones fijas se comen ≈ "
          f"{1 - S.neto_etsy(P_SUELTO) / (P_SUELTO / 1.21):.0%} del precio sin IVA).", "",
          "| Cuota de sueltos | Caso | Neto/venta Etsy-EN | **P(≥ 500 €)** | P(0 ventas) | Mediana |",
          "|---|---|---|---|---|---|",
          f"| — | referencia Día 13 | {modelo_ant:.2f} € | **{ref['prob_500']:.1%}** | {ref['prob_0_ventas']:.1%} | {ref['mediana']:.0f} € |"]
    for s, caso, nv, r in filas:
        md.append(f"| {s:.0%} | {caso} | {nv:.2f} € | **{r['prob_500']:.1%}** | {r['prob_0_ventas']:.1%} | {r['mediana']:.0f} € |")
    peor = min(r["prob_500"] for _, _, _, r in filas)
    mejor = max(r["prob_500"] for _, _, _, r in filas)
    md += ["", f"- Rango de la oferta v2: **{peor:.1%} – {mejor:.1%}** frente a {ref['prob_500']:.1%} de referencia.",
           "- Lectura: los sueltos a 4–6 $ solo compensan si traen compradores **nuevos** (caso aditivo). "
           "Si sustituyen ventas del pack (caníbal), restan. Ver decisión en la BITÁCORA del Día 14."]
    (out / "dia14.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (out / "dia14.json").write_text(json.dumps({"n": n, "semilla": semilla, **res}, indent=1, ensure_ascii=False),
                                    encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
