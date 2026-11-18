# 13 — Auditoría: probabilidad de "canal muerto" (Día 10, 2026-11-17)

## Problema
Hasta el Día 9 el simulador daba **P(0 ventas en 12 meses) ≈ 0 %** en todas las combinaciones. Choca con los datos externos:

| Dato | Valor | Fiabilidad |
|---|---|---|
| Productos de Gumroad sin ninguna venta | 44 % | [S] (Día 1, `02_PLATAFORMAS_Y_COSTES.md`) |
| Páginas web con 0 visitas de Google (Ahrefs 2023, ~14.000 M páginas) | **96,55 %**; solo 3,45 % recibe > 10 visitas/mes | [S] [ahrefs.com/blog/search-traffic-study](https://ahrefs.com/blog/search-traffic-study/) — la muestra sesga hacia sitios de mejor calidad; la causa principal es falta de enlaces y de demanda |
| Tiendas de Etsy que nunca venden | ≈ 65 % | [S débil] [sellertoolshq.com](https://sellertoolshq.com/guides/etsy-success-rate/) — sin metodología publicada; incluye tiendas abandonadas |

**Diagnóstico:** el modelo usaba distribuciones lognormales cuyo extremo bajo es "poco tráfico", nunca "cero". En la realidad un canal nuevo es casi **binario**: o arranca o no da nada (Google no posiciona la web, Etsy no enseña los anuncios, las redes no tienen alcance).

## Cambio en el modelo (v5, `simulador/dia10.py`)
En cada corrida de Monte Carlo cada canal puede estar **muerto** (0 visitas los 12 meses). Si está vivo se usa la distribución de siempre. La muerte es común a todas las piezas del catálogo.

| Canal | p_muerto base [E] | estrés [E] | Por qué |
|---|---|---|---|
| SEO (Google) | 0,60 | 0,80 | 96,5 % de páginas a 0; aquí ~10 páginas de cola larga sin enlaces. Se aplica por sitio, no por página, por eso no 0,95. |
| Redes del dueño | 0,40 | 0,60 | Ya existía abandono (6 %/mes); se añade "alcance nulo" de una cuenta nueva. |
| Etsy-ES | 0,50 | 0,70 | 65 % de tiendas sin venta, pero muchas están abandonadas; aquí se publica con cuidado. |
| Etsy-EN | 0,40 | 0,60 | Mercado más grande; hay casos de tiendas nuevas de 2026 que venden. |
| Hotmart | 0,60 | 0,80 | Sin datos de tráfico orgánico; depende de afiliados. |

## Calibración
Un solo producto (inmobiliarias, web + Etsy-ES) da ahora **P(0 ventas) = 24 %** (antes 0,4 %). Sigue por debajo del 44 % de Gumroad, pero es razonable: la mayoría de productos de Gumroad se suben sin ningún canal, y aquí hay dos canales trabajados. **Si acaso, sigue algo optimista.**

## Lección
Una distribución sin masa en el cero infla la probabilidad de éxito cuando el éxito depende de varios canales. A partir de ahora todo canal nuevo del simulador debe llevar su `p_muerto`.
