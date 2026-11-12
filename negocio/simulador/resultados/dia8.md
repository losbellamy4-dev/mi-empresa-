# Día 8 — ajuste de canal del catálogo BB

Monte Carlo: 20000 corridas, semilla 42, lanzamiento jun-2027, 12 meses, cota correlacionada.
**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.** Supuestos: cabecera de `dia8.py` y `../investigacion/10_CANALES_HOTMART_ETSY_EN.md`.

| Combinación | Pesimista | Base | Optimista | MC mediana | MC p10–p90 | P(0 ventas) | **P(≥ 500 €)** |
|---|---|---|---|---|---|---|---|
| `BB_etsyES` Referencia v3: BB con Etsy-ES | 7 € | 275 € | 3893 € | 408 € | 103–1482 € | 0.1% | **41.6%** |
| `BB_hotmart` BB con Hotmart en lugar de Etsy-ES | -0 € | 196 € | 3099 € | 301 € | 68–1155 € | 0.3% | **31.8%** |
| `BB_etsyES+HM` BB con Etsy-ES y además Hotmart | -14 € | 343 € | 5015 € | 494 € | 106–2030 € | 0.1% | **49.6%** |
| `BB+EN` BB Etsy-ES + inmobiliarias traducido en Etsy-EN | 24 € | 603 € | 7554 € | 789 € | 195–3247 € | 0.0% | **66.5%** |
| `BB_HM+EN` BB Hotmart + inmobiliarias en Etsy-EN | 16 € | 524 € | 6760 € | 698 € | 164–2886 € | 0.0% | **62.3%** |
| `BB_todo` BB Etsy-ES + Hotmart + inmobiliarias en Etsy-EN | 2 € | 671 € | 8677 € | 850 € | 182–3680 € | 0.0% | **67.5%** |
| `BB+EN_estres` Prueba de estrés: BB+EN con Etsy-EN 10–500 visitas/mes | 3 € | 375 € | 5103 € | 529 € | 126–2054 € | 0.1% | **52.3%** |
| `B_EN_solo` Solo inmobiliarias en Etsy-EN (sin web en español) | 32 € | 343 € | 3676 € | 339 € | 55–1821 € | 1.1% | **38.7%** |

## Tornado de la mejor combinación (`BB_todo`)

Caso base determinista: **671 €**.

| Parámetro | Neto con p10 | Neto con p90 | Amplitud |
|---|---|---|---|
| `etsy_max` | 190 € | 2853 € | 2663 € |
| `p_etsy` | 346 € | 1360 € | 1014 € |
| `seo_max` | 600 € | 971 € | 372 € |
| `p_directa` | 604 € | 836 € | 232 € |
| `tau_etsy` | 606 € | 737 € | 131 € |
| `red_base` | 655 € | 758 € | 103 € |
| `f_premium` | 633 € | 708 € | 75 € |
| `tau_seo` | 651 € | 703 € | 51 € |
| `retraso_seo` | 648 € | 696 € | 48 € |

Gráfica: `tornado_dia8.svg`.

Nota: el modelo NO cuenta el trabajo extra de cada canal (traducir, subir a Hotmart, mantener 2–3 tiendas).
