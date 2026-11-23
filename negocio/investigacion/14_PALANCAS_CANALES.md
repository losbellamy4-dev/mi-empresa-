# 14 — ¿Merece la pena trabajar el SEO? Palancas por canal (Día 12, 2026-11-19)

**[V]** fuente oficial · **[S]** secundaria · **[E]** estimación mía.

## Pregunta
La cola del Día 10 pedía "palancas para bajar p_muerto del SEO". Antes de dedicar horas al SEO, medí en el simulador **cuánto vale** bajar el riesgo de cada canal (`simulador/dia12.py` → `resultados/dia12.md`, 20.000 corridas por celda).

## Resultado del simulador (estimaciones, no garantías)
Puntos de P(≥ 500 €) que se ganan por cada 0,1 menos de probabilidad de canal muerto:

| Canal | Catálogo `BB+2EN` | `BB+EN` | Si se baja de su base a 0,2 |
|---|---|---|---|
| **Etsy-EN** | **+4,4 pp** | +3,4 pp | 42 % → **52 %** (desde 0,4) |
| Etsy-ES | +1,4 pp | +1,7 pp | 42 % → 47 % (desde 0,5) |
| SEO (Google) | +1,3 pp | +1,4 pp | 42 % → 48 % (desde 0,6) |
| Redes del dueño | +0,2 pp | +0,3 pp | sin efecto apreciable |

## Qué dicen los datos externos del SEO
- Ahrefs: solo el **5,7 %** de las páginas nuevas llegó al top 10 de Google en un año (estudio de 2017); en la actualización de 2025, **1,74 %** de URLs aleatorias, o **6,11 %** si se filtran páginas en inglés con contenido [S] ([ahrefs.com](https://ahrefs.com/blog/how-long-does-it-take-to-rank/); cifra de 2025 vista en copias traducidas, falta comprobarla en el original).
- Por tanto el `p_muerto` del SEO = 0,60 ya es **generoso**. Bajarlo a 0,2 exigiría enlaces y meses de contenido que un estudiante con 3–5 h/semana no tiene.

## Pinterest
- Solo anécdotas de vendedores, la mayoría con interés comercial: Pinterest como primera fuente social de tráfico hacia tiendas de Etsy de plantillas; "100.000 impresiones en 2 meses sin anuncios" [S débil] ([growingyourcraft](https://www.growingyourcraft.com/blog/marketing-for-digital-product-etsy-shop), [eRank](https://help.erank.com/blog/tips-for-using-pinterest-to-promote-your-etsy-shop), [craftybase](https://craftybase.com/blog/pinterest-for-etsy-seller-handmade)). El dato propio del Día 7 (≈ 0,2 % de clics sobre impresiones) indica poco tráfico real.
- Consejos repetidos: crear pines nuevos en vez de repinear los anuncios (se puede ver como spam), 3–5 pines por producto, enlazar a la sección de la tienda y reclamar la URL de Etsy en Pinterest.

## Decisión [E]
1. **No invertir en SEO más allá de lo básico**: títulos, descripciones y una página por producto en la web, que ya están en el plan. El SEO queda como opción gratuita, no como palanca.
2. **La palanca es Etsy-EN.** Lo que baja su `p_muerto` es la calidad del anuncio: foto de portada, título y etiquetas, número de anuncios y reseñas iniciales. Por eso hoy se han hecho los 5 mockups del anuncio ancla (`producto/mockups/`).
3. **Pinterest se usa para alimentar Etsy-EN** (pines que enlazan a los anuncios), no como canal propio. Encaja en el tiempo de "redes", que según el modelo apenas mueve el resultado por sí solo.
4. Pendiente: buscar datos (no anécdotas) de qué hace que un anuncio nuevo de Etsy consiga impresiones: ranking de "nuevos anuncios", tasa de clics de la portada y número de anuncios en la tienda.
