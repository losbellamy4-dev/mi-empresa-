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

## Día 2 — 2026-11-14 (Fase 1: Investigación)

**Avances**
- `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: demanda y competencia en español de L1, L2, L3, L5, L10, L11, con fuentes citadas y TAM/SAM/SOM preliminar de L1 y L1b (datos oficiales: 2,09 M alumnos de ESO, 0,70 M de Bachillerato y ~792.000 docentes en 2024-25).
- `investigacion/05_EDAD_MINIMA_PLATAFORMAS.md`: confirmado que en Etsy, Gumroad, Payhip, Lemon Squeezy/Stripe y TpT el titular y el cobro deben ser del adulto.
- `03_LISTA_LARGA.md` actualizada.

**Decisiones**
- **L10 descartada** (la EULA de Minecraft prohíbe vender mods; el Marketplace es solo para partners aprobados).
- **L2 y L11 pasan a reserva** (competencia gratuita fuerte / cultura de "todo gratis").
- **Nuevas variantes:** L1b (agenda/cuaderno del profesor de Secundaria) y L3b (recursos en español para aulas bilingües de EE. UU.).

**Aprendizaje honesto**
- El que paga no es el alumno: las agendas para alumnos se venden a unos 2 $ o se regalan, y las de docentes a 7–29 $. Vender a estudiantes de 14 años es difícil porque no tienen medio de pago propio.
- L1 en solitario solo llega a 500 € en el extremo optimista del SOM (estimación).
- Riesgo nuevo: la **estacionalidad**. El pico de compra docente (agosto–septiembre) cae después de la entrega del 15 de mayo de 2027. El simulador deberá modelarlo.
- Sin herramientas de volumen de búsqueda: la demanda se infiere de las ventas y reseñas visibles en los listados.

**Bloqueos**: ninguno. Todavía no hace falta que intervenga el humano.

**Primera tarea de mañana**: puntuar con P1–P6 las ideas vivas (L1b, L3b, L5, L1+L7) y profundizar en L3b (TpT) y en el nicho vertical de L5.
