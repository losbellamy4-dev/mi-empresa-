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

## Día 2 — 2026-11-08 (Fase 1: Investigación)

*(Nota: entre el día 1 (19-oct) y hoy no hubo sesiones registradas; se retoma donde se dejó.)*

**Avances**
- `investigacion/04_DEMANDA_COMPETENCIA.md`: demanda y competencia en español para L1, L2, L3, L5, L7, L11, más TAM/SAM/SOM estimado de L1 (TAM ≈ 1,7 M estudiantes de 3º-4º ESO + Bachillerato; SOM 12 meses ≈ 20–250 compradores [E]).
- `02_PLATAFORMAS_Y_COSTES.md`: edad verificada — **Etsy** (titular ≥18; 13–17 solo con cuenta, datos y finanzas del adulto) y **Gumroad** (≥13 y capacidad legal para contratar → adulto).
- `03_LISTA_LARGA.md`: **L10 descartada** (EULA Minecraft: venta solo por el Marketplace oficial con licencia de empresa). Añadida **L13** (overlays/alertas para streamers en español).
- `05_PUNTUACION_PRELIMINAR.md`: L1 3,80 · L13 3,40 · L5 2,90 · L2 2,90 · L11 2,75 · L3 2,50.
- `simulador/prototipo_embudo.py` (preparación de Fase 2): embudo multicanal + Monte Carlo + sensibilidad. **Ejecutado.** Resultados en `simulador/resultados/prototipo_L1_dia2*.json`.

**Resultado del prototipo (L1, supuestos preliminares, NO garantía)**
| Escenario | P10 | P50 | P90 | P(≥500 €) |
|---|---|---|---|---|
| Producto 4–9 €, 7 meses | 42 € | 182 € | 476 € | ~9 % |
| Pack 9–16 €, 7 meses | 97 € | 380 € | 964 € | ~37 % |
| Producto 4–9 €, 12 meses | 68 € | 293 € | 787 € | ~26 % |
| Pack 9–16 €, 12 meses | 157 € | 615 € | 1.580 € | ~59 % |
Variables que más mueven el resultado: tráfico de Pinterest, conversión, tráfico SEO, tráfico Etsy. Las redes del propio menor apenas cuentan.

**Decisiones / aprendizajes**
- Patrón general: casi todo nicho tiene mucho material **gratis**; se paga especificidad + confianza en el autor. L2, L3 y L11 bajan porque un alumno de 14 años no es autor creíble para ese comprador.
- ⚠️ **Riesgo nuevo:** TikTok pone las cuentas de 13–15 años en privado por defecto y sin sugerencias → el canal "studytok" del propio dueño casi no sirve. Canales a priorizar: Pinterest, SEO con herramienta gratuita (L7), Etsy; o cuenta de marca a nombre del adulto.
- Un producto único de ~6 € casi seguro **no** llega a 500 € con supuestos conservadores; hace falta **pack de mayor precio** o **línea de productos** y ≥12 meses de venta.

**Bloqueos**: ninguno. Nada requiere al humano todavía.

**Primera tarea de mañana**: buscar la 3ª finalista (fichas/flashcards de ESO hechas por un alumno; finanzas para adolescentes) y profundizar L13 (competencia en español, edad mínima de Twitch).
