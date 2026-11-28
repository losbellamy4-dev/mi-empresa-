# Vista previa de simulación de las finalistas (Día 4)

Monte Carlo con 20000 corridas por idea, horizonte de 12 meses tras lanzar, semilla 42.
**Estimación del modelo con supuestos [E], no una garantía.** El simulador de Fase 2 sustituirá estos rangos por datos investigados.

| Idea | Neto/venta | Pesimista (p5) | Base (mediana) | Optimista (p95) | MC mediana | MC p10–p90 | P(≥ 500 €) |
|---|---|---|---|---|---|---|---|
| A_opositores | 11.12 € | -4 € | 370 € | 13943 € | 363 € | 41–2464 € | **42%** |
| B_inmobiliarias | 12.64 € | -0 € | 293 € | 6479 € | 301 € | 36–1514 € | **35%** |
| C_estudiantes | 5.03 € | -10 € | 153 € | 6298 € | 151 € | 10–1101 € | **23%** |

Parámetros (p5–p95 de lognormales): A_opositores: visitas/mes maduras (80, 4000), conversión (0.002, 0.03), tau (2, 8) meses; B_inmobiliarias: visitas/mes maduras (40, 1500), conversión (0.004, 0.03), tau (1, 6) meses; C_estudiantes: visitas/mes maduras (150, 8000), conversión (0.001, 0.015), tau (2, 8) meses

## Lectura honesta
- **Con estos supuestos, ninguna finalista tiene la mediana por encima de 500 €.** La probabilidad estimada va del 23 % (C) al 42 % (A). Es decir: lo más probable, sin hacer nada especial, es quedarse por debajo.
- El "optimista (p95)" pone todos los parámetros en su p95 a la vez. Es poco realista; mira mejor el rango p10–p90 del Monte Carlo.
- La variable que más pesa es el **tráfico mensual maduro** (cubre dos órdenes de magnitud). La Fase 2 tiene que acotarla con datos de SEO/canal y medir la sensibilidad formalmente.
- El orden A > B > C coincide con la puntuación cualitativa de `investigacion/FINALISTAS.md`.
