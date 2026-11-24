# Benchmarks de tráfico y conversión para el simulador (preparación de Fase 2, Día 4)

**[S]** = fuente secundaria (blogs de vendedores o agencias: tomar como orientativo) · **[E]** = estimación mía.

## 1. Conversión en Etsy (relevante para B y, en parte, C)
- Rango típico de una tienda: **1–3 %** de visitas a compra; las que superan ~5 % se consideran top [S] ([Gelato](https://www.gelato.com/blog/etsy-conversion-rate)). Otras fuentes amplían a 1–5 % [S] ([AdNabu](https://blog.adnabu.com/?p=24278)).
- Media general del e-commerce ≈ 2,61 % (Monetate 2019, dato antiguo) [S] ([Alura](https://www.alura.io/blog/how-to-increase-your-conversion-rates-on-etsy.md)).
- No encontré ninguna cifra específica de descargas digitales.

## 2. Embudo gratis → pago (relevante para A y C: generador gratis → pack de pago)
- ChartMogul (SaaS): el 25 % de los productos convierte < 2,5 % de los registros gratis a pago en 6 meses; otro 25 % convierte un 10–15 %; > 15 % es raro [S] ([ChartMogul](https://chartmogul.com/reports/saas-conversion-report/)).
- FirstPageSage vía CrazyEgg: freemium autoservicio 3–5 %; visita → registro gratis 13,3 %; gratis → pago 2,6 % [S, con incoherencias internas en el artículo] ([CrazyEgg](https://www.crazyegg.com/blog/free-to-paid-conversion-rate/)).
- **Implicación [E]:** visita → pago en un embudo de dos etapas ≈ 13 % × 2,6 % ≈ **0,35 %**. En la vista previa supuse para A una mediana de visita → pago de ≈ 0,77 % (rango 0,2–3 %). **El simulador de Fase 2 debe modelar dos etapas** (visita → uso del generador → compra) y probablemente bajar la conversión de A y C.

## 3. Crecimiento del tráfico SEO de un dominio nuevo
- Primeros clics a partir de los **meses 4–6**; crecimiento compuesto en los meses 7–12 [S] ([Stackmatix](https://www.stackmatix.com/blog/seo-timeline-new-startup-domain), [Averi](https://resources.averi.ai/benchmarks/website-traffic-benchmarks-startups)).
- Blogs pequeños (< 10.000 visitas/mes): los que más crecen lo hacen al ~8 % mensual compuesto (Animalz, 2019) [S] ([Animalz](https://www.animalz.co/?p=2468)).
- **Implicación [E]:** la curva `1 - exp(-m/tau)` de la vista previa es demasiado optimista al principio. En Fase 2 hay que usar un **retraso de 3–5 meses** con tráfico SEO casi nulo y canales complementarios (Etsy, Pinterest, TikTok/Shorts del dueño) que no dependan de Google.
- Consecuencia de calendario: si la web se publica en mayo de 2027, el SEO empezaría a dar visitas hacia septiembre-octubre de 2027. **Publicar antes (cuando el producto mínimo esté listo) aumenta la probabilidad** de llegar a 500 € en el horizonte. Lo propondré como decisión del humano cuando toque.

## Pendiente
- Datos de tráfico de Pinterest y de Etsy para recién llegados (impresiones y visitas por anuncio).
- Tasa de clics (CTR) por posición en Google, para pasar de volumen de búsqueda a visitas.
