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

## Día 2 — 2026-11-05 (Fase 1: Investigación)

**Avances**
- Nuevo `investigacion/04_DEMANDA_Y_COMPETENCIA.md`.
- **Edad mínima:** Etsy tiene vía oficial para 13–17 años (el tutor registra la cuenta con sus datos y es el *shop owner*) [verificado en help.etsy.com]. Gumroad/Payhip/Lemon Squeezy: sin confirmación oficial → se asume cuenta del adulto.
- **L10 (Minecraft) descartada**: el EULA prohíbe vender contenido/add-ons sin permiso de Mojang.
- Señales de demanda/competencia para L1, L2, L3, L5, L11 (precios reales, competidores, competencia gratuita).
- Primeros datos de mercado: Bachillerato 1.125.860 alumnos (2024-25); total no universitario 8,25 M (2025-26).

**Decisiones**
- L7 (generador de horarios) y L8 (ebook) dejan de ser ideas independientes: se integran en L1 como imán de tráfico y bonus.
- Ranking provisional: L1 3,75 > L5 3,20 > L11 2,80 > L3 2,60 > L2 2,45.

**Aprendizaje honesto**
- Las búsquedas web dan listados sueltos, no cifras de ventas; la única señal numérica fuerte hoy es una tienda Etsy de plantillas Canva en español con ~1.600 ventas (L5).
- Hueco en L1: no encontré planners específicos de ESO/Bachillerato español. Ojo: no encontrarlo no demuestra que no existan.
- El PDF del Ministerio y las pautas de Minecraft devolvieron error 503; reintentar.

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: contar reseñas/ventas de los primeros listados de Etsy en español para L1 y L5, y calcular TAM/SAM/SOM.
