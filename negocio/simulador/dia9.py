"""Día 9: umbral de corte para la validación barata de Etsy-EN.

Pregunta: ¿cuántas visitas al mes (en madurez) tienen que dar los anuncios en
inglés de inmobiliarias para que el catálogo BB+EN siga teniendo P(≥ 500 €) ≥ 50 %?
Con eso se fija la regla de "seguir / parar" de la prueba con 3–5 anuncios.

Método: igual que `dia8.py` (BB+EN, cota correlacionada), pero el `etsy_max` de la
pieza Etsy-EN se fija en una banda estrecha alrededor de V (V×0,9 – V×1,1) y se
barre V. El resto de parámetros (incluida la conversión p_etsy) sigue variando.

Traducción a lo que se OBSERVA en Etsy (visitas del mes m tras publicar):
  visitas(m) = V · (1 − e^(−m/τ)). Para no sobreestimar V se usa la rampa RÁPIDA
  (τ = 1 → en el mes 2 ya se ve el 86 % del techo) [E conservador].
  El dato de la prueba son visitas de ~5 anuncios; el pack completo tendrá más
  anuncios, pero NO se extrapola por número de anuncios (conservador).

Uso: python3 dia9.py [n_corridas] [semilla]
"""
import json
import math
import sys
from pathlib import Path

import simulador as S
import ajustes as A
import dia7 as D7
import dia8 as D8

VS = [10, 20, 30, 50, 75, 100, 150, 200, 300, 500, 800]
F_MES2 = 1 - math.exp(-2 / 1)   # τ = 1


def kcs_con_V(V):
    piezas = [(1.0, "etsy_es", False), (0.5, "etsy_es", False), (1.0, "etsy_en", True)]
    kcs = []
    for i, (f, canal, solo) in enumerate(piezas):
        c = D8.pieza(f, canal, solo)
        if canal == "etsy_en":
            c["params"]["etsy_max"] = ("log", V * 0.9, V * 1.1)
        kc = f"D9_V{V}_{i}"
        D7.registrar(kc, c)
        kcs.append(kc)
    return kcs


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    semilla = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    out = Path(__file__).parent / "resultados"
    filas = []
    for V in VS:
        kcs = kcs_con_V(V)
        r = A.resumir(*A.mc_catalogo(kcs, n, semilla, True))
        r["base"] = D8.escenarios(kcs)[1]
        r["V"] = V
        r["visitas_mes2_obs"] = V * F_MES2
        filas.append(r)
    umbral50 = next((f["V"] for f in filas if f["prob_500"] >= 0.5), None)
    umbral_base = next((f["V"] for f in filas if f["base"] >= 500), None)
    md = ["# Día 9 — umbral de corte de la validación Etsy-EN (catálogo BB+EN)", "",
          f"Monte Carlo: {n} corridas por fila, semilla {semilla}, cota correlacionada.",
          "**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.** Método: cabecera de `dia9.py`.", "",
          "| Techo Etsy-EN V (visitas/mes) | Visitas que se verían en el mes 2 | Base | MC mediana | P(0 ventas) | **P(≥ 500 €)** |",
          "|---|---|---|---|---|---|"]
    md += [f"| {f['V']} | ≈ {f['visitas_mes2_obs']:.0f} | {f['base']:.0f} € | {f['mediana']:.0f} € | "
           f"{f['prob_0_ventas']:.1%} | **{f['prob_500']:.1%}** |" for f in filas]
    md += ["", f"- Primer V con P(≥ 500 €) ≥ 50 %: **{umbral50}** visitas/mes.",
           f"- Primer V con caso base ≥ 500 €: **{umbral_base}** visitas/mes.",
           "- Regla derivada: ver `../investigacion/11_PLAN_VALIDACION_ETSY_EN.md`."]
    (out / "dia9.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (out / "dia9.json").write_text(json.dumps({"n": n, "semilla": semilla, "umbral_p50": umbral50,
                                               "umbral_base": umbral_base, "filas": filas},
                                              indent=1, ensure_ascii=False), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
