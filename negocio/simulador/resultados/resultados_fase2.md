# Resultados del simulador de Fase 2 (v1)

Monte Carlo: 20000 corridas por idea y lanzamiento, semilla 42, 12 meses desde el lanzamiento.
**Son estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.** Ecuaciones: `../../modelo/modelo.md`.

## Resumen

| Idea | Neto/venta web | Pesimista | Base | Optimista | MC mediana | MC p10–p90 | P(≥ 500 €) jun-27 | P(≥ 500 €) feb-27 |
|---|---|---|---|---|---|---|---|---|
| A Opositores (planificador + generador gratis) | 11.12 € | -1 € | 151 € | 2882 € | 224 € | 48–849 € | **22.2%** | 22.3% |
| B Inmobiliarias (plantillas Canva) | 12.64 € | 9 € | 262 € | 3301 € | 368 € | 91–1400 € | **38.6%** | 37.9% |
| C Estudiantes ESO/Bach (planner + generador) | 5.03 € | -7 € | 79 € | 1563 € | 123 € | 24–462 € | **8.7%** | 8.8% |

## A. Opositores (planificador + generador gratis)

- Escenario base: 2814 visitas y 16.2 ventas en 12 meses → 151 € netos.
- Optimista: 17845 visitas, 276.1 ventas → 2882 €.
- Monte Carlo (jun-27): media 385 €, mediana de ventas 23, P(0 ventas en 12 meses) = 0.3%.
- Sensibilidad (tornado, de mayor a menor efecto): `etsy_max` 71↔463 €, `seo_max` 114↔320 €, `p_etsy` 97↔259 €, `p_compra` 116↔237 €.
- Correlación de rangos con el neto (Monte Carlo): `etsy_max` +0.59, `seo_max` +0.37, `p_etsy` +0.30, `p_compra` +0.29, `p_uso` +0.22, `red_base` +0.13, `retraso_seo` -0.06, `tau_etsy` -0.05, `tau_seo` -0.05.
- Gráficas: `hist_A.svg`, `tornado_A.svg`.

## B. Inmobiliarias (plantillas Canva)

- Escenario base: 1903 visitas y 24.0 ventas en 12 meses → 262 € netos.
- Optimista: 10065 visitas, 285.2 ventas → 3301 €.
- Monte Carlo (jun-27): media 644 €, mediana de ventas 33, P(0 ventas en 12 meses) = 0.1%.
- Sensibilidad (tornado, de mayor a menor efecto): `etsy_max` 106↔922 €, `p_etsy` 148↔519 €, `seo_max` 221↔437 €, `p_directa` 220↔367 €.
- Correlación de rangos con el neto (Monte Carlo): `etsy_max` +0.69, `p_etsy` +0.38, `seo_max` +0.29, `p_directa` +0.26, `red_base` +0.13, `retraso_seo` -0.07, `tau_etsy` -0.05, `tau_seo` -0.05.
- Gráficas: `hist_B.svg`, `tornado_B.svg`.

## C. Estudiantes ESO/Bach (planner + generador)

- Escenario base: 5445 visitas y 20.7 ventas en 12 meses → 79 € netos.
- Optimista: 36518 visitas, 335.2 ventas → 1563 €.
- Monte Carlo (jun-27): media 211 €, mediana de ventas 30, P(0 ventas en 12 meses) = 0.1%.
- Sensibilidad (tornado, de mayor a menor efecto): `etsy_max` 34↔246 €, `seo_max` 61↔165 €, `p_etsy` 48↔140 €, `p_compra` 59↔127 €.
- Correlación de rangos con el neto (Monte Carlo): `etsy_max` +0.58, `seo_max` +0.34, `p_etsy` +0.30, `p_compra` +0.30, `red_base` +0.21, `p_uso` +0.20, `tau_seo` -0.06, `retraso_seo` -0.05, `tau_etsy` -0.04.
- Gráficas: `hist_C.svg`, `tornado_C.svg`.
