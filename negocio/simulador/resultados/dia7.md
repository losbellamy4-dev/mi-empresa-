# Día 7 — `etsy_max` de B y tornado del catálogo BB

Monte Carlo: 20000 corridas, semilla 42, lanzamiento jun-2027, 12 meses.
**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.**

## 1. Sensibilidad al rango de visitas en Etsy

| Rango `etsy_max` (visitas/mes) | Variante | Base | MC mediana | MC p10–p90 | **P(≥ 500 €)** |
|---|---|---|---|---|---|
| v2 20–800 | B 17/29 € (un sector) | 303 € | 418 € | 103–1612 € | **43.0%** |
| v2 20–800 | BB inmobiliarias + psicólogos, correl. | 452 € | 615 € | 163–2348 € | **58.4%** |
| v3 10–400 | B 17/29 € (un sector) | 185 € | 276 € | 64–998 € | **28.0%** |
| v3 10–400 | BB inmobiliarias + psicólogos, correl. | 275 € | 408 € | 103–1482 € | **41.6%** |
| estres 5–200 | B 17/29 € (un sector) | 126 € | 196 € | 39–736 € | **18.0%** |
| estres 5–200 | BB inmobiliarias + psicólogos, correl. | 187 € | 284 € | 66–1050 € | **28.8%** |

## 2. Tornado del catálogo BB (rango Etsy v3, cota correlacionada)

Caso base determinista: **275 €**. Cada fila mueve un parámetro de p10 a p90 en los dos productos a la vez.

| Parámetro | Neto con p10 | Neto con p90 | Amplitud |
|---|---|---|---|
| `etsy_max` | 141 € | 843 € | 702 € |
| `seo_max` | 204 € | 576 € | 372 € |
| `p_etsy` | 177 € | 496 € | 319 € |
| `p_directa` | 208 € | 440 € | 232 € |
| `red_base` | 259 € | 362 € | 103 € |
| `tau_seo` | 256 € | 307 € | 51 € |
| `retraso_seo` | 253 € | 300 € | 48 € |
| `tau_etsy` | 257 € | 294 € | 37 € |
| `f_premium` | 261 € | 290 € | 30 € |

Gráfica: `tornado_BB.svg`.
