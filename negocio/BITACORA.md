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

## Día 2 — 2026-11-03 (Fase 1: Investigación)

**Avances**
- Nuevo `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: señales de demanda y competencia para L1, L2, L3, L5, L7, L10, L11 + puntuación provisional ponderada.
- `02_PLATAFORMAS_Y_COSTES.md`: verificado en Etsy que de 13 a 17 años se puede vender solo si el tutor registra la cuenta con sus datos y es responsable. Gumroad: hace falta tener edad legal para firmar contratos.
- `03_LISTA_LARGA.md`: L10 descartada y añadida L13.

**Decisiones**
- **L10 (Minecraft) descartada**: el EULA prohíbe lucrarse sin permiso de Mojang, y los mods solo se venden por el Marketplace oficial.
- **L11 (flashcards PAU) degradada**: hay muchísimo material gratis (AnkiWeb, Wuolah) y el dueño aún no ha cursado Bachillerato.
- **Nueva L13: agenda del docente en español**. Los docentes pagan, compran cada curso y la temporada alta (verano) cae justo después de la entrega.
- Puntuación provisional: **L1 3,60** · **L13 3,35** · L8 2,85 (como bonus de L1) · L2 2,70 · resto < 2,5.

**Aprendizaje honesto**
- En casi todos los nichos hay competencia gratuita fuerte. Los precios que se ven son bajos (2–8 €), así que para llegar a 500 € harían falta unas 70–250 ventas. El simulador tendrá que tomarse en serio el volumen de tráfico.
- Límite técnico: Etsy bloquea la lectura automática (403) y la web del Ministerio y minecraft.net devolvieron 503. Sin datos de reseñas reales todavía.

**Bloqueos**: ninguno. Todavía no hace falta que intervenga un humano.

**Primera tarea de mañana**: cifras oficiales de alumnado/docentes (reintentar Ministerio) → TAM/SAM/SOM de L1 y L13; reseñas de top listados vía herramientas SEO de terceros.
