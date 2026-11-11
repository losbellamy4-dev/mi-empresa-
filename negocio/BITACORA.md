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

## Día 2 — 2026-11-11 (Fase 1: Investigación)

**Avances**
- Nuevo `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: competencia, precios y huecos de L1, L2, L3, L5, L7 y L11, con fuentes.
- Datos oficiales de mercado: ~2,07 M alumnos de ESO y ~708.000 de Bachillerato (Ministerio, 2025-26); ~300.000 presentados a la PAU 2026.
- Edad mínima: Etsy confirma 18+ con cuenta del tutor para 13–17 (verificado). Gumroad exige edad legal para contratar. Payhip y Lemon Squeezy siguen sin verificar.
- Puntuación provisional: L1 3,55 · L11 3,35 · L5 2,95 · L2 2,65 · L3 2,35 · L7 2,05.

**Decisiones**
- **L10 (Minecraft) descartada**: el EULA prohíbe lucrarse con contenido sin permiso de Mojang.
- L2 y L3 bajan a "débil" (competencia densa en español, poca ventaja del dueño).
- L7 deja de ser negocio por sí misma: pasa a ser "imán de tráfico" gratuito para L1/L11.

**Aprendizaje honesto**
- No encontré ningún mazo de flashcards de pago para la PAU en español. Eso puede ser un hueco o una señal de que los estudiantes no pagan por esto (Wuolah lo da gratis). Todavía no puedo saber cuál de las dos.
- Los planners en español se venden a 3–7 €: para llegar a 500 € netos harían falta del orden de 80–170 ventas. El precio bajo obliga a crear paquetes.

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: Google Trends + conteo de reseñas para L1 y L11; TAM/SAM/SOM; plan de canal de tráfico para cada candidata.
