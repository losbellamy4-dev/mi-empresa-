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

## Día 2 — 2026-11-23 (Fase 1: Investigación)

*(Nota: la sesión anterior fue el 2026-10-19; la tarea no se ha ejecutado a diario.)*

**Avances**
- `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: demanda y competencia de L1, L2, L3, L5, L7, L8, L10, L11, con fuentes.
- `investigacion/05_TAM_SAM_SOM_L1.md`: TAM ≈ 2,79 M alumnos de ESO+Bachillerato (dato oficial 2024-25); SAM 56k–140k [E]; SOM 30–350 compradores [E]. Harían falta ~85 ventas a ~6 € netos para llegar a 500 €.
- `02_PLATAFORMAS_Y_COSTES.md`: verificado que Etsy permite a menores de 13–17 vender **solo** con cuenta, nombre, email y pagos a nombre del tutor. Tarifas nuevas de TpT (1-oct-2026).
- `03_LISTA_LARGA.md` actualizado.

**Decisiones**
- **L10 descartada**: el EULA de Minecraft prohíbe el uso comercial de contenido de Mojang sin permiso.
- **L7, L8 y L11 pasan a ser componentes de L1**: herramienta gratis de horarios para atraer tráfico, guía de técnicas de estudio como bonus y fichas de repaso de ESO.
- Hueco detectado: la oferta de planners en español está pensada para Latinoamérica y universitarios. No encontré productos adaptados al sistema español (evaluaciones, recuperaciones, EBAU, ESO 1º–4º).

**Aprendizaje honesto**
- Sin herramientas de volumen de búsqueda, la demanda se ha medido de forma indirecta (oferta existente, ventas visibles). Es una limitación y queda documentada.
- En todas las categorías hay mucha competencia gratuita. El producto de pago necesita una razón clara para existir: adaptación al sistema español y que esté listo para usar.

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: puntuar formalmente las 4 ideas vivas (P1–P6) en `06_PUNTUACION.md`, después redactar `FINALISTAS.md` con la recomendación y abrir la decisión para el humano.
