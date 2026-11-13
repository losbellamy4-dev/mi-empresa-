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

## Día 2 — 2026-11-13 (Fase 1: Investigación)

*Nota: entre el día 1 (19-oct) y hoy no hubo sesiones registradas; el proyecto retoma sin pérdida de estado.*

**Avances**
- Nuevo `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: señales de demanda, competencia y precios para L1, L2, L3, L5, L11; datos base (ESO 2.089.477 y Bachillerato 704.424 alumnos —previsión—; >806.000 docentes no universitarios [V]).
- Edad mínima verificada en Etsy: titular 18+; 13–17 solo a través de la cuenta del tutor [V].

**Decisiones**
- **L10 (Minecraft) descartada** por el EULA de Mojang.
- **L11 (flashcards EBAU) casi descartada**: Wuolah ofrece apuntes gratis a la mitad de preuniversitarios (dato de la propia empresa).
- **L1 es la idea más fuerte** hasta ahora; hipótesis de producto combinado L1+L7+L8 ("kit de organización ESO/Bach en español" + herramienta gratuita de horarios como gancho).

**Aprendizaje honesto**
- Etsy bloquea la lectura automática y no tengo volúmenes de búsqueda reales: la demanda se mide de forma indirecta. Esto aumenta la incertidumbre del parámetro "tráfico" en el futuro simulador → rango amplio en Monte Carlo.
- En L1 el comprador probable es la **familia**, no el alumno (poder de compra, iPad). Afecta a mensaje y canal.

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: TAM/SAM/SOM numérico de L1, L5 y L3 + puntuación P1–P6 → borrador de `FINALISTAS.md`.
