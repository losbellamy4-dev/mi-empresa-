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

## Día 2 — 2026-11-02 (Fase 1: Investigación)

**Avances**
- Nuevo `investigacion/04_DEMANDA_COMPETENCIA.md`: competencia y precios en español de L1, L2, L3, L5, L11; primer TAM/SAM/SOM de L1 con datos del Ministerio (ESO 2,09 M + Bachillerato 0,70 M alumnos en 2024-25).
- SOM conservador de L1: 40–280 compradores en 12 meses → 240–1.700 € netos. El umbral de 500 € es alcanzable **solo con un canal de tráfico** (redes de estudio, boca a boca).
- Edad mínima: Etsy permite 13–17 a través de una cuenta registrada por el tutor (verificado en su centro de ayuda). Gumroad: fuentes contradictorias. Payhip: sin dato → asumir cuenta del adulto.

**Decisiones**
- **L10 (Minecraft) descartada**: vender contenido fuera del Marketplace oficial es arriesgado y Mojang puede retirar permisos.
- L7 (generador de horarios) y L8 (ebook) se fusionan con L1 como "kit de estudio" (L7 = imán de tráfico gratis).
- L2 (finanzas) y L11 (flashcards PAU) bajan: sin ventaja del dueño / riesgo de errores de contenido.

**Aprendizaje honesto**
- Riesgo nuevo en L1: el usuario es menor y casi nunca tiene tarjeta → paga el padre/madre. Hay que convencer a dos personas.
- El sustituto real de un planner digital es la agenda en papel (3–25 €) que muchos centros ya entregan.
- Sin herramientas de volumen de búsqueda, la demanda es cualitativa; el simulador marcará el tráfico como supuesto.

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: buscar una 3.ª finalista más fuerte (recursos en español para colegios bilingües de EE. UU.; plantillas Canva por sector) y puntuar P1–P6 todas las ideas vivas.
