# VEREDICTO del simulador — v2 (Día 6, 2026-10-27) · PROVISIONAL

> Sigue siendo provisional porque el humano no ha elegido idea. Son **estimaciones del modelo bajo supuestos conservadores, no garantías**.
> Datos: `../simulador/resultados/ajustes_v2.md` (20.000 corridas por variante, semilla 42, lanzamiento en junio de 2027, 12 meses). Supuestos nuevos: `modelo.md` §7.

## Respuesta corta
- **Ningún producto suelto llega a 500 € en el caso base**, aunque se ajuste. El mejor, **B con dos niveles (17 € y "pack agencia" de 29 €)**, se queda en 303 € en el caso base, con **P(≥ 500 €) = 43 %**.
- **Un catálogo de dos productos roza el umbral:** el caso base queda en 452–473 € (todavía por debajo), pero la mediana del Monte Carlo pasa a 615–666 € y **P(≥ 500 €) = 58–62 %** con la cota conservadora (correlacionada).
- **Veredicto v2:** NO en el escenario base estricto; **SÍ por poco** en la mediana del Monte Carlo, y solo con catálogo. Es suficiente para preparar la Fase 3, **con la condición** de diseñar el negocio como catálogo desde el principio y medir pronto el tráfico real de Etsy.

## Qué ajustes funcionan y cuáles no

| Ajuste | Efecto en P(≥ 500 €) | Conclusión |
|---|---|---|
| Subir el precio único (A a 21 €, B a 29 €) | A 22 → 18 % · B 39 → 29 % | ❌ Con elasticidad 1–2, la caída de la conversión se come la subida de precio. **Descartado** (se puede volver a probar con datos reales de una prueba A/B). |
| Nivel premium opcional (A 15/24 €, B 17/29 €) | A 22 → 25 % · B 39 → **43 %** | ✅ Sube el ticket medio sin perder compradores (supuesto: el premium no resta ventas al pack). **Adoptado.** |
| Escalera en Etsy (4 € → pack) | B 39 → 27 % | ❌ El producto barato canibaliza las ventas del pack en Etsy y el upsell es demasiado bajo. **Descartado.** |
| Catálogo A + B | → 62 % (correl.) / 72 % (indep.) | ✅ en números, pero son **dos productos muy distintos** (una herramienta web y unas plantillas): mucho trabajo. |
| **Catálogo B en dos sectores** (inmobiliarias + 2.º sector con la mitad de tráfico) | → **58 %** (correl.) / 69 % (indep.) | ✅ **Recomendado:** reutiliza el mismo flujo de trabajo en Canva, y el segundo sector cuesta mucho menos que el primero. |

## Por qué el catálogo funciona (y su trampa)
- Con un solo producto, todo depende de **un** valor de tráfico en Etsy, que es muy incierto. Con dos productos hay dos oportunidades, y el dominio y la tienda se pagan una sola vez.
- **Trampa:** el modelo no cuenta el doble de trabajo. Si construir el segundo producto retrasa o empeora el primero, la ventaja desaparece. Por eso el plan es: **primero B-inmobiliarias completo, y después el segundo sector** reutilizando las plantillas base.
- La cota "correlacionada" asume que si el vendedor o Etsy fallan en un producto, fallan también en el otro. Es la que se toma como referencia.

## Qué hay que acertar sí o sí (sin cambios respecto a v1)
1. **Las visitas en Etsy** (`etsy_max`) y **su conversión** (`p_etsy`). Siguen siendo los rangos más anchos y los que más mueven el resultado.
2. **Diseño original** (no se puede revender una plantilla de Canva apenas modificada ni usar elementos de Canva Pro sueltos), o el producto no se puede vender.
3. **Constancia** publicando en redes y Pinterest (el abandono está modelado con un 6 % al mes).

## Siguiente trabajo útil (no depende de la elección)
- Acotar `etsy_max` con datos gratuitos (autocompletado de Etsy, número de anuncios y reseñas en "plantillas inmobiliaria"/"real estate canva template").
- Elegir el 2.º sector de B con datos (clínicas estéticas, peluquerías, academias…).
- Tornado de sensibilidad del catálogo BB.

---

## Anexo — VEREDICTO v1 (Día 5, 2026-10-25), conservado como historial

> Provisional porque el humano todavía no ha elegido idea. Es una **estimación del modelo** bajo supuestos conservadores, **no una garantía**.
> Datos: `../simulador/resultados/resultados_fase2.md` (20.000 corridas por idea, semilla 42).

### Pregunta de salida de Fase 2: ¿el modelo conservador alcanza ≥ 500 €?

**No, en ninguna de las tres ideas.** En el escenario **base** (todos los parámetros en su mediana) ninguna llega a 500 € en 12 meses:

| Idea | Pesimista | Base | Optimista | P(≥ 500 €) | Ventas necesarias |
|---|---|---|---|---|---|
| A Opositores | −1 € | 151 € | 2.882 € | **22 %** | ≈ 48 |
| B Inmobiliarias | 9 € | 262 € | 3.301 € | **39 %** | ≈ 42 |
| C Estudiantes | −7 € | 79 € | 1.563 € | **9 %** | ≈ 106 |

### Qué ha cambiado respecto a la vista previa del Día 4
- La vista previa daba A 42 % · B 35 % · C 23 %. Con el embudo de dos etapas (visita → generador → compra ≈ 0,3 %) y el retraso del SEO, **A baja a la mitad y B pasa a ser la más fuerte**.
- La razón es el **canal Etsy**: da visitas desde el primer mes, sin esperar a Google, y convierte directamente (1–3 %). En B es el parámetro que más mueve el resultado (correlación +0,7).

### Qué hay que acertar sí o sí (sensibilidad)
- **A:** el tráfico de Google en madurez (`seo_max`) y la conversión del generador al pack (`p_compra`).
- **B:** las visitas en Etsy (`etsy_max`) y su conversión (`p_etsy`).
- **C:** el ticket de 7 € obliga a vender más de 100 unidades; aunque crezca el tráfico, sigue débil.

### Qué significa para el proyecto
1. Según la regla de la Fase 2, **ninguna idea pasa todavía a Fase 3 tal cual**. Toca **ajustar la idea** (volver a Fase 1 con lo aprendido), no empezar de cero.
2. Ajustes candidatos a simular en el Día 6 (sin coste real):
   - **Etsy + web en todas las ideas** desde el primer día (ya incluido en A y B).
   - **Subir el ticket:** packs por oposición concreta a 19–24 € (A) o un pack "agencia" de 29 € (B).
   - **Combinar A+B como catálogo** (dos públicos y dos canales): probar si la suma supera el umbral en la mediana.
   - **Producto escalera:** artículo barato en Etsy (3–5 €) que lleve al pack completo.
3. **Recomendación provisional actualizada: B (inmobiliarias)**, con A como alternativa sólida. El 🔴 sigue siendo tuyo: ver `../🔴_ACCION_REQUERIDA.md`.

### Límites conocidos del modelo
- Sin volúmenes absolutos de búsqueda: los rangos de tráfico son estimaciones [E] anchas.
- El rango de Etsy para B sale de anécdotas de vendedores, no de datos sistemáticos.
- La comparación de lanzamiento en febrero o junio de 2027 apenas cambia la probabilidad, porque se miden 12 meses desde el lanzamiento en ambos casos. **La ventaja de lanzar antes es llegar antes a esos 12 meses**, no vender más dentro de ellos.
