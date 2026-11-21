# Día 13 — brecha de valor en Etsy-EN (catálogo `BB+2EN`)

Monte Carlo: 8000 corridas por celda, semilla 42. Resto de canales muertos en su valor base (SEO 0,60 · redes 0,40 · Etsy-ES 0,50 · Hotmart 0,60).
**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.**

## 1. P(≥ 500 €) según p_muerto de Etsy-EN (filas) y conversión de Etsy-EN (columnas)

| p_muerto Etsy-EN | conv ×0.5 | conv ×0.75 | conv ×1.0 |
|---|---|---|---|
| 0.3 | 35.2% | 41.3% | 46.6% |
| 0.4 | 32.4% | 38.5% | 41.3% |
| 0.5 | 30.6% | 35.0% | 38.2% |
| 0.6 | 28.5% | 31.2% | 34.3% |
| 0.7 | 24.3% | 27.8% | 30.1% |

## 2. Escenarios con nombre

| Escenario | p_muerto EN | conv × | **P(≥500)** | P(0 ventas) | Mediana |
|---|---|---|---|---|---|
| `oferta_actual` | 0.6 | 0.5 | **28.5%** | 12.5% | 187 € |
| `base_v5` | 0.4 | 1.0 | **41.3%** | 8.3% | 348 € |
| `oferta_grande` | 0.35 | 0.9 | **43.0%** | 7.0% | 369 € |

- Corregir la brecha de valor (de `oferta_actual` a `oferta_grande`) vale **+14.5 pp** de P(≥ 500 €).
- Los escenarios con nombre son supuestos [E]; la cifra útil es el **orden de magnitud** del efecto.
