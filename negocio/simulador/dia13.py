"""Día 13 (2026-11-21): ¿cuánto cuesta la "brecha de valor" en Etsy-EN?

Hallazgo de investigación (`investigacion/15_ETSY_NUEVOS_ANUNCIOS.md`):
  · Etsy da a cada anuncio nuevo un empujón temporal (horas–días) para medir cómo
    reacciona el comprador; después el puesto depende del Listing Quality Score
    (clics → favoritos → compras). [S: Etsy Seller Handbook / eRank]
  · Los rivales en "real estate instagram template(s)" venden packs de 50–1.000+
    diseños por 9–47 $; nuestros anuncios de prueba ofrecen 4 diseños por 9 $.
    Un comprador que compara lado a lado ve ~10–100× menos diseños por dólar.
Riesgo: CTR y conversión bajos durante el empujón → LQS bajo → el anuncio deja de
salir → canal muerto. El modelo v5 no lo tenía en cuenta explícitamente.

Aquí se barre, para el catálogo BB+2EN:
  · p_muerto de Etsy-EN (0,3 – 0,7) y
  · un multiplicador de la conversión de Etsy-EN (p_etsy × 0,5 / 0,75 / 1,0).
Escenarios con nombre [E]:
  oferta_actual   p_muerto 0,6, conv ×0,5   (brecha de valor sin corregir)
  base_v5         p_muerto 0,4, conv ×1,0   (supuesto del Día 10)
  oferta_grande   p_muerto 0,35, conv ×0,9  (ancla = pack de ~38 diseños × 3 paletas,
                                             precio en la banda de los rivales)

Uso:  python3 dia13.py [n] [semilla]  → resultados/dia13.md y .json
Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.
"""
import json
import sys
from pathlib import Path

import simulador as S
import dia10 as D10

PM_EN = (0.3, 0.4, 0.5, 0.6, 0.7)
CONV = (0.5, 0.75, 1.0)
ESCENARIOS = {"oferta_actual": (0.6, 0.5), "base_v5": (0.4, 1.0), "oferta_grande": (0.35, 0.9)}


def piezas_con_conv(mult, etiqueta):
    nombre, piezas = D10.COMBOS["BB+2EN"]
    pz = D10.registrar(f"d13_{etiqueta}", piezas)
    for kc, mkt in pz:
        if mkt == "etsy_en":
            t, a, b = S.IDEAS[kc]["params"]["p_etsy"]
            S.IDEAS[kc]["params"]["p_etsy"] = (t, a * mult, b * mult)
    return pz


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    semilla = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    out = Path(__file__).parent / "resultados"
    pz_por_conv = {m: piezas_con_conv(m, str(m)) for m in CONV + (0.9,)}
    rejilla = {}
    md = ["# Día 13 — brecha de valor en Etsy-EN (catálogo `BB+2EN`)", "",
          f"Monte Carlo: {n} corridas por celda, semilla {semilla}. Resto de canales muertos en su valor base "
          "(SEO 0,60 · redes 0,40 · Etsy-ES 0,50 · Hotmart 0,60).",
          "**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.**", "",
          "## 1. P(≥ 500 €) según p_muerto de Etsy-EN (filas) y conversión de Etsy-EN (columnas)", "",
          "| p_muerto Etsy-EN | " + " | ".join(f"conv ×{m}" for m in CONV) + " |",
          "|---|" + "---|" * len(CONV)]
    for p in PM_EN:
        fila = []
        for m in CONV:
            pm = dict(D10.P_MUERTO["base"], etsy_en=p)
            r = D10.mc(pz_por_conv[m], n, semilla, pm)
            rejilla[f"{p}|{m}"] = r
            fila.append(f"{r['prob_500']:.1%}")
        md.append(f"| {p} | " + " | ".join(fila) + " |")
    esc = {}
    md += ["", "## 2. Escenarios con nombre", "",
           "| Escenario | p_muerto EN | conv × | **P(≥500)** | P(0 ventas) | Mediana |", "|---|---|---|---|---|---|"]
    for k, (p, m) in ESCENARIOS.items():
        r = D10.mc(pz_por_conv[m], n, semilla, dict(D10.P_MUERTO["base"], etsy_en=p))
        esc[k] = {"p_muerto_en": p, "conv": m, **r}
        md.append(f"| `{k}` | {p} | {m} | **{r['prob_500']:.1%}** | {r['prob_0_ventas']:.1%} | {r['mediana']:.0f} € |")
    d = esc["oferta_grande"]["prob_500"] - esc["oferta_actual"]["prob_500"]
    md += ["", f"- Corregir la brecha de valor (de `oferta_actual` a `oferta_grande`) vale **{d * 100:+.1f} pp** de P(≥ 500 €).",
           "- Los escenarios con nombre son supuestos [E]; la cifra útil es el **orden de magnitud** del efecto."]
    (out / "dia13.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (out / "dia13.json").write_text(json.dumps({"n": n, "semilla": semilla, "rejilla": rejilla, "escenarios": esc},
                                               indent=1, ensure_ascii=False), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
