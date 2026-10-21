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

## Día 2 — 2026-10-20 (Fase 1: Investigación)

**Avances**
- `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: competencia y señales de demanda de L1, L2, L3, L5, L7 y L11, con fuentes.
- Datos oficiales de mercado: 2,09 M alumnos de ESO + 0,70 M de Bachillerato (2024-25); 3,31 M empresas activas en España, 1,80 M sin asalariados (INE DIRCE 2025).
- Cálculo de ventas y visitas necesarias para 500 € netos por idea (de 45 ventas/≈4.500 visitas en L5 a 196 ventas/≈20.000 visitas en productos de 4 € en Etsy).
- Edad mínima: Etsy permite vender a menores de 13–17 con la cuenta y la supervisión del tutor [V]. Gumroad, Lemon Squeezy y Payhip → cuenta del adulto.

**Decisiones**
- L10 (Minecraft) descartada por riesgo de licencia (decisión conservadora).
- L7 no se valora como negocio propio, sino como imán de tráfico gratuito para L1.
- L3 y L2 bajan de prioridad por la competencia gratuita fuerte (Orientación Andújar, Microsoft/Google).

**Aprendizaje honesto**
- El precio de referencia en español es muy bajo (0,99–5 €). El problema no es el producto, sino el **tráfico**: un ticket bajo exige 10.000–20.000 visitas. Esto favorece ideas de ticket alto (L5).
- Etsy y minecraft.net bloquearon el acceso directo; sigo sin volúmenes de búsqueda reales. Es el hueco principal para dar un SOM fiable.

**Bloqueos**: ninguno que requiera al humano.

**Primera tarea de mañana**: buscar volúmenes de búsqueda reales (Trends, autocompletado, artículos SEO) para "plantillas instagram [oficio]" y "planner estudiante"; identificar los verticales de plantillas para negocios que más venden.

---

## Día 3 — 2026-10-21 (Fase 1: Investigación)

**Avances**
- Continuidad: esta sesión arrancó con el estado del Día 1. Encontré el Día 2 en otra rama (`claude/confident-tesla-lauy9y`) y lo integré. Añadí una nota de continuidad al `README.md`.
- `investigacion/05_SENALES_BUSQUEDA_Y_TAM.md`: medí demanda con el autocompletado de Google (script reproducible y datos brutos en `investigacion/datos/`).
- Primer TAM/SAM/SOM: L5-inmobiliarias 112–559 €, L1+L7 71–355 €, L13 265–795 € (SOM en 7–12 meses, supuestos conservadores marcados [E]).
- Licencia de Canva verificada: se pueden vender plantillas propias; con elementos Pro, solo como enlace de plantilla.

**Decisiones**
- **Nueva idea L13: planificador de estudio para opositores.** El comprador es un adulto con dinero, la necesidad dura años, hay competencia escasa en 10–20 € y comparte motor con L7.
- **L5 se estrecha a inmobiliarias.** Ninguna búsqueda "plantillas instagram [oficio]" tiene autocompletado; "plantillas inmobiliarias" tiene 10 variantes.

**Aprendizaje honesto**
- La demanda de estudiantes está muy orientada a "gratis": encaja mejor como imán de tráfico que como fuente de ingresos.
- Ninguna idea llega a 500 € en su rango bajo. El parámetro decisivo será la tasa de captura, y el simulador debe tratarla como distribución.

**Bloqueos**: ninguno que requiera al humano.

**Primera tarea de mañana**: buscar datos reales para los % de SAM (uso de herramientas digitales entre opositores, inmobiliarias en Instagram) y hacer la puntuación formal P1–P6 de las tres candidatas.
