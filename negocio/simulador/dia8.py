"""Día 8: ajuste de CANAL para el catálogo BB (inmobiliarias + psicólogos).

El VEREDICTO v3 dijo NO porque Etsy en español casi no tiene compradores de
plantillas sectoriales. Aquí se prueban dos canales alternativos y sus mezclas:

  · Hotmart (marketplace hispano de infoproductos, con afiliados).
    Tarifa 9,9 % + 1,00 € fijo desde el 21-sep-2026 [S]. Requiere titular 18+ [S].
    Visitas desde su marketplace/afiliados para un producto nuevo y sin reseñas:
    5–300/mes en madurez [E muy incierto: no hay datos públicos de tráfico orgánico].
    Fracción de ventas hechas por afiliados (pagan 50 % de comisión): 0–40 % [E].
  · Etsy en INGLÉS: traducir el pack de inmobiliarias ("real estate Canva templates").
    Señal: una tienda nueva de 2026 para agentes inmobiliarios muestra 24 ventas en
    3 meses (≈ 8/mes) [S, un solo caso, sesgo del superviviente]. Con conversión 1–3 %
    eso son ≈ 270–800 visitas/mes; por el sesgo se usa 30–1.500 (mediana ≈ 210) [E].
    Sin SEO propio ni redes (el dueño publica en español).

Cada canal extra se modela como una "pieza" más del catálogo: el mismo producto,
con su tráfico web (SEO/redes) a ~0 para no contarlo dos veces.
Cota correlacionada (la de referencia): los parámetros con el mismo nombre
(`etsy_max`, `p_etsy`, …) comparten cuantil entre piezas, aunque sean canales
distintos → si un marketplace va mal, los otros también (conservador).

Uso: python3 dia8.py [n_corridas] [semilla]
"""
import copy
import json
import sys
from pathlib import Path

import simulador as S
import ajustes as A
import dia7 as D7

ETSY_ES = (10, 400)                 # v3 (Día 7)
HOTMART = {"etsy_max": ("log", 5, 300), "f_afil": ("uni", 0.0, 0.4)}
ETSY_EN = {"etsy_max": ("log", 30, 1500), "p_etsy": ("log", 0.005, 0.03)}
ETSY_EN_ESTRES = ("log", 10, 500)   # por si el caso de 24 ventas/3 meses es excepcional
CASI_CERO = 1e-6


def pieza(f_trafico, canal, solo_canal):
    """Pieza del catálogo (B 17/29 €) en un canal: 'etsy_es', 'hotmart' o 'etsy_en'."""
    c = A.pieza(D7.con_etsy(A.VARIANTES["B_niv"], ETSY_ES), f_trafico)
    p = c["params"]
    if canal == "hotmart":
        c["mkt"] = "hotmart"
        t, a, b = HOTMART["etsy_max"]
        p["etsy_max"] = (t, a * f_trafico, b * f_trafico)
        p["f_afil"] = HOTMART["f_afil"]
    elif canal.startswith("etsy_en"):
        t, a, b = ETSY_EN_ESTRES if canal.endswith("estres") else ETSY_EN["etsy_max"]
        p["etsy_max"] = (t, a * f_trafico, b * f_trafico)
        p["p_etsy"] = ETSY_EN["p_etsy"]
    if solo_canal:                  # el tráfico web ya lo cuenta la pieza principal
        for k in ("seo_max", "red_base"):
            t, a, b = p[k]
            p[k] = (t, a * CASI_CERO, b * CASI_CERO)
    return c


# (f_trafico, canal, solo_canal): 1.0 = inmobiliarias, 0.5 = psicólogos
COMBOS = {
    "BB_etsyES": ("Referencia v3: BB con Etsy-ES",
                  [(1.0, "etsy_es", False), (0.5, "etsy_es", False)]),
    "BB_hotmart": ("BB con Hotmart en lugar de Etsy-ES",
                   [(1.0, "hotmart", False), (0.5, "hotmart", False)]),
    "BB_etsyES+HM": ("BB con Etsy-ES y además Hotmart",
                     [(1.0, "etsy_es", False), (0.5, "etsy_es", False),
                      (1.0, "hotmart", True), (0.5, "hotmart", True)]),
    "BB+EN": ("BB Etsy-ES + inmobiliarias traducido en Etsy-EN",
              [(1.0, "etsy_es", False), (0.5, "etsy_es", False), (1.0, "etsy_en", True)]),
    "BB_HM+EN": ("BB Hotmart + inmobiliarias en Etsy-EN",
                 [(1.0, "hotmart", False), (0.5, "hotmart", False), (1.0, "etsy_en", True)]),
    "BB_todo": ("BB Etsy-ES + Hotmart + inmobiliarias en Etsy-EN",
                [(1.0, "etsy_es", False), (0.5, "etsy_es", False),
                 (1.0, "hotmart", True), (0.5, "hotmart", True), (1.0, "etsy_en", True)]),
    "BB+EN_estres": ("Prueba de estrés: BB+EN con Etsy-EN 10–500 visitas/mes",
                     [(1.0, "etsy_es", False), (0.5, "etsy_es", False), (1.0, "etsy_en_estres", True)]),
    "B_EN_solo": ("Solo inmobiliarias en Etsy-EN (sin web en español)",
                  [(1.0, "etsy_en", True)]),
}


def registrar(nombre, piezas):
    kcs = []
    for i, (f, canal, solo) in enumerate(piezas):
        kc = f"D8_{nombre}_{i}"
        D7.registrar(kc, pieza(f, canal, solo))
        kcs.append(kc)
    return kcs


def escenarios(kcs):
    out = []
    for q in (0.1, 0.5, 0.9):
        tot = S.COSTE_FIJO
        for kc in kcs:
            tot += S.simular(kc, S.valores_en(kc, q), 6)[0]
        out.append(tot)
    return out


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    semilla = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    out = Path(__file__).parent / "resultados"
    res = {}
    md = ["# Día 8 — ajuste de canal del catálogo BB", "",
          f"Monte Carlo: {n} corridas, semilla {semilla}, lanzamiento jun-2027, 12 meses, cota correlacionada.",
          "**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.** Supuestos: cabecera de `dia8.py`"
          " y `../investigacion/10_CANALES_HOTMART_ETSY_EN.md`.", "",
          "| Combinación | Pesimista | Base | Optimista | MC mediana | MC p10–p90 | P(0 ventas) | **P(≥ 500 €)** |",
          "|---|---|---|---|---|---|---|---|"]
    kcs_por = {}
    for k, (nombre, piezas) in COMBOS.items():
        kcs = registrar(k, piezas)
        kcs_por[k] = kcs
        r = A.resumir(*A.mc_catalogo(kcs, n, semilla, True))
        r["pesimista"], r["base"], r["optimista"] = escenarios(kcs)
        r["nombre"] = nombre
        res[k] = r
        md.append(f"| `{k}` {nombre} | {r['pesimista']:.0f} € | {r['base']:.0f} € | {r['optimista']:.0f} € | "
                  f"{r['mediana']:.0f} € | {r['p10']:.0f}–{r['p90']:.0f} € | {r['prob_0_ventas']:.1%} | "
                  f"**{r['prob_500']:.1%}** |")

    # Tornado de la mejor combinación
    mejor = max((k for k in res if k not in ("B_EN_solo", "BB+EN_estres")), key=lambda k: res[k]["prob_500"])
    base, filas = D7.tornado_catalogo(kcs_por[mejor])
    S.svg_tornado(base, filas, f"{mejor}: p10 ↔ p90 en todas las piezas", out / "tornado_dia8.svg")
    res["tornado"] = {"combo": mejor, "base": base,
                      "filas": [{"param": p, "neto_p10": a, "neto_p90": b} for p, a, b, _ in filas]}
    md += ["", f"## Tornado de la mejor combinación (`{mejor}`)", "",
           f"Caso base determinista: **{base:.0f} €**.", "",
           "| Parámetro | Neto con p10 | Neto con p90 | Amplitud |", "|---|---|---|---|"]
    md += [f"| `{p}` | {a:.0f} € | {b:.0f} € | {d:.0f} € |" for p, a, b, d in filas]
    md += ["", "Gráfica: `tornado_dia8.svg`.",
           "", "Nota: el modelo NO cuenta el trabajo extra de cada canal (traducir, subir a Hotmart, mantener 2–3 tiendas)."]
    (out / "dia8.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (out / "dia8.json").write_text(json.dumps({"n": n, "semilla": semilla, "resultados": res},
                                              indent=1, ensure_ascii=False), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
