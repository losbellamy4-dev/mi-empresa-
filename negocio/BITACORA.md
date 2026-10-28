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

## Día 2: 2026-10-28 (Fase 1: Investigación)

**Avances**
- `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: primera pasada de demanda y competencia para L1, L2, L3, L5, L7 y L11, con fuentes.
- TAM de L1 con dato oficial: 2.089.403 alumnos de ESO + 704.256 de Bachillerato (2024-25, La Moncloa) ≈ 2,79 M. SAM conservador 85–140 mil; 500 € ≈ 72 ventas.
- Edad mínima verificada: Etsy (13–17 solo con cuenta del tutor), Gumroad (13+ y capacidad contractual), Payhip (sin edad, pero exige PayPal/Stripe). Actualizado `02_PLATAFORMAS_Y_COSTES.md`.
- Licencia de Canva verificada (L5): se pueden vender plantillas, pero el contenido Pro solo como enlace de plantilla.

**Decisiones**
- **L10 (Minecraft) descartada**: el Marketplace exige Partner Program 18+ con empresa y fuera de él la monetización está restringida.
- **L3 degradada**: la demanda es real (mercado de docentes en Instagram), pero compiten docentes con credenciales a 2–5 €. El dueño no tiene ventaja.
- **L7 deja de ser negocio propio**: el mercado de herramientas gratuitas está saturado. Se queda como imán de tráfico gratuito dentro de L1.

**Aprendizaje honesto**
- Patrón: solo tienen ventaja real las ideas donde **el dueño es el cliente** (estudiantes). Ranking provisional: L1 > L2 (reorientada a adolescentes) > L11 > L5 > L3.
- Las señales de demanda de hoy son indirectas (nº de productos y contadores visibles de Gumroad). Falta un dato de volumen de búsqueda.
- Riesgo nuevo en L1: el comprador es menor, así que quizá paguen los padres. Hay que estudiar quién paga.

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: señales de volumen de búsqueda (Google Trends) para L1, L2 y L11, e investigar L2 reorientada a "finanzas para adolescentes".
