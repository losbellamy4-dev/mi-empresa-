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

## Día 2 — 2026-11-15 (Fase 1: Investigación)

**Nota:** la sesión anterior fue el 2026-10-19; han pasado ~4 semanas sin ejecución (la tarea no corrió o no quedó registro). Se retoma sin pérdida de estado.

**Avances**
- Nuevo `investigacion/04_DEMANDA_COMPETENCIA.md`: competencia, precios y sustitutos gratuitos de L1, L2, L3, L5, L7, L11 y nueva L13.
- Datos oficiales de mercado: ESO 2.089.403 alumnos, Bachillerato 704.256, Primaria 2.707.302 (curso 2024-25, La Moncloa).
- Edad mínima Etsy verificada en fuente oficial: titular 18+; 13–17 solo con cuenta del tutor.
- Tabla de "ventas necesarias para 500 €" por precio: a 6 € hacen falta ~96 ventas (~9.600 visitas al 1 %); a 1,5 € serían ~460 ventas.

**Decisiones**
- **L10 (Minecraft) descartada**: según fuentes secundarias no se puede cobrar por mapas/mods fuera del Marketplace oficial. Fuente primaria caída hoy (503).
- **L13 añadida** (kit para opositores). Corrección hecha en la misma sesión: el "pack premium" de Opositatest es gratuito y los opotrackers de pago cuestan 0,80–1,50 €, así que el producto básico apenas vale nada; solo sirve una versión "pro" clara.
- **L2 y L3 bajan** (mucho material gratis de calidad; Orientación Andújar domina Primaria a 1–5 €).
- Nueva restricción para las finalistas: **precio ≥6 € o bundle**.

**Aprendizaje honesto**
- En casi todos los nichos el mayor rival es el **material gratis** de quien lo usa para captar clientes (academias, webs de docentes). El hueco tiene que ser de formato/calidad/especificidad, no solo de "existir en español".

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: buscar señales de volumen de búsqueda y de disposición a pagar para L1 y L13 (versión pro); luego TAM/SAM/SOM y matriz de puntuación.
