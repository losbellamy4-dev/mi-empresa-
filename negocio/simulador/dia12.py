"""Día 12 (2026-11-19): ¿qué canal muerto pesa más? → dónde invertir el esfuerzo.

Pregunta: la cola del Día 10 pedía "palancas para bajar p_muerto del SEO". Antes de
trabajar el SEO hay que saber si merece la pena: barrido de p_muerto de UN canal
cada vez (los demás en su valor base de dia10.P_MUERTO) para el catálogo BB+2EN y
para BB+EN, midiendo cuánto cambia P(≥ 500 €).

Lectura: la pendiente ΔP(≥500)/Δp_muerto de cada canal = "valor de reducir el riesgo
de ese canal". Si el SEO tiene poca pendiente, es mejor dedicar las horas a otro canal.

Uso:  python3 dia12.py [n] [semilla]  → resultados/dia12.md y .json
Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.
"""
import json
import sys
from pathlib import Path

import dia10 as D10

CANALES = ("seo", "red", "etsy_es", "etsy_en")
VALORES = (0.2, 0.4, 0.6, 0.8)
COMBOS = ("BB+2EN", "BB+EN")


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    semilla = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    out = Path(__file__).parent / "resultados"
    res = {}
    md = ["# Día 12 — ¿qué canal muerto pesa más?", "",
          f"Monte Carlo: {n} corridas por celda, semilla {semilla}. Se varía la probabilidad de canal muerto "
          "de **un** canal; el resto queda en su valor base (SEO 0,60 · redes 0,40 · Etsy-ES 0,50 · Etsy-EN 0,40 · Hotmart 0,60).",
          "**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.**", ""]
    for combo in COMBOS:
        nombre, piezas = D10.COMBOS[combo]
        pz = D10.registrar(f"d12_{combo}", piezas)
        base = D10.mc(pz, n, semilla, D10.P_MUERTO["base"])
        res[combo] = {"base": base, "barrido": {}}
        md += [f"## `{combo}` — {nombre}", "",
               f"Base: P(≥500) = **{base['prob_500']:.1%}**, mediana {base['mediana']:.0f} €.", "",
               "| Canal | " + " | ".join(f"p_muerto = {v:.1f}" for v in VALORES) + " | Pendiente (pp por −0,1) |",
               "|---|" + "---|" * (len(VALORES) + 1)]
        for c in CANALES:
            fila = []
            for v in VALORES:
                pm = dict(D10.P_MUERTO["base"], **{c: v})
                fila.append(D10.mc(pz, n, semilla, pm)["prob_500"])
            pend = (fila[0] - fila[-1]) / ((VALORES[-1] - VALORES[0]) / 0.1) * 100
            res[combo]["barrido"][c] = {"valores": VALORES, "prob_500": fila, "pendiente_pp": pend}
            md.append(f"| {c} | " + " | ".join(f"{x:.1%}" for x in fila) + f" | **{pend:+.1f}** |")
        md.append("")
    orden = sorted(CANALES, key=lambda c: -res["BB+2EN"]["barrido"][c]["pendiente_pp"])
    md += ["## Lectura", "",
           "- Orden de importancia en `BB+2EN` (más puntos de P(≥500) por cada 0,1 menos de p_muerto): "
           + " > ".join(f"**{c}**" for c in orden) + "."]
    (out / "dia12.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (out / "dia12.json").write_text(json.dumps({"n": n, "semilla": semilla, **res}, indent=1, ensure_ascii=False),
                                    encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
