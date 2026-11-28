# Día 20 — punto de control: oferta de un solo nivel (sin Pack Agencia 29 €)

Monte Carlo: 8000 corridas, semilla 42, catálogo `BB+2EN`, escenario `oferta_grande` (p_muerto Etsy-EN 0.35, conversión Etsy-EN ×0.9; resto de canales muertos en su valor base).
**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.**

| Caso | Descripción | **P(≥ 500 €)** | P(0 ventas) | Mediana | Media |
|---|---|---|---|---|---|
| `ref_dia13` | Referencia Día 13/14: 17/29 € en todos los canales | **43.0%** | 7.0% | 369 € | 1031 € |
| `un_nivel_17` | Un nivel: 17 € web/Etsy-ES, Etsy-EN también 17 € | **39.1%** | 7.1% | 325 € | 874 € |
| `un_nivel_ancla` | Un nivel: 17 € web/Etsy-ES, ancla 22 $ en Etsy-EN | **42.0%** | 7.1% | 362 € | 998 € |
| `ancla+sueltos_canibal` | Igual + 30 % sueltos 5 $ que sustituyen ventas del pack | **37.7%** | 7.1% | 306 € | 818 € |
| `ancla+sueltos_aditivo` | Igual + 30 % sueltos 5 $ como ventas extra | **43.4%** | 6.8% | 380 € | 1092 € |

- Quitar el Pack Agencia y usar el ancla de 22 $ en Etsy-EN mueve P(≥ 500 €) **-1.0 pp** (43.0% → 42.0%).
- Neto por venta: web 17 € → 12.64 € · Etsy 17 € → 11.66 € · Etsy-EN ancla 22 $ → 13.98 € · mezcla ancla+30 % sueltos → 10.62 €.
- La nueva cifra de referencia del proyecto es `un_nivel_ancla` (la oferta que existe hoy de verdad).
