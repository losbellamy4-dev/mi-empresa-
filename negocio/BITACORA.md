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

## Día 2 — 2026-11-18 (Fase 1: Investigación)

*(Nota: han pasado ~30 días desde la sesión anterior; se retoma sin pérdida de estado.)*

**Avances**
- `investigacion/04_DEMANDA_COMPETENCIA.md`: primera pasada de demanda y competencia para L1, L2, L3, L5, L7, L11 con fuentes.
- Datos oficiales de tamaño: ESO 2.089.403 alumnos; PAU 2025 320.927 matriculados; 1,8 M empresas sin asalariados y 313.827 locales de hostelería (INE DIRCE 2025, tabla descargada y leída).
- Edad: Etsy confirmado [V] → cuenta a nombre del adulto (13–17 solo bajo su supervisión). Gumroad ≥13 (fuente débil). Payhip/Lemon Squeezy siguen sin verificar.
- L10 (Minecraft) **descartada**.

**Decisiones / hallazgos**
- Ninguna idea suelta destaca (puntuaciones 2,75–3,25). L1 y L3 sufren mucha competencia gratuita (Notion, AulaPT, Tes).
- Señal de demanda más sólida: el mercado de la PAU (fecha fija, ~320 k estudiantes/año, Wuolah con ~500 k usuarios activos al mes).
- Propuesta nueva: **L13 "Kit 2º Bachillerato + PAU"** combinando L11 + L1 + L7 + L8.
- ⚠️ Calendario: si gana L13, el lanzamiento debería ser marzo–abril de 2027, antes de la entrega del 15 de mayo.

**Bloqueos**: ninguno. Aún no hace falta que intervenga el humano.

**Primera tarea de mañana**: pasar L13 por el filtro y puntuarla; comprobar si alguien vende flashcards/mazos de pago para la PAU.
