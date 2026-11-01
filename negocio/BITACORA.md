# BITÁCORA — Micro-negocio digital validado por simulación

Diario del proyecto. Una entrada por sesión. Fecha límite de entrega: 15 de mayo de 2027.

---

## Día 1 — 2026-10-19 (Fase 1: Investigación)

**Avances**
- Creada la estructura `/negocio/` (investigacion, modelo, simulador, web, entregables), `ESTADO.json` y esta bitácora.
- `investigacion/00_CRITERIOS.md`: 8 filtros obligatorios + 6 criterios de puntuación ponderados.
- `investigacion/02_PLATAFORMAS_Y_COSTES.md`: comisiones de Gumroad, Lemon Squeezy, Payhip, Etsy, TpT, Fiverr; restricciones de edad (Stripe exige tutor como titular si <18; Fiverr solo cuenta del tutor 13–17); benchmarks de conversión (2–6 % landing pages → supuesto conservador 1 %).
- `investigacion/01_PANORAMA_MODELOS.md`: 6 familias de modelos analizadas.
- `investigacion/03_LISTA_LARGA.md`: 12 ideas, 7 pasan el primer filtro.

**Decisiones**
- Todo cobro irá a nombre del adulto responsable (diseño desde el día 1).
- Descartada L4 (plantillas de facturación para autónomos): VeriFactu exige software certificado a autónomos desde 1-jul-2027.
- El hueco competitivo más claro es el **idioma español**; el riesgo principal es el **canal de tráfico** (sin audiencia, la web propia sola no vende).

**Aprendizaje honesto**
- La mediana de un creador en Gumroad ronda 70 $/año (dato 2020). 500 € está muy por encima de lo típico: el simulador deberá modelar una alta probabilidad de cero ventas si no hay canal de tráfico.

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: validar demanda y competencia en español de L1 (planners de estudio), L3 (imprimibles educativos) y L5 (plantillas Canva para negocios locales).

---

## Día 2 — 2026-11-01 (Fase 1: Investigación)

*Nota: entre el 19-oct y el 1-nov no hubo sesiones registradas; se retoma exactamente donde quedó el Día 1.*

**Avances**
- `investigacion/04_DEMANDA_COMPETENCIA.md`: competencia y precios en español para L1, L2, L3, L5, L11 (con fuentes), verificación de edad mínima y puntuación preliminar P1–P6.
- Edad mínima **Etsy verificada** [V]: el tutor crea la cuenta con sus datos y tiene toda la información financiera a su nombre. Gumroad: "edad legal para contratar". Payhip/Lemon Squeezy: sin dato → cuenta del adulto.
- Primeras cifras de mercado: ~2,07 M alumnos de ESO y ~0,71 M de Bachillerato (2025-26, leídas de un gráfico del Ministerio, **pendiente de verificar**; el PDF oficial dio error 503).

**Decisiones**
- **L10 (Minecraft/Roblox) descartada**: solo contenido cosmético y Mojang puede retirar permisos sin aviso.
- **L8 (ebook) fusionada en L1** como bonus; **L7** se mantiene solo como imán de tráfico gratuito para L1.

**Puntuación preliminar** [E]: L5 Canva negocios locales 3,50 · L1 planners estudio 3,35 · L2 presupuesto 3,00 · L3 imprimibles Primaria 2,85 · L11 Anki EBAU 2,65 · L7 2,50.

**Aprendizaje honesto**
- La oferta en español existe en todas las categorías, pero es **muy barata** (1–7 $ en planners, 1–2,50 € en fichas). L5 tiene el ticket más alto (8–37 €) porque compra un negocio, no un particular.
- No encontré mazos Anki de pago para EBAU: puede ser hueco o falta de disposición a pagar. Sin más datos, L11 sigue débil.
- Las señales de demanda siguen siendo indirectas (no hay acceso a volúmenes de búsqueda).

**Pregunta útil para Adrián (no bloquea nada):** ¿sabes usar Canva o te apetece diseñar para negocios (peluquerías, cafeterías…)? Cambia la nota de L5 frente a L1. Si quieres responder, escribe en `negocio/RESPUESTA_HUMANO.md`.

**Bloqueos**: ninguno.

**Primera tarea de mañana**: contar reseñas/ventas de los 10 primeros listados de Etsy/Gumroad para L1 y L5; crear `05_TAM_SAM_SOM.md`.
