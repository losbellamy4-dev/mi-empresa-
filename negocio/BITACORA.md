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

## Día 2 — 2026-11-10 (Fase 1: Investigación)

*(Nota: entre el día 1, 19-oct, y hoy no hubo sesiones registradas.)*

**Avances**
- `investigacion/04_DEMANDA_COMPETENCIA.md`: señales de demanda, competencia y precios para L1, L2, L3, L5, L7, L11; tamaño bruto del mercado escolar (ESO 2,09 M, Bachillerato 0,70 M, 806 k docentes).
- Edad mínima verificada en términos oficiales: Etsy (18+, menores vía cuenta del tutor), Gumroad (mayoría de edad contractual), Payhip (depende de PayPal/Stripe). Confirma: todo a nombre del adulto.
- Ranking provisional: L1 Kit de estudio ESO 3,30 · L5 Canva negocios locales 3,25 · L3 imprimibles 2,70.

**Decisiones**
- L10 (Minecraft) descartada por riesgo de EULA.
- L2 (finanzas) y L11 (Anki EBAU) aparcadas: demasiada oferta gratuita / baja disposición a pagar (Wuolah: la mayoría gana 30–40 €/año).
- L7 (herramienta web) y L8 (ebook) fusionadas en L1 como imán de tráfico y bonus.

**Aprendizaje honesto**
- En español casi toda la oferta escolar se dirige al **docente**, no al alumno → hueco para L1, pero con el problema de que el alumno no tiene tarjeta (ticket bajo, ~72 ventas para 500 €).
- L5 necesita muchas menos ventas (~20–40) porque compra un adulto con tarjeta y el ticket es mayor; el riesgo es la saturación si no se elige bien el nicho.

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: L5 — elegir nicho concreto con datos de DIRCE/INE y competencia en Etsy en español; verificar licencia de Canva para vender plantillas.
