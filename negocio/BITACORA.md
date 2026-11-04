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

## Día 2 — 2026-11-04 (Fase 1: Investigación)

*(Nota: desde la sesión anterior, el 19-oct, pasaron 16 días sin ejecución; se retoma sin pérdidas.)*

**Avances**
- Nuevo `investigacion/04_DEMANDA_COMPETENCIA.md`: competencia y precios reales para L1, L2, L3, L5 y L11, con fuentes.
- Dato oficial de mercado: **2.089.403 alumnos de ESO** (curso 2024-25, Ministerio de Educación).
- Edad mínima **verificada** en los términos oficiales de Etsy (13-17 años permitidos solo con un adulto titular), Gumroad (≥13 + capacidad contractual) y Payhip (B2B, sin edad, exige plena capacidad). Conclusión: el adulto es siempre el titular. Actualizado `02_PLATAFORMAS_Y_COSTES.md`.
- **L10 (Minecraft) descartada**: vender mods o add-ons fuera del Marketplace oficial no está permitido según fuentes secundarias (la web oficial dio error 503).
- **Nueva idea L13**: recursos en español para profesores de inmersión dual en EE. UU., vendidos en Teachers Pay Teachers. TpT cambió sus planes el 1-oct-2026: Basic paga el 55 % − 0,30 $ por recurso (pendiente de confirmar en la fuente oficial).
- Puntuación provisional: **L1 3,80** > L13 3,20 > L3 2,90 > L5 2,80 > L2 2,45.

**Decisiones**
- L8 (ebook), L11 (flashcards) y L7 (generador de horarios) pasan a ser **complementos de L1**, no ideas independientes.
- L5 y L2 bajan a "débiles": formato copiado, precios hundidos y muchos sustitutos gratis.

**Aprendizaje honesto**
- No hay herramientas de volumen de búsqueda en esta sesión: P1 (demanda) se apoya en señales indirectas (nº de listados, precios, reseñas). Hay que reforzarlo.
- L1 tiene un hueco real (no encontré ningún planner adaptado al sistema educativo español: materias LOMLOE, calendario escolar, EBAU/PAU), pero estrecho. Además, quien paga suele ser la familia, no el estudiante.

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: señales de volumen (Google Trends, autocompletado, Reddit) para L1 y L13; competencia de L7; confirmar las comisiones de TpT; empezar el TAM/SAM/SOM de L1.
