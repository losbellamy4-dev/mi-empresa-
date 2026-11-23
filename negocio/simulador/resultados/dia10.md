# Día 10 — auditoría de P(0 ventas): canales muertos

Monte Carlo: 20000 corridas, semilla 42, lanzamiento jun-2027, 12 meses, cota correlacionada.
**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.** Supuestos: cabecera de `dia10.py`.

## 1. Combinaciones de canal (v4 sin canales muertos → v5 con ellos)

| Combinación | P(≥500) v4 | **P(≥500) v5 base** | P(≥500) v5 estrés | P(0 ventas) v4 → v5 base | Mediana v4 → v5 | Media v5 |
|---|---|---|---|---|---|---|
| `B_solo` Calibración: solo inmobiliarias (web + Etsy-ES) | 26.5% | **10.6%** | 5.9% | 0.4% → 24.2% | 268 → 72 € | 211 € |
| `BB_etsyES` Referencia v3: BB con Etsy-ES | 41.1% | **17.8%** | 9.4% | 0.1% → 19.6% | 396 → 107 € | 323 € |
| `BB+EN` BB Etsy-ES + inmobiliarias traducido en Etsy-EN | 66.0% | **37.0%** | 23.9% | 0.0% → 8.1% | 784 → 300 € | 778 € |
| `BB_todo` BB Etsy-ES + Hotmart + inmobiliarias en Etsy-EN | 68.1% | **39.2%** | 24.7% | 0.0% → 5.2% | 846 → 331 € | 849 € |
| `BB+EN_estres` Prueba de estrés: BB+EN con Etsy-EN 10–500 visitas/mes | 51.2% | **25.6%** | 14.6% | 0.0% → 8.6% | 518 → 190 € | 473 € |
| `B_EN_solo` Solo inmobiliarias en Etsy-EN (sin web en español) | 39.1% | **22.6%** | 15.5% | 1.0% → 41.5% | 344 → 82 € | 482 € |
| `BB+2EN` BB Etsy-ES + inmobiliarias y psicólogos en Etsy-EN | 72.2% | **42.2%** | 27.9% | 0.0% → 8.1% | 946 → 360 € | 1032 € |

## 2. Regla de la prueba Etsy-EN, recalculada

La prueba de 5 anuncios **observa** el tráfico de Etsy-EN, así que en estas filas ese canal está vivo; los demás canales siguen pudiendo morir (probabilidades base).

| Techo Etsy-EN V | Visitas vistas en el mes 2 | P(≥500) v4 (Día 9) | **P(≥500) v5** | P(0 ventas) v5 | Mediana v5 |
|---|---|---|---|---|---|
| 50 | ≈ 43 | 48.2% | **21.3%** | 0.3% | 187 € |
| 75 | ≈ 65 | 52.0% | **24.6%** | 0.1% | 235 € |
| 100 | ≈ 86 | 55.9% | **27.6%** | 0.0% | 286 € |
| 150 | ≈ 130 | 65.3% | **36.8%** | 0.0% | 381 € |
| 200 | ≈ 173 | 72.6% | **46.9%** | 0.0% | 473 € |
| 300 | ≈ 259 | 82.8% | **64.8%** | 0.0% | 648 € |
| 500 | ≈ 432 | 93.6% | **85.6%** | 0.0% | 979 € |

- Primer V con P(≥ 500 €) ≥ 50 % (v5): **300** visitas/mes en madurez (≈ 259 visibles en el mes 2).
