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

## Día 2 — 2026-11-25 (Fase 1: Investigación)

> Nota: entre el día 1 (19-10) y hoy han pasado 5 semanas sin ejecutarse la tarea. El calendario sigue cumpliéndose de sobra (la entrega es el 15-5-2027), pero si la tarea debía ser diaria, merece la pena revisar la programación.

**Avances**
- `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: poblaciones base (ESO 2.089.403; matriculados en la PAU 2024: 341.831) y demanda y competencia de L1, L2, L3, L5 y L11. Ranking provisional.
- `investigacion/05_EDAD_EN_PLATAFORMAS.md`: Etsy y Gumroad exigen mayoría de edad o capacidad para contratar; Payhip y Lemon Squeezy no fijan una edad pero dependen de Stripe/PayPal. Se confirma que **todo va a nombre del adulto**.

**Decisiones**
- **L10 descartada**: la EULA de Minecraft prohíbe vender mods y mapas fuera del Marketplace oficial.
- L8 (ebook) queda absorbida como bonus del kit de estudio.
- Mejor candidata provisional: **kit de estudio para ESO/Bachillerato en España (L1+L7+L11)**, con una herramienta web gratuita como imán de tráfico.

**Aprendizaje honesto**
- Hay un riesgo nuevo: si el comprador es un adolescente, lo normal es que no tenga tarjeta → más fricción de pago. Las ideas con público adulto (L2, L5) tienen el cobro más fácil pero menos ventaja del dueño. El simulador tendrá que modelar este equilibrio.
- Sin herramientas de volumen de búsqueda, la demanda solo está medida con señales indirectas. Es una debilidad que hay que corregir.

**Bloqueos**: ninguno. Todavía no hace falta que intervenga un humano.

**Primera tarea de mañana**: buscar una fuente gratuita de volumen de búsqueda y un dato sobre la fricción de pago en compradores adolescentes.
