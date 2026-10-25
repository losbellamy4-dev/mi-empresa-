# VEREDICTO del simulador — v1 (Día 5, 2026-10-25) · PROVISIONAL

> Provisional porque el humano todavía no ha elegido idea. Es una **estimación del modelo** bajo supuestos conservadores, **no una garantía**.
> Datos: `../simulador/resultados/resultados_fase2.md` (20.000 corridas por idea, semilla 42).

## Pregunta de salida de Fase 2: ¿el modelo conservador alcanza ≥ 500 €?

**No, en ninguna de las tres ideas.** En el escenario **base** (todos los parámetros en su mediana) ninguna llega a 500 € en 12 meses:

| Idea | Pesimista | Base | Optimista | P(≥ 500 €) | Ventas necesarias |
|---|---|---|---|---|---|
| A Opositores | −1 € | 151 € | 2.882 € | **22 %** | ≈ 48 |
| B Inmobiliarias | 9 € | 262 € | 3.301 € | **39 %** | ≈ 42 |
| C Estudiantes | −7 € | 79 € | 1.563 € | **9 %** | ≈ 106 |

## Qué ha cambiado respecto a la vista previa del Día 4
- La vista previa daba A 42 % · B 35 % · C 23 %. Con el embudo de dos etapas (visita → generador → compra ≈ 0,3 %) y el retraso del SEO, **A baja a la mitad y B pasa a ser la más fuerte**.
- La razón es el **canal Etsy**: da visitas desde el primer mes, sin esperar a Google, y convierte directamente (1–3 %). En B es el parámetro que más mueve el resultado (correlación +0,7).

## Qué hay que acertar sí o sí (sensibilidad)
- **A:** el tráfico de Google en madurez (`seo_max`) y la conversión del generador al pack (`p_compra`).
- **B:** las visitas en Etsy (`etsy_max`) y su conversión (`p_etsy`).
- **C:** el ticket de 7 € obliga a vender más de 100 unidades; aunque crezca el tráfico, sigue débil.

## Qué significa para el proyecto
1. Según la regla de la Fase 2, **ninguna idea pasa todavía a Fase 3 tal cual**. Toca **ajustar la idea** (volver a Fase 1 con lo aprendido), no empezar de cero.
2. Ajustes candidatos a simular en el Día 6 (sin coste real):
   - **Etsy + web en todas las ideas** desde el primer día (ya incluido en A y B).
   - **Subir el ticket:** packs por oposición concreta a 19–24 € (A) o un pack "agencia" de 29 € (B).
   - **Combinar A+B como catálogo** (dos públicos y dos canales): probar si la suma supera el umbral en la mediana.
   - **Producto escalera:** artículo barato en Etsy (3–5 €) que lleve al pack completo.
3. **Recomendación provisional actualizada: B (inmobiliarias)**, con A como alternativa sólida. El 🔴 sigue siendo tuyo: ver `../🔴_ACCION_REQUERIDA.md`.

## Límites conocidos del modelo
- Sin volúmenes absolutos de búsqueda: los rangos de tráfico son estimaciones [E] anchas.
- El rango de Etsy para B sale de anécdotas de vendedores, no de datos sistemáticos.
- La comparación de lanzamiento en febrero o junio de 2027 apenas cambia la probabilidad, porque se miden 12 meses desde el lanzamiento en ambos casos. **La ventaja de lanzar antes es llegar antes a esos 12 meses**, no vender más dentro de ellos.
