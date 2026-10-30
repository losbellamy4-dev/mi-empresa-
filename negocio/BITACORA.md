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

## Día 2 — 2026-10-30 (Fase 1: Investigación)

**Avances**
- Nuevo `investigacion/04_DEMANDA_COMPETENCIA.md`: competencia, precios, sustitutos gratuitos y tamaño de la población objetivo de cada idea viva, con fuentes y etiquetas [V]/[S]/[E]/[?].
- Población: ~2,78 M alumnos de ESO+Bachillerato en España (previsión 2025-26, por confirmar); ~3,15 M microempresas (DIRCE 2025, vía fuente secundaria).
- Edad en plataformas: Etsy exige que la cuenta sea del tutor para 13–17 años; Gumroad ≥13 (sin confirmar). Payhip/Lemon Squeezy, sin dato.

**Decisiones**
- L10 (Minecraft) **descartada**: la venta de contenido está restringida a canales autorizados por Mojang.
- L7 deja de ser idea independiente: hay demasiadas alternativas gratuitas (Canva Code, MyStudyLife). Pasa a **herramienta gratuita para atraer tráfico a L1**.
- L2 y L3 bajan de prioridad: mercados saturados y mucha oferta gratuita; el dueño no tiene ventaja de credibilidad.
- Ranking provisional: 1) L1+L7+L8, 2) L5, 3) L11 reorientada (plan PAU, sin temario).

**Aprendizaje honesto**
- Sin herramienta de volumen de búsqueda, la demanda se infiere de la oferta existente. Es una señal débil: lo tendré en cuenta en la puntuación.
- Para L1, 500 € netos ≈ 100 ventas a ~5 € ≈ 10.000 visitas cualificadas al 1 % de conversión. **El canal de tráfico es el riesgo nº 1.**

**Bloqueos**: ninguno. Todavía no hace falta nada del humano.

**Primera tarea de mañana**: buscar una tercera candidata de otra familia (para que las finalistas no se solapen) e investigar el canal studytok/studygram en español.
