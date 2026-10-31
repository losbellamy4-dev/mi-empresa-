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

## Día 2 — 2026-10-31 (Fase 1: Investigación)

**Avances**
- `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: demanda, precios y competencia de L1, L2, L3, L5, L11; revisión del EULA de Minecraft (L10); tabla de edad mínima por plataforma.
- `investigacion/05_MERCADO_TAM_SAM_SOM.md`: datos oficiales del Ministerio (ESO 2.092.405; Bachillerato 711.651; Primaria 2.715.544 en 2024-25) y primer TAM/SAM/SOM honesto para L1.
- `03_LISTA_LARGA.md` actualizada con semáforo.

**Decisiones**
- **L10 descartada**: el EULA prohíbe monetizar contenido de Minecraft sin permiso de Mojang.
- **L1 pasa a candidata principal**: casi no hay planners de estudio en español para alumnos de ESO/Bachillerato (Etsy muestra sobre todo agendas de docentes) y los kits Notion de estudio en español se venden a 5–39 €.
- L3 y L11 bajan mucho: la competencia gratuita (Educación 3.0, Wuolah) hunde el precio.

**Aprendizaje honesto**
- Según el SOM estimado para L1 (40–150 compradores en 12 meses), llegar a 500 € netos requiere unas 65–85 ventas a 7–9 €. Es plausible, pero depende casi por completo del canal de tráfico. No he podido medir el volumen de búsqueda (no tengo Google Trends); queda como hueco de la investigación.
- Etsy confirma oficialmente que de 13 a 17 años solo se puede vender con un tutor como titular de la cuenta.

**Bloqueos**: ninguno. No hace falta nada del humano todavía.

**Primera tarea de mañana**: investigar la variante "agenda/plantillas para docentes de Secundaria en español" como posible finalista y empezar la tabla de puntuación P1–P6.
