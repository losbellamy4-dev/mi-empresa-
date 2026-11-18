# Día 9 — umbral de corte de la validación Etsy-EN (catálogo BB+EN)

Monte Carlo: 20000 corridas por fila, semilla 42, cota correlacionada.
**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.** Método: cabecera de `dia9.py`.

| Techo Etsy-EN V (visitas/mes) | Visitas que se verían en el mes 2 | Base | MC mediana | P(0 ventas) | **P(≥ 500 €)** |
|---|---|---|---|---|---|
| 10 | ≈ 9 | 276 € | 410 € | 0.1% | **42.1%** |
| 20 | ≈ 17 | 293 € | 422 € | 0.0% | **43.1%** |
| 30 | ≈ 26 | 309 € | 441 € | 0.0% | **44.7%** |
| 50 | ≈ 43 | 341 € | 480 € | 0.0% | **48.2%** |
| 75 | ≈ 65 | 381 € | 521 € | 0.0% | **52.0%** |
| 100 | ≈ 86 | 421 € | 564 € | 0.0% | **55.9%** |
| 150 | ≈ 130 | 501 € | 669 € | 0.0% | **65.3%** |
| 200 | ≈ 173 | 582 € | 763 € | 0.0% | **72.6%** |
| 300 | ≈ 259 | 742 € | 925 € | 0.0% | **82.8%** |
| 500 | ≈ 432 | 1064 € | 1284 € | 0.0% | **93.6%** |
| 800 | ≈ 692 | 1546 € | 1755 € | 0.0% | **98.4%** |

- Primer V con P(≥ 500 €) ≥ 50 %: **75** visitas/mes.
- Primer V con caso base ≥ 500 €: **150** visitas/mes.
- Regla derivada: ver `../investigacion/11_PLAN_VALIDACION_ETSY_EN.md`.
