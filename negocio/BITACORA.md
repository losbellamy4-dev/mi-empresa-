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

## Día 2 — 2026-10-24 (Fase 1: Investigación)

**Avances**
- Nuevo `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: oferta y precios en español para L1 (1–14 €, sobre todo agendas para docentes y Notion), L11 (no se encontraron mazos Anki para la PAU → mayor hueco), L3 (docentes venden a 2–8,50 €), L5 (packs a 10–20 €, pero Canva regala plantillas parecidas).
- Datos de público: ESO ≈ 2,07 M y Bachillerato ≈ 0,71 M alumnos (previsión del Ministerio 2025-26); ≈ 340.000 hacen la PAU cada año [E].
- Edad mínima verificada: Etsy (13–17 solo con cuenta del tutor), Lemon Squeezy y Payhip (exigen negocio lícito / PayPal-Stripe → titular adulto), Gumroad 18+ (fuente secundaria). Actualizado `02_PLATAFORMAS_Y_COSTES.md`.
- L10 (Minecraft) **descartada**: las normas de Mojang no permiten cobrar por add-ons fuera del Marketplace.

**Decisiones**
- Ranking provisional: L1+L7 (3,4) > L11 (3,1) > L5 (2,8) > L3 (2,4). L2 sin puntuar aún.
- Nueva candidata a estudiar: **kit de estudio combinado (L1+L7+L11)**, con una herramienta web gratuita como imán de tráfico.

**Limitaciones honestas**
- Etsy bloquea la lectura automática (403): no he podido contar reseñas en español. Sin acceso a datos de volumen de búsqueda; la demanda se infiere de la oferta existente.

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: investigar L2 (finanzas personales) y los canales de tráfico accesibles a un menor (normas de edad de TikTok/YouTube/Pinterest), para estimar visitas alcanzables (SOM).
