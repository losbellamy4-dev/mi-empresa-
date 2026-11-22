# 15 — Qué da impresiones a un anuncio NUEVO de Etsy, y la brecha de valor (Día 13, 2026-11-21)

[S] = dato con fuente · [S débil] = fuente de terceros sin metodología · [E] = estimación propia.

## 1. Cómo decide Etsy si enseña un anuncio nuevo
| Hecho | Fiabilidad | Fuente |
|---|---|---|
| Cada anuncio nuevo recibe un **empujón pequeño y temporal** en la búsqueda para que Etsy aprenda cómo reaccionan los compradores. | [S] | Etsy Seller Handbook, art. 366469719354 (ago-2025), citado en [printful.com/blog/etsy-seo](https://printful.com/blog/etsy-seo) y [gelato.com](https://www.gelato.com/ca/blog/etsy-seo-tips) (la página de Etsy devuelve 403 al robot) |
| La duración del empujón **no es oficial**: "de unas horas a unos días" (eRank); una guía de 2026 dice 14–21 días (fuente única, no verificada). | [S débil] | [help.erank.com](https://help.erank.com/blog/7-factors-that-affect-rank-on-etsy/), [sellertoolshq.com](https://sellertoolshq.com/guides/etsy-algorithm-2026/) |
| Pasado el empujón, el puesto depende del **Listing Quality Score**: lo que hace el comprador tras hacer clic (tiempo, favoritos, compra). Las tiendas y anuncios nuevos empiezan con una tasa de interacción neutra. | [S] | eRank; podcast de Etsy ([transcripción](https://www.etsy.com/uk/seller-handbook/article/podcast-transcript-etsy-search/397558006917)) |
| Renovar anuncios para volver a tener el empujón **no compensa** según el propio equipo de búsqueda de Etsy. | [S] | podcast de Etsy |
| Otros factores: relevancia de título/etiquetas/atributos; puntuación de experiencia de la tienda (políticas completas, sección "Acerca de", sin reseñas de 1★ ni reclamaciones de copyright); idioma de la cuenta (traducción manual mejor que la automática); personalización. | [S] | eRank |
| Tiempo hasta la primera venta en una tienda nueva: típico 1–3 semanas, con casos de 3–6 meses. **No hay estadísticas fiables** de visitas por anuncio antes de la primera venta. | [S débil] (blogs y foros) | foros de community.etsy.com |

**Traducción al modelo:** un anuncio nuevo tiene **una sola oportunidad corta** de demostrar CTR y conversión. Si en ese empujón nadie hace clic o nadie compra, el anuncio se hunde y el canal queda "muerto" en la práctica. Por eso `p_muerto` de Etsy-EN depende sobre todo de **lo atractiva que sea la oferta comparada con la de al lado**, no del SEO.

## 2. La competencia en "real estate instagram template(s)"
| Hecho | Fiabilidad | Fuente |
|---|---|---|
| ≈ 8.600 anuncios compiten por "real estate instagram template"; volumen de esa frase exacta ≈ 40–70 búsquedas/mes en Etsy. | [S débil] (RankHero, cifras internamente incoherentes) | [rankhero.com](https://www.rankhero.com/keywords/real-estate-instagram-template) |
| Packs grandes: 345+ posts y stories por 47 $; 200 posts y stories; 50 plantillas; "1000+" por 21 $; packs mensuales por 18 $. Precios de packs: **9–47 $**, a menudo con "descuento" permanente. | [S] (fichas de Etsy en buscador) | p. ej. [etsy.com/listing/1228556772](https://www.etsy.com/listing/1228556772/50-real-estate-templates-instagram-real), [etsy.com/listing/1734445087](https://www.etsy.com/listing/1734445087/real-estate-instagram-posts-carousels), [etsy.com/listing/4530399257](https://www.etsy.com/listing/4530399257/july-2026-real-estate-social-media-canva) |
| Tiendas establecidas con 1.878 y 4.798 ventas; una tienda abierta en 2026 con 24 ventas. | [S] | resultados de búsqueda de tiendas de Etsy |
| Los rivales se diferencian por **estrategia de contenido** ("con la estrategia incluida") y por "funciona con Canva gratis". | [S] | stan.store, fichas de Etsy |

## 3. El problema: brecha de valor
| Oferta | Diseños | Precio | Diseños por dólar |
|---|---|---|---|
| Nuestro anuncio ancla #1 (Just Listed) | 4 (× 3 paletas) | 9 $ | 0,4 (1,3 contando paletas) |
| Nuestro bundle de prueba #5 | 16 + 2 carruseles | 24 $ | ≈ 0,75 |
| Pack típico de la competencia | 50–345 | 15–47 $ | **≈ 3–7** |

En la página de resultados el comprador ve nuestra portada al lado de "345+ templates". Con 10–100× menos diseños por dólar, es razonable esperar **menos clics y menos compras durante el empujón** → Listing Quality Score bajo → canal muerto. [E]

## 4. Cuánto pesa (simulador `dia13.py` → `simulador/resultados/dia13.md`)
| Escenario [E] | p_muerto EN | conversión EN | P(≥ 500 €) | Mediana |
|---|---|---|---|---|
| Oferta actual (brecha sin corregir) | 0,60 | ×0,5 | **28,5 %** | 187 € |
| Supuesto v5 (Día 10) | 0,40 | ×1,0 | 41,3 % | 348 € |
| Oferta grande (ancla = pack de ~38 diseños × 3 paletas) | 0,35 | ×0,9 | **43,0 %** | 369 € |

Corregir la brecha vale **≈ +15 puntos** de probabilidad. Es la mayor palanca encontrada hasta ahora que depende solo de nosotros y no cuesta dinero. Ojo: el supuesto v5 de 0,40 probablemente era **optimista para la oferta actual**; el veredicto real con los 5 anuncios tal cual estarían más cerca del 28–34 %.

## 5. Decisión y cambio de plan (pendiente de la elección de idea)
1. **No competir en cantidad bruta** (no se pueden hacer 345 diseños a mano), sino **cerrar la brecha lo bastante**: el anuncio ancla pasa a ser el **pack base completo** (las 10 plantillas, ≈ 38 diseños × 3 paletas × ES/EN, ya especificado en `12_ESPEC_PACK_INMOBILIARIAS.md`) a **19–24 $**, en la banda de precio de los rivales.
2. Anuncios sueltos (Just Listed, Open House…) **a 4–6 $** como puerta de entrada y para cubrir palabras clave de cola larga ("just listed template", "open house flyer instagram"), cada uno enlazando al pack.
3. Diferenciación honesta en portada y título: **"strategy included"** (calendario de 30 días de publicaciones con qué plantilla usar cada día) + "works with free Canva" + versión en español (casi nadie la ofrece en el mercado EN de EE. UU., con ≈ 40 M de hispanohablantes) [E].
4. Consecuencia para la Fase 3: la prueba de Etsy-EN necesita el **pack completo antes** de publicar, no solo 4 diseños. Más trabajo previo (≈ 10–15 h de Canva para Adrián [E]), pero publicar la oferta débil arriesga quemar el empujón de los anuncios.

## Lo que sigue sin saberse
- El volumen real de búsqueda en Etsy (eRank gratis, 🔴 lo puede mirar un adulto) y la conversión real de una tienda nueva: **solo la prueba lo mide**.
