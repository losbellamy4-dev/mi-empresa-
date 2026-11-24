# Día 12 — ¿qué canal muerto pesa más?

Monte Carlo: 20000 corridas por celda, semilla 42. Se varía la probabilidad de canal muerto de **un** canal; el resto queda en su valor base (SEO 0,60 · redes 0,40 · Etsy-ES 0,50 · Etsy-EN 0,40 · Hotmart 0,60).
**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.**

## `BB+2EN` — BB Etsy-ES + inmobiliarias y psicólogos en Etsy-EN

Base: P(≥500) = **42.2%**, mediana 360 €.

| Canal | p_muerto = 0.2 | p_muerto = 0.4 | p_muerto = 0.6 | p_muerto = 0.8 | Pendiente (pp por −0,1) |
|---|---|---|---|---|---|
| seo | 47.8% | 44.6% | 42.2% | 39.8% | **+1.3** |
| red | 42.7% | 42.2% | 42.2% | 41.3% | **+0.2** |
| etsy_es | 46.9% | 43.2% | 40.9% | 38.4% | **+1.4** |
| etsy_en | 51.9% | 42.2% | 33.7% | 25.5% | **+4.4** |

## `BB+EN` — BB Etsy-ES + inmobiliarias traducido en Etsy-EN

Base: P(≥500) = **37.0%**, mediana 300 €.

| Canal | p_muerto = 0.2 | p_muerto = 0.4 | p_muerto = 0.6 | p_muerto = 0.8 | Pendiente (pp por −0,1) |
|---|---|---|---|---|---|
| seo | 43.0% | 40.3% | 37.0% | 34.6% | **+1.4** |
| red | 38.1% | 37.0% | 36.1% | 36.0% | **+0.3** |
| etsy_es | 42.7% | 39.5% | 35.7% | 32.7% | **+1.7** |
| etsy_en | 44.2% | 37.0% | 31.0% | 24.0% | **+3.4** |

## Lectura

- Orden de importancia en `BB+2EN` (más puntos de P(≥500) por cada 0,1 menos de p_muerto): **etsy_en** > **etsy_es** > **seo** > **red**.
