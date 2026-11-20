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

## Día 2 — 2026-11-20 (Fase 1: Investigación)

*(Nota: entre el Día 1, el 19-oct, y hoy no hubo sesiones registradas; se retoma desde el estado guardado.)*

**Avances**
- Nuevo `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: demanda y competencia de cada idea viva, con fuentes y marcas [V]/[S]/[E].
- Edad verificada: **Etsy** (18+; de 13 a 17 solo con la cuenta del adulto) y **TPT** (18+) → se confirma que todo va a nombre del adulto.
- Comisiones de TPT actualizadas: Basic 55 % − 0,30 $; Exclusive 77,5 % (59,95 $/año, exclusividad); Premium cerrado desde el 1-oct-2026.
- Datos de TPT reales: el producto top de "dual language" tiene 275 valoraciones a 7,95 $; los que más venden son pósteres y etiquetas sencillos.

**Decisiones**
- L10 (Minecraft) **descartada**: el canal de venta está cerrado a partners aprobados.
- L2 (finanzas) → reserva: mercado saturado y sin ventaja propia.
- L7 → solo como herramienta gratuita para atraer tráfico (compite con la IA gratuita).
- Nueva subidea **L3-US**: recursos en español para docentes de programas de inmersión dual en EE. UU. (más de 3.600 programas, ~80 % en español).

**Aprendizaje honesto**
- El planner de estudio (L1), que parecía la más natural, compite contra plantillas **gratis** de Canva, Notion y Slidesgo. La idea "obvia" no es la mejor.
- La demanda pagada más clara está en los compradores que ya pagan por costumbre: pequeños negocios (L5) y docentes de EE. UU. (L3-US).

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: TAM/SAM/SOM y puntuación P1–P6 de las 3 candidatas (L5, L3-US, Kit EBAU) → borrador de `FINALISTAS.md`.
