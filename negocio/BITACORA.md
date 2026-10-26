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

## Día 2 — 2026-10-26 (Fase 1: Investigación)

**Avances**
- `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: competencia y precios reales para L1, L2, L3, L5, L11 y L10 (con fuentes).
- `investigacion/05_TAM_SAM_SOM.md`: TAM con datos oficiales (2,79 M alumnos ESO+Bachillerato; ~248 k maestros de Primaria). SAM/SOM estimados y marcados como tales. L1: SOM ≈ 220–1.150 € → 500 € cabe dentro del rango, no en el extremo bajo.
- Verificado [V]: Etsy exige titular 18+; de 13 a 17 solo con cuenta del tutor. Canva: plantillas con contenido Pro solo se venden como enlace de plantilla, no como PDF.

**Decisiones**
- **L10 (Minecraft) descartada**: monetizar mapas/addons fuera del Marketplace está restringido; un servidor de pago choca con F2 y F6.
- **L1 se consolida como favorita**: ningún competidor encontrado adapta el planner al sistema español (LOMLOE, trimestres, PAU); el dueño es el usuario objetivo.
- L3, L2, L5 bajan (tickets bajos, saturación o falta de credibilidad). L11 pasa a bonus.

**Aprendizaje honesto**
- No tengo datos de volumen de búsqueda ni de reseñas en Etsy: la demanda medida hoy es indirecta. Lo dejo marcado.
- Riesgo nuevo para el simulador: el comprador de L1 suele ser la familia, no el estudiante (fricción de pago → conversión más baja).

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: investigar L7 y los canales de tráfico de L1 (alcance orgánico en TikTok/Instagram, Pinterest, búsquedas en Etsy) con cifras reales; elegir el 3er finalista y empezar `FINALISTAS.md`.
