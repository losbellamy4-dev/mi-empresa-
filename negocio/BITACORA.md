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

## Día 2 — 2026-11-09 (Fase 1: Investigación)

**Avances**
- Nuevo `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: señales de demanda, competencia y hueco de L1, L2, L3, L5, L7 y L11, con fuentes.
- Edad en plataformas: Etsy verificada en fuente oficial (titular 18+; de 13 a 17 solo bajo la cuenta del tutor, con su facturación). Gumroad, Payhip y Lemon Squeezy siguen sin verificar → supuesto: cuenta del adulto.
- TAM/SAM/SOM preliminar de L1, con un dato oficial: 2.089.403 alumnos de ESO + 704.256 de Bachillerato (curso 2024-25).

**Decisiones**
- **L10 descartada**: el EULA de Minecraft prohíbe vender add-ons fuera del Marketplace oficial.
- L7 (herramienta web) y L8 (ebook) dejan de ser ideas independientes y pasan a ser **complementos de L1** (imán de tráfico y bonus).
- Ranking provisional: L1 > L5 > L11 > L2 > L3.

**Aprendizaje honesto**
- No he encontrado ninguna agenda para ESO/Bachillerato adaptada al sistema español (curso sep–jun, trimestres, PAU); las que hay son genéricas o están desactualizadas. Es un hueco real, pero con precios bajos (2–12 €).
- Para L1, el SOM estimado (30–280 compradores) contiene el umbral de ~70 ventas, pero su extremo bajo se queda corto. El canal de tráfico sigue siendo el riesgo n.º 1.
- Limitación de método: Etsy bloquea la descarga automática de sus búsquedas y no tengo volúmenes de búsqueda exactos. Uso señales indirectas y lo marco como tal.

**Bloqueos**: ninguno. (Opcional 🔴: si el adulto tiene una cuenta de Google Ads, el Planificador de palabras clave daría volúmenes reales de búsqueda en España.)

**Primera tarea de mañana**: TAM/SAM/SOM de L5 y L11, buscar mazos de la PAU en AnkiWeb y Quizlet, puntuar todas las ideas con P1–P6 y empezar el borrador de FINALISTAS.md.
