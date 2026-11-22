# Plan de validación barata de Etsy en inglés (Día 9, 2026-11-16)

> Condición del VEREDICTO v4: el "SÍ" depende de un solo dato de Etsy-EN. Este plan lo comprueba **antes** de construir el catálogo completo.
> Leyenda: [S] fuente secundaria · [E] estimación propia. Umbrales sacados del simulador: `../simulador/resultados/dia9.md`.
> 🔴 Abrir la tienda de Etsy y pagar los anuncios lo hace **un adulto** (titular de la cuenta). Coste total ≈ 1–2 €.

## 1. Qué se publica (prueba mínima)
- **5 anuncios en inglés** del pack de inmobiliarias (lo que haya terminado; ver `12_ESPEC_PACK_INMOBILIARIAS.md`):
  1. "Just Listed" — 10 posts de Instagram (el producto ancla).
  2. "Open House" — 6 posts + 3 stories.
  3. "Just Sold / Under Contract" — 6 posts.
  4. "Real estate tips carousel" — 2 carruseles de 7 diapositivas.
  5. **Bundle** de los 4 anteriores (precio ancla).
- Precios de prueba: 9 $, 9 $, 7 $, 9 $ y bundle 24 $ (dentro del rango observado de 7–17 $ para Canva y 18–35 $ para packs [S], `10_CANALES_HOTMART_ETSY_EN.md`).
- Coste: 5 × 0,20 $ de publicación = **1 $** [S]. Sin Etsy Ads de pago al principio.
- Cada anuncio: título con nicho estrecho ("Just Listed Instagram Post Template for Real Estate Agents | Canva"), 13 etiquetas, 5+ mockups (el comprador no puede previsualizar un archivo de Canva [S]), PDF con enlace de Canva como archivo descargable.

## 2. Qué se mide (Etsy → Shop Manager → Stats, gratis)
| Métrica | Cuándo | Para qué |
|---|---|---|
| Visitas totales de los 5 anuncios | semanas 2, 4, 6 y 8 | Estimar el techo V del modelo |
| Favoritos | mismas fechas | Señal temprana de interés (si hay visitas pero 0 favoritos → fallan mockups o precio) |
| Ventas | mismas fechas | Conversión real (comparar con 0,5–3 % del modelo) |
| Búsquedas que traen visitas | semana 4 | Ajustar títulos y etiquetas |

Anotar los números en `negocio/RESPUESTA_HUMANO.md` (o en `negocio/investigacion/datos/etsy_en_prueba.md`) y la tarea diaria los mete en el simulador.

## 3. Regla de decisión — **v5 (Día 10, `dia10.md`)**; sustituye a la del Día 9
Visitas de los 5 anuncios **en el mes 2** tras publicar (inferencia conservadora: rampa rápida, sin extrapolar por número de anuncios). Desde el Día 10 el modelo admite que SEO, redes y Etsy-ES pueden dar **cero** visitas, así que los umbrales suben:

| Visitas observadas en el mes 2 | Techo V que implica | P(≥ 500 €) BB+EN (v5) | Decisión |
|---|---|---|---|
| **≥ 260** | ≥ 300 | ≈ 65 % | ✅ **Seguir**: construir todo el catálogo (EN + ES + psicólogos EN) |
| 130–259 | 150–299 | 37–64 % | 🟡 **Seguir con ajustes**: añadir los anuncios de psicólogos en EN (sube ≈ +5 puntos), mejorar títulos/mockups; volver a medir en 2 semanas |
| 45–129 | 50–149 | 21–36 % | 🟠 **Repensar**: probar otro sector en inglés o volver a Fase 1 con lo aprendido |
| < 45 | < 50 | ≤ 21 % | ❌ **Etsy-EN no aporta**: VEREDICTO NO; volver a Fase 1 |

(Tabla del Día 9, ya obsoleta: seguir con ≥ 130, ajustar con 65–129.)

Regla secundaria: si hay **≥ 100 visitas y 0 ventas** en 8 semanas, el problema es el anuncio (mockups, precio), no la demanda → arreglar antes de decidir.

Estas probabilidades son **estimaciones del modelo, no garantías**.

## 4. Calendario propuesto [E]
- Semana 0: el adulto abre la tienda (🔴). Adrián sube los 5 anuncios (plantillas, mockups y textos que deja preparados la tarea).
- Semanas 2–8: medir cada 2 semanas.
- Semana 8–9: decisión según la tabla.

Si se lanza en **enero de 2027**, la decisión llega a mediados de marzo, con tiempo para terminar el catálogo antes de la entrega del 15-may-2027.

## 5. Fuentes
- Tiempo hasta la primera venta 1–4 semanas en tiendas bien optimizadas; 10–20 anuncios en los primeros 30 días; 0,20 $ por anuncio y 6,5 % por transacción; las plantillas de Canva necesitan mockups [S, blogs de vendedores, sin datos]: [insightagent](https://www.insightagent.app/guides/start-digital-download-shop-etsy), [listingview](https://listingview.io/blogs/how-to-sell-digital-products-on-etsy-in-2026), [digitalbizplr](https://digitalbizplr.com/blogs/learn/how-to-sell-digital-products-etsy-2026), [growingyourcraft](https://www.growingyourcraft.com/gyc-etsy-academy/roadmap/stage-2).
- No se encontró ningún dato fiable de "visitas necesarias hasta la primera venta": los blogs se contradicen. Por eso la regla usa visitas (dato propio medible) y no fechas.

## 6. Añadido del Día 14 — oferta v2 y métrica de caníbalización
- La prueba se hace con la oferta v2 (`producto/ANUNCIOS_PRUEBA.md`): ancla = pack completo 22 $ + 4 sueltos a 4–6 $. **No publicar el ancla sin los 34 diseños montados.**
- Métrica nueva: **cuota de ventas que son sueltos**. Regla: si en el mes 2 más del 50 % de las ventas son sueltos y hay ≤ 1 venta del pack → retirar los sueltos (o subirlos a 9 $) y dejar el pack solo. Motivo: `simulador/resultados/dia14.md` (caníbal 35–41 % frente a aditivo 47–48 %).
