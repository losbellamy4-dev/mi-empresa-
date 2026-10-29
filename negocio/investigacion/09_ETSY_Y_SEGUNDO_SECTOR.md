# Etsy en español y elección del 2.º sector de B (Día 7, 2026-10-29)

Leyenda: [S] dato con fuente · [E] estimación propia · [M] mixto.

## 1. ¿Cuántas visitas puede dar Etsy a B? (`etsy_max`)

**Intento directo fallido.** Etsy devuelve 403 al fetch y un captcha al navegador sin cabeza, así que no se pudieron contar anuncios ni reseñas de "plantillas canva inmobiliaria". Para medirlo de verdad hace falta una cuenta de vendedor (Etsy Search Analytics) o eRank: 🔴 humano, opcional y gratis (ver más abajo).

**Señales indirectas**
- En las búsquedas web en español ("plantillas inmobiliaria Canva", "plantillas canva psicólogos", "plantillas estética Canva") **no sale ni un anuncio de Etsy**. Los resultados son de Canva (gratis), Hotmart y Gumroad [S]:
  - Hotmart: "Anuncios 10X" (58 anuncios inmobiliarios) y "Sistema generador de clientes para Realtors" (más de 300 diseños) [S] ([1](https://hotmart.com/es/marketplace/productos/anuncios-10x-pack-optimizar/C102919052W), [2](https://hotmart.com/es/marketplace/productos/plantillas-real-estate-para-redes-sociales-300/C104483085I)).
  - Gumroad: packs inmobiliarios de 7–12 $ y de 21 plantillas [S] ([3](https://productosdigitalesar.gumroad.com/l/yqxpin)).
- En inglés, Etsy sí tiene un mercado grande y muy saturado: hay anuncios de plantillas inmobiliarias con más de 3.300 reseñas y precios de 2–22 $ [S] ([4](https://www.etsy.com/market/real_estate_templates)). En español, ese mercado no se ve.
- Hay cifras de ingresos de vendedores (de 100 a 800 $/mes "en el centro") y "50 ventas/mes en un nicho medio", pero son blogs o ejemplos hipotéticos [S, débil] ([5](https://wifimoolah.com/p/idea-40), [6](https://www.pocketsflow.com/blog/how-to-sell-canva-templates-on-etsy)). No sirven como dato.

**Conclusión [E]:** el rango v2 (20–800 visitas/mes en madurez) es **optimista para el comprador hispanohablante**. Paso a un rango conservador **v3 = 10–400** y mantengo una prueba de estrés de 5–200. En este modelo, el canal de venta en español con más señales es **Hotmart/Gumroad + web propia**, no Etsy.

## 2. Elección del 2.º sector

Criterios: tamaño del público en España, señales de búsqueda (autocompletado de Google, `datos/autocompletado_2026-10-29*.json`), competencia en español, disposición a pagar y riesgo F8.

| Sector | Tamaño en España | Autocompletado ("plantillas para…", "post para…") | Competencia en español | Riesgo | Nota [E] |
|---|---|---|---|---|---|
| **Psicólogos** | **47.396** colegiados de la rama sanitaria en 2025 (+8,6 %) [S] ([INE vía Infocop](https://www.infocop.es/estadistica-colegiados-de-la-rama-sanitaria/)); 82 % mujeres; muchos autónomos con consulta propia | **10/10** sugerencias, incluidas "plantillas canva para psicologos" y "plantillas notion para psicologos" | Poca: un pack de Gumroad a 29,99 $ (21 posts + 10 destacadas) [S] ([7](https://carlajayaro.gumroad.com/l/zbbwb)) y un pack de 200 en Etsy (en inglés) | Medio: los textos de ejemplo no pueden hacer afirmaciones clínicas. Las plantillas llevan solo diseño y huecos de texto, con ideas genéricas no clínicas | **4,1** |
| Centros de estética / peluquerías | ≈ 72.300 locales (22.300 de estética) en 2021 [S] ([DBK vía Forbes](https://forbes.es/ultima-hora/230563/las-ventas-de-peluqueria-y-centros-de-estetica-se-elevan-un-11-en-2022-y-superan-las-cifras-de-prepandemia/)) | Estética 6/10 ("promociones", "editables", "publicidad") y peluquería 3/10 | **Muy alta y barata** en Hotmart: packs de más de 350 plantillas, 13 €, y varios packs de 1–12 $ en Gumroad [S] ([8](https://hotmart.com/es/marketplace/productos/plantillas-para-estetica-de-belleza/M89056354F)) | La medicina estética tiene normas de publicidad sanitaria: habría que evitarla | 3,2 |
| Fisioterapia | Sin cifra verificada hoy | "post para fisioterapia" 5/10 (temas, ideas, Instagram) | Sin medir | Medio (sanitario) | 3,3 (reserva) |
| Restaurantes | Muy grande | 10/10, pero casi todo "gratis", "excel", "wordpress" y "menú" | Canva gratis domina | Es otro producto (cartas o menús) | 2,5 |
| Inmobiliarias (1.º sector, referencia) | 60.683 empresas y más de 69.000 locales (ene-2025) [S] ([DBK vía idealista](https://www.idealista.com/news/node/900100)) | 10/10 | Media (Hotmart y Gumroad) | Bajo | — |

**Decisión [E]: el 2.º sector de B es "psicólogos"**, con fisioterapia en reserva. El público es más pequeño que el de estética, pero busca plantillas de Canva de forma explícita, tiene poca competencia en español y acepta precios de unos 30 $. Esto encaja con el nivel premium de 29 €. Como el "pack para consultas sanitarias" sirve también para fisioterapeutas y nutricionistas, se puede ampliar después con poco trabajo.

## 3. 🔴 Opcional (gratis, requiere adulto)
Abrir una cuenta de vendedor de Etsy o una cuenta gratuita de eRank para ver el volumen real de búsqueda en Etsy de "plantillas inmobiliaria" y "plantillas psicologos". Es la medida que más reduciría la incertidumbre del modelo (ver tornado del Día 7). No es necesario para seguir.
