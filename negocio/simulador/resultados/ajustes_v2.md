# Ajustes de idea — resultados del simulador (v2, Día 6)

Monte Carlo: 20000 corridas por variante, semilla 42, lanzamiento jun-2027, 12 meses.
**Estimaciones del modelo bajo supuestos [E] conservadores, NO garantías.** Supuestos nuevos: `../../modelo/modelo.md` §7.

| Variante | Pesimista | Base | Optimista | MC mediana | MC p10–p90 | P(0 ventas) | **P(≥ 500 €)** |
|---|---|---|---|---|---|---|---|
| `A_v1` A tal cual (v1) | -1 € | 151 € | 2882 € | 224 € | 48–849 € | 0.3% | **22.2%** |
| `A_21` A con pack a 21 € | -5 € | 127 € | 2813 € | 192 € | 41–729 € | 0.9% | **17.9%** |
| `A_niv` A 15 € + premium 24 € (2 oposiciones + plantillas extra) | -0 € | 172 € | 3385 € | 255 € | 56–949 € | 0.3% | **25.1%** |
| `B_v1` B tal cual (v1) | 9 € | 262 € | 3301 € | 368 € | 91–1400 € | 0.1% | **38.6%** |
| `B_29` B con pack a 29 € | 0 € | 201 € | 3175 € | 278 € | 64–1128 € | 0.9% | **28.8%** |
| `B_niv` B 17 € + pack agencia 29 € | 11 € | 303 € | 3980 € | 418 € | 103–1612 € | 0.1% | **43.0%** |
| `B_esc` B con escalera en Etsy (4 € → pack 17 €) | -3 € | 175 € | 3050 € | 261 € | 61–979 € | 0.0% | **26.6%** |
| `B_niv_esc` B 17 €/29 € + escalera en Etsy | -3 € | 189 € | 3417 € | 288 € | 68–1040 € | 0.0% | **29.5%** |
| `AB_ind` Catálogo A (15/24 €) + B (17/29 €), indep. | 25 € | 473 € | 7067 € | 786 € | 290–2263 € | 0.0% | **71.7%** |
| `AB_cor` Catálogo A (15/24 €) + B (17/29 €), correl. | 25 € | 473 € | 7067 € | 666 € | 189–2458 € | 0.0% | **61.5%** |
| `BB_ind` Catálogo B en dos sectores (17/29 €; 2.º sector con mitad de tráfico), indep. | 23 € | 452 € | 5840 € | 734 € | 266–2195 € | 0.0% | **68.9%** |
| `BB_cor` Catálogo B en dos sectores (17/29 €; 2.º sector con mitad de tráfico), correl. | 23 € | 452 € | 5840 € | 615 € | 163–2348 € | 0.0% | **58.4%** |
