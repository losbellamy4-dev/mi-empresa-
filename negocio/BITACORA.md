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

## Día 2 — 2026-11-06 (Fase 1: Investigación)

**Avances**
- Nuevo `investigacion/04_DEMANDA_COMPETENCIA.md`: competencia y precios en español de L1, L2, L3, L5, L11; TAM/SAM/SOM v1 de L1; puntuación preliminar P1–P6.
- `02_PLATAFORMAS_Y_COSTES.md`: edad mínima de Etsy verificada en su ayuda oficial (13–17 solo con el tutor como titular de cuenta y tienda). Gumroad: edad legal para contratar → cuenta del adulto.
- `03_LISTA_LARGA.md`: L10 descartada; L8 fusionada en L1.

**Decisiones**
- L10 (Minecraft) fuera: el EULA prohíbe vender contenido sin permiso de Mojang.
- Candidatas provisionales a finalistas: **L1 planners de estudio (3,50)**, **L11 flashcards EBAU/PAU (3,35)**, **L5 plantillas Canva para negocios locales (3,10)**.

**Aprendizaje honesto**
- Las señales de demanda de hoy son cualitativas (competidores y precios), no cifras de ventas: confianza media-baja en P1.
- Los precios en español son bajos (2–10 €). Ventas necesarias para 500 €: L5 ≈ 35, L11 ≈ 60–85, L1 ≈ 85–140.
- La estacionalidad (septiembre para planners; marzo–junio para PAU) tendrá que ir en el simulador. La entrega del 15-may-2027 llega tarde para la temporada PAU 2027.

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: señales cuantitativas para L1/L11/L5 (Google Trends, reseñas en listados top) y TAM/SAM/SOM de L5 con datos DIRCE del INE.
