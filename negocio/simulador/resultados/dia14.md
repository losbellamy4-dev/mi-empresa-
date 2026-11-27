# Día 14 — punto de control: oferta v2 de Etsy-EN (ancla 22 $ + sueltos 4–6 $)

Monte Carlo: 8000 corridas, semilla 42, catálogo `BB+2EN`, escenario base `oferta_grande` (p_muerto Etsy-EN 0.35, conversión ×0.9). Cambio 1 $ = 0.92 €.
**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.**

- Neto por venta de Etsy-EN que suponía el modelo (pack 17 € / 29 €): **13.38 €**.
- Neto del ancla 22 $ (20.24 €): 13.98 € · de un suelto 5 $ (4.60 €): **2.80 €** (las comisiones fijas se comen ≈ 26% del precio sin IVA).

| Cuota de sueltos | Caso | Neto/venta Etsy-EN | **P(≥ 500 €)** | P(0 ventas) | Mediana |
|---|---|---|---|---|---|
| — | referencia Día 13 | 13.38 € | **43.0%** | 7.0% | 369 € |
| 30% | canibal | 11.50 € | **40.8%** | 7.0% | 339 € |
| 30% | aditivo | 11.50 € | **46.6%** | 6.7% | 435 € |
| 45% | canibal | 9.64 € | **38.0%** | 7.0% | 310 € |
| 45% | aditivo | 9.64 € | **47.5%** | 7.1% | 450 € |
| 60% | canibal | 7.77 € | **34.8%** | 7.0% | 276 € |
| 60% | aditivo | 7.77 € | **48.2%** | 7.8% | 468 € |

- Rango de la oferta v2: **34.8% – 48.2%** frente a 43.0% de referencia.
- Lectura: los sueltos a 4–6 $ solo compensan si traen compradores **nuevos** (caso aditivo). Si sustituyen ventas del pack (caníbal), restan. Ver decisión en la BITÁCORA del Día 14.
