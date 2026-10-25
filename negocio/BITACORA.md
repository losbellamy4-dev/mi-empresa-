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

## Día 2 — 2026-10-25 (Fase 1: Investigación)

**Avances**
- `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: edad mínima por plataforma, tamaño de mercado oficial (ESO 2.089.403 y Bachillerato 704.256 alumnos, curso 2024-25), demanda y competencia de 6 ideas, puntuación preliminar y anexo de canales de tráfico.
- **Etsy (fuente oficial):** de 13 a 17 años se puede vender solo mediante la cuenta del padre/madre/tutor. Confirma el diseño de "todo a nombre del adulto".
- **L10 (Minecraft) descartada**: no hay vía limpia de monetización, y un servidor tiene costes y exige moderar.
- L13 (Notion) y L8 (ebook) se integran en L1 como formatos o bonus. L7 (generador de horarios) se modela como **canal de tráfico** de L1.
- **Simulador:** primer esqueleto en `simulador/embudo.py` (solo biblioteca estándar), con 3 escenarios, Monte Carlo de 5.000 corridas y sensibilidad. Resultados en `simulador/resultados/embudo_generico_dia2.json`.

**Resultado del simulador (genérico y provisional, no calibrado a ninguna idea)**
- Pesimista 4 €, base 129 €, optimista 1.465 € netos en 7 meses. P(≥ 500 €) ≈ **6 %**.
- La sensibilidad dice que lo que más mueve el resultado son las **visitas** (0,66) y la **conversión** (0,50), por encima del precio (0,31).
- **Aprendizaje:** un producto de 4–10 € sin un canal de tráfico propio **no llega** a 500 € en el modelo. Hay que subir el ticket (bundles de 12–20 €, packs para docentes o negocios) y/o asegurar un canal que traiga más de 1.000 visitas al mes. Esto cambia qué buscar en las finalistas.

**Puntuación preliminar:** L1 3,85 · L5 3,00 · L3 3,00 · L11 2,40 · L2 2,25.

**Bloqueos:** ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana:** buscar 2–3 ideas o variantes con ticket más alto o con canal propio. Medir el tráfico realista de Etsy y Pinterest para una tienda nueva.
