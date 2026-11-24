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

## Día 2 — 2026-11-24 (Fase 1: Investigación → finalistas)

**Nota**: la sesión anterior fue el 2026-10-19; la tarea no se ejecutó a diario en este intervalo. Para no perder el calendario (entrega 15-may-2027), cerré la Fase 1 con una versión 1 de finalistas en vez de alargarla.

**Avances**
- `investigacion/04_DEMANDA_COMPETENCIA.md`: señales de demanda y competencia para L1, L2, L3, L5, L7, L11; puntuación P1–P6.
- `investigacion/05_TAM_SAM_SOM.md`: mercado de las 3 mejores (datos INE DIRCE 2025 y Ministerio de Educación; el resto marcado como estimación).
- `investigacion/FINALISTAS.md`: A = planner de estudio (3,55), B = plantillas Canva para negocios locales (3,35), C = imprimibles Primaria (3,15). **Recomiendo A.**
- Edad verificada: Etsy permite 13–17 solo con cuenta del tutor [V]; Gumroad exige edad legal para contratar [V].
- `🔴_ACCION_REQUERIDA.md` creado: elegir idea.

**Decisiones**
- L10 descartada: el EULA de Minecraft prohíbe vender mods.
- L11 y L2 descartadas por puntuación (lo gratis aprieta demasiado).
- L7 y L8 se integran en A (imán de tráfico gratis y bonus).
- Hotmart añadido como canal candidato (muy usado en español).

**Aprendizaje honesto**
- En las tres finalistas el rango de SOM cruza los 500 €: ninguna llega con seguridad. La variable que decide es el tráfico, no el producto.
- Etsy bloquea la lectura automática y no tengo volúmenes de búsqueda reales; la demanda se apoya en señales cualitativas.

**Bloqueos**: decisión humana pendiente (no bloquea: la Fase 2 puede empezar en paralelo para las tres).

**Primera tarea de la próxima sesión**: comprobar `RESPUESTA_HUMANO.md`. Si no existe, investigar benchmarks para el modelo (tráfico orgánico en Etsy y TikTok, conversión de producto digital, estacionalidad escolar) y escribir `modelo/modelo.md` + esqueleto del simulador.
