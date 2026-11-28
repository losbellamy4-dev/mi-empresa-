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

## Día 2 — 2026-10-20 (Fase 1: Investigación)

**Avances**
- `investigacion/04_DEMANDA_Y_COMPETENCIA.md`: competencia y señales de demanda de L1, L2, L3, L5, L7 y L11, con fuentes.
- Datos oficiales de mercado: 2,09 M alumnos de ESO + 0,70 M de Bachillerato (2024-25); 3,31 M empresas activas en España, 1,80 M sin asalariados (INE DIRCE 2025).
- Cálculo de ventas y visitas necesarias para 500 € netos por idea (de 45 ventas/≈4.500 visitas en L5 a 196 ventas/≈20.000 visitas en productos de 4 € en Etsy).
- Edad mínima: Etsy permite vender a menores de 13–17 con la cuenta y la supervisión del tutor [V]. Gumroad, Lemon Squeezy y Payhip → cuenta del adulto.

**Decisiones**
- L10 (Minecraft) descartada por riesgo de licencia (decisión conservadora).
- L7 no se valora como negocio propio, sino como imán de tráfico gratuito para L1.
- L3 y L2 bajan de prioridad por la competencia gratuita fuerte (Orientación Andújar, Microsoft/Google).

**Aprendizaje honesto**
- El precio de referencia en español es muy bajo (0,99–5 €). El problema no es el producto, sino el **tráfico**: un ticket bajo exige 10.000–20.000 visitas. Esto favorece ideas de ticket alto (L5).
- Etsy y minecraft.net bloquearon el acceso directo; sigo sin volúmenes de búsqueda reales. Es el hueco principal para dar un SOM fiable.

**Bloqueos**: ninguno que requiera al humano.

**Primera tarea de mañana**: buscar volúmenes de búsqueda reales (Trends, autocompletado, artículos SEO) para "plantillas instagram [oficio]" y "planner estudiante"; identificar los verticales de plantillas para negocios que más venden.

---

## Día 3 — 2026-10-21 (Fase 1: Investigación)

**Avances**
- Continuidad: esta sesión arrancó con el estado del Día 1. Encontré el Día 2 en otra rama (`claude/confident-tesla-lauy9y`) y lo integré. Añadí una nota de continuidad al `README.md`.
- `investigacion/05_SENALES_BUSQUEDA_Y_TAM.md`: medí demanda con el autocompletado de Google (script reproducible y datos brutos en `investigacion/datos/`).
- Primer TAM/SAM/SOM: L5-inmobiliarias 112–559 €, L1+L7 71–355 €, L13 265–795 € (SOM en 7–12 meses, supuestos conservadores marcados [E]).
- Licencia de Canva verificada: se pueden vender plantillas propias; con elementos Pro, solo como enlace de plantilla.

**Decisiones**
- **Nueva idea L13: planificador de estudio para opositores.** El comprador es un adulto con dinero, la necesidad dura años, hay competencia escasa en 10–20 € y comparte motor con L7.
- **L5 se estrecha a inmobiliarias.** Ninguna búsqueda "plantillas instagram [oficio]" tiene autocompletado; "plantillas inmobiliarias" tiene 10 variantes.

**Aprendizaje honesto**
- La demanda de estudiantes está muy orientada a "gratis": encaja mejor como imán de tráfico que como fuente de ingresos.
- Ninguna idea llega a 500 € en su rango bajo. El parámetro decisivo será la tasa de captura, y el simulador debe tratarla como distribución.

**Bloqueos**: ninguno que requiera al humano.

**Primera tarea de mañana**: buscar datos reales para los % de SAM (uso de herramientas digitales entre opositores, inmobiliarias en Instagram) y hacer la puntuación formal P1–P6 de las tres candidatas.

---

## Día 4 — 2026-10-23 (Fase 1 → cierre; esperando elección)

**Avances**
- Continuidad: arrancó con el estado del Día 1; integré el Día 3 (`ise0l1`, que ya contenía el Día 2) por fast-forward.
- Datos reales de opositores [S] (OpositaTest 2025/2026): la mitad prepara por libre, gasto medio de 81 €/mes, el 52 % trabaja a jornada completa, el 84 % hace test online y el 27 % usa IA.
- Competencia de L13: el kit de PreparaOposiciones es **gratis** (cebo para una suscripción), OpoPlan de OpositApp es freemium y Redopositor cuesta 49–79 €. El hueco está en una herramienta de 12–19 € sin suscripción.
- Competencia de L5-inmobiliarias: pack de 21 posts a 12 $ en Gumroad, kits en Etsy de 11–46 €, plantillas gratis de Canva y SocialPilot. No encontré ningún dato sectorial de uso de redes.
- **`investigacion/FINALISTAS.md` v1**: A opositores 3,50 · B inmobiliarias 3,35 · C estudiantes 3,05. Recomiendo A.
- **Vista previa de simulación** (`simulador/sim_preview.py`, solo librería estándar): P(≥ 500 € en 12 meses) ≈ A 42 % · B 35 % · C 23 %. **Las tres medianas quedan por debajo de 500 €.**

**Decisiones**
- Se cumple el criterio de salida de Fase 1 → 🔴 decisión pendiente del humano (`🔴_ACCION_REQUERIDA.md`). No se bloquea: la Fase 2 se prepara en paralelo.
- El SAM de L13 baja de 30.000 a 15.000–45.000 al descontar a quienes ya tienen el plan de su academia.

**Aprendizaje honesto**
- Con supuestos razonables, lo más probable es **no** llegar a 500 €. El tráfico es la variable dominante. La Fase 2 debe acotarla con datos, y el producto tiene que diseñarse para conseguir tráfico (generador gratis, SEO), no solo para vender.

**Bloqueos**: elección de idea (🔴 humano). No impide trabajar.

- Extra: `investigacion/06_BENCHMARKS_FASE2.md` con conversión en Etsy (1–3 %), embudo gratis→pago (≈0,35 % de visita a pago) y retraso del SEO (4–6 meses). **La vista previa probablemente sobreestima A y C**: lo corregirá el simulador de Fase 2.

**Primera tarea de mañana**: comprobar `RESPUESTA_HUMANO.md` en todas las ramas; si no hay, escribir `modelo/modelo.md` (embudo de dos etapas y retraso SEO) para las tres ideas.

---

## Día 5 — 2026-10-25 (Fase 2: modelo y simulador · elección pendiente)

**Avances**
- Continuidad: la sesión arrancó otra vez desde el Día 1. Integré el Día 4 (`fnmjjw`) por fast-forward. `odi82r` y `kmq0em` son Días 2 duplicados de otras sesiones y los descarté. No hay `RESPUESTA_HUMANO.md` en ninguna rama.
- `investigacion/07_BENCHMARKS_TRAFICO.md`: CTR por posición (la 1.ª bajó al ≈ 19 % por los resúmenes de IA), anécdotas de Pinterest y de tiendas Etsy nuevas (≈ 380 visitas/mes y 1,5 % de conversión en un caso).
- `modelo/modelo.md` v1: tres canales (SEO con retraso de 3–6 meses, redes del dueño con abandono, Etsy), embudo de dos etapas, estacionalidad, comisiones e IVA.
- `simulador/simulador.py` (Python estándar): escenarios, Monte Carlo de 20.000 corridas, tornado, correlación de rangos y gráficas SVG en `simulador/resultados/`. Tarda unos 4 s.
- `modelo/VEREDICTO.md` v1 (provisional).

**Resultados (estimaciones, no garantías)**
- P(≥ 500 € en 12 meses): **A 22 % · B 39 % · C 9 %**. Caso base: A 151 €, B 262 €, C 79 €. **Ninguna idea llega en el caso base.**
- Primera corrida: B 55 % frente a A 7 %, pero la comparación no era justa (A no tenía canal Etsy y el rango de Etsy de B era alto). Corregido: A con Etsy y el rango de B bajado a 20–800 visitas/mes.

**Decisiones**
- La recomendación cambia de A a **B**, aunque A sigue siendo una alternativa razonable. Actualizado el 🔴.
- Según la regla de la Fase 2, toca **ajustar la idea** antes de construir, no avanzar a la Fase 3.

**Aprendizaje honesto**
- La vista previa del Día 4 sobreestimaba A por el doble. El canal que da ventas pronto (Etsy) pesa más que el SEO en un horizonte de 12 meses.

**Bloqueos**: elección de idea (🔴 humano). Recomendado: cambiar la rama por defecto del repo para que cada sesión arranque con el último estado.

**Primera tarea de mañana**: simular los ajustes (ticket más alto, catálogo A+B, producto escalera en Etsy) y escribir el VEREDICTO v2.

---

## Día 6 — 2026-10-27 (Fase 2: ajustes de idea · elección pendiente)

**Avances**
- Continuidad: la sesión volvió a arrancar en el Día 1. Integré el Día 5 (`bb8zsu`) en `wrrkun` por fast-forward. `nksbhx` (26-oct) es otro Día 2 duplicado, el tercero. No hay `RESPUESTA_HUMANO.md` en ninguna rama.
- `simulador.py`: ganchos opcionales de elasticidad precio-conversión, nivel premium y escalera en Etsy. Comprobado que, sin ellos, los resultados de v1 salen idénticos.
- `simulador/ajustes.py`: 8 variantes de A/B y dos catálogos (A+B y B en dos sectores), cada uno con cota independiente y cota correlacionada.
- `investigacion/08_BENCHMARKS_AJUSTES.md`: elasticidad, tripwire/upsell y entrega y licencia de plantillas de Canva en Etsy. Todas las fuentes son de proveedores, así que se usaron por su lado conservador.
- `modelo/modelo.md` §7 y `modelo/VEREDICTO.md` v2.

**Resultados (estimaciones, no garantías)**
- Subir el precio único **empeora** el resultado: A 22 → 18 %, B 39 → 29 %. La escalera de 4 € también: B 39 → 27 %, porque canibaliza el pack.
- El nivel premium ayuda poco: B 39 → **43 %**, A 22 → 25 %.
- Un catálogo de dos productos roza el umbral. **B en dos sectores:** caso base 452 €, mediana MC 615 €, **P(≥ 500 €) 58 %** (correl.) / 69 % (indep.). A + B: 62 % / 72 %, pero con mucho más trabajo.

**Decisiones**
- La recomendación se concreta: **B como catálogo por sectores** (primero inmobiliarias, luego un segundo sector), con precios de 17 € y 29 €. Actualizado el 🔴.
- Veredicto v2: un producto suelto no pasa; el catálogo pasa por poco en la mediana del Monte Carlo, aunque no en el escenario base determinista. Se puede preparar la Fase 3 con esa condición, en cuanto el humano elija.

**Aprendizaje honesto**
- La palanca no es el precio, sino **tener más oportunidades de tráfico** (más productos de nicho). El riesgo que el modelo no ve es el doble trabajo de mantener dos productos.

**Bloqueos**: elección de idea (🔴 humano). La rama por defecto sigue en el Día 1 y provoca sesiones duplicadas (🔴, recomendado).

**Primera tarea de mañana**: acotar `etsy_max` de B con datos gratuitos (autocompletado de Etsy, nº de anuncios y reseñas) y elegir con datos el segundo sector.

---

## Día 7 — 2026-10-29 (Fase 2: acotar el canal Etsy · elección pendiente)

**Avances**
- Continuidad: otra vez se arrancó en el Día 1. Integré `wrrkun` (Día 6) en `e2k4ce` por fast-forward. `smd1j5` (28-oct) es el cuarto Día 2 duplicado. No hay `RESPUESTA_HUMANO.md` en ninguna rama.
- Etsy bloquea la consulta automática (403 y captcha): no se pudieron contar anuncios ni reseñas. Recurrí a señales indirectas.
- `investigacion/09_ETSY_Y_SEGUNDO_SECTOR.md`: en las búsquedas en español no aparece Etsy, solo Canva gratis, Hotmart y Gumroad. Etsy en inglés está saturado. Tamaños de sector: 60.683 inmobiliarias, 47.396 psicólogos sanitarios, ≈ 72.300 peluquerías y centros de estética.
- Autocompletado de 35 consultas en `investigacion/datos/autocompletado_2026-10-29*.json`.
- `simulador/dia7.py`: tres rangos de Etsy y tornado del catálogo BB. `modelo/VEREDICTO.md` v3.

**Resultados (estimaciones, no garantías)**
- Con Etsy conservador (10–400): **B 43 → 28 %**, **BB 58 → 42 %** (base 275 €, mediana 408 €). Con la prueba de estrés (5–200), BB baja al 29 %.
- Tornado BB: `etsy_max` (141–843 €) > `seo_max` > `p_etsy` > `p_directa`.

**Decisiones**
- El 2.º sector de B es **psicólogos** (búsquedas explícitas de "plantillas canva para psicologos", poca competencia en español y precios de unos 30 $), con fisioterapia en reserva. Descartados estética (Hotmart saturado y barato) y restaurantes (casi todo "gratis" y otro producto).
- Veredicto v3: **NO**. Antes de la Fase 3 hay que ajustar el **canal**.

**Aprendizaje honesto**
- El Día 6 rozaba el umbral solo porque suponía mucho tráfico en Etsy. Al acotarlo con lo que se sabe, el negocio vuelve a quedarse por debajo. Mejor descubrirlo ahora que tras meses construyendo.

**Bloqueos**: elección de idea (🔴). Rama por defecto aún en el Día 1 (🔴 urgente: 4 sesiones perdidas).

**Primera tarea de mañana**: investigar Hotmart como canal (comisiones, titular adulto, tráfico del marketplace) y Etsy en inglés; añadirlos al simulador y compararlos con BB v3.

---

## Día 8 — 2026-11-12 (Fase 2: ajuste de canal · elección pendiente)

**Avances**
- Continuidad: **del 30-oct al 11-nov, 14 sesiones** arrancaron desde el Día 1 y rehicieron el Día 2 (ramas 5nedo3, mrt3hf, 10ufax, v0nom2, 75rio6, mlwmb4, a9xscj, 39cwu6, sozpm1, ws1gcz, afawuz, 6vnqfh, q1wsc1 y otras). Integré `e2k4ce` (Día 7) en `2loft6` por fast-forward. No hay `RESPUESTA_HUMANO.md` en ninguna rama. Aviso enviado al dueño.
- `investigacion/10_CANALES_HOTMART_ETSY_EN.md`: Hotmart cobra 9,9 % + 1,00 € (desde 21-sep-2026), exige titular 18+ y no publica datos de tráfico orgánico; es un canal de afiliados. Etsy-EN: mercado grande; una tienda nueva de 2026 para agentes inmobiliarios muestra 24 ventas en 3 meses.
- `simulador.py`: canal de marketplace configurable (`mkt="hotmart"`, con fracción de ventas por afiliados). Comprobado que los casos base de v3 salen idénticos (303/452/185 €).
- `simulador/dia8.py`: 8 combinaciones de canal + tornado. `modelo/VEREDICTO.md` v4.

**Resultados (estimaciones, no garantías)**
- BB con Etsy-ES (ref.): 42 %. Hotmart en su lugar: 32 %. Etsy-ES + Hotmart: 50 %.
- **BB + inmobiliarias en Etsy-EN: 66 %, base 603 €, mediana 789 €.** Todo junto: 68 %. Estrés Etsy-EN (10–500): 52 %, base 375 €.

**Decisiones**
- Veredicto v4: **SÍ condicionado**. Recomendación de canal: web ES (Payhip) + Etsy con anuncios ES/EN. Hotmart, opcional y más tarde.
- Condición para la Fase 3: validar Etsy-EN con pocos anuncios antes de construir todo el catálogo.

**Aprendizaje honesto**
- Lo que cambia el resultado no es el producto ni el precio, sino **ir a donde ya están los compradores** (Etsy en inglés). Pero el supuesto se apoya en un único caso visible, y por eso la prueba de estrés baja al 52 %.

**Bloqueos**: elección de idea (🔴). Rama por defecto aún en el Día 1 (🔴 urgente: ya son 18 sesiones perdidas).

**Primera tarea de mañana**: plan de validación de Etsy-EN (anuncios, métricas y umbral de corte), lista de las 10 plantillas del pack inmobiliarias ES/EN y esqueleto de la web en `/negocio/web/`.

---

## Día 9 — 2026-11-16 (Fase 2→3: preparar la validación · elección pendiente)

**Avances**
- Continuidad: esta sesión volvió a arrancar en el Día 1. Integré `2loft6` (Día 8) en `9sf6u8` por fast-forward. El 13, 14 y 15 de noviembre hubo **3 Días 2 duplicados más** (`uph903`, `1zg9sz`, `lfcc0k`): ya son **21 sesiones perdidas**. No hay `RESPUESTA_HUMANO.md` en ninguna rama.
- Nuevo: abrí un **PR borrador de esta rama hacia la rama por defecto**. Si se fusiona (un clic), las próximas sesiones arrancarán desde aquí.
- `simulador/dia9.py` → `resultados/dia9.md`: barrido del techo de visitas de Etsy-EN (V) para el catálogo BB+EN.
- `investigacion/11_PLAN_VALIDACION_ETSY_EN.md`: 5 anuncios en inglés (≈ 1 $), métricas cada 2 semanas y regla de decisión en el mes 2.
- `investigacion/12_ESPEC_PACK_INMOBILIARIAS.md`: las 10 plantillas (≈ 38 diseños por idioma), el pack agencia y el orden de construcción.
- `web/`: esqueleto v0 de la landing (index + borrador legal), adaptado a móvil y modo oscuro, con los botones de compra desactivados (🔴).

**Resultados (estimaciones, no garantías)**
- P(≥ 500 €) del catálogo BB+EN: 42 % con V = 10, **52 % con V = 75**, **65 % con V = 150** (caso base 501 €), 83 % con V = 300.
- Regla: con ≥ 130 visitas de los 5 anuncios en el mes 2 → seguir; 65–129 → ajustar; 25–64 → repensar canal; < 25 → Etsy-EN no aporta.

**Aprendizaje honesto**
- Revisando los resultados veo que **P(0 ventas) ≈ 0 %** en todas las combinaciones. Choca con el dato del Día 1 (el 44 % de productos de Gumroad no vende nada). El modelo probablemente da por seguro algo de tráfico de SEO y redes. Lo reviso mañana, porque podría estar inflando todas las probabilidades.

**Bloqueos**: elección de idea (🔴). La rama por defecto sigue en el Día 1 (🔴 urgente, ahora con un PR para arreglarlo en un clic).

**Primera tarea de mañana**: auditar el supuesto de P(0 ventas) (añadir un "canal muerto" con cierta probabilidad) y volver a correr dia8/dia9. Después, textos ES/EN de los 5 anuncios de prueba.

---

## Día 10 — 2026-11-17 (Fase 2: auditoría del simulador · elección pendiente)

**Avances**
- Continuidad: esta sesión también arrancó en el Día 1 (rama `2hgi05`). Integré `9sf6u8` (Día 9) por fast-forward. No hay `RESPUESTA_HUMANO.md` en ninguna rama. El PR #1 sigue abierto y sin fusionar.
- **Auditoría de P(0 ventas)** (`investigacion/13_CANAL_MUERTO.md`, `simulador/dia10.py` → `resultados/dia10.md`): cada canal (SEO, redes, Etsy-ES, Etsy-EN, Hotmart) puede quedarse en **0 visitas** con una probabilidad basada en datos (Ahrefs: 96,55 % de páginas sin tráfico de Google; Etsy: ≈ 65 % de tiendas sin ventas; Gumroad: 44 % de productos sin ventas).
- Regla de la prueba de Etsy-EN recalculada (`investigacion/11_PLAN_VALIDACION_ETSY_EN.md` §3).
- `producto/ANUNCIOS_PRUEBA.md` (+ `anuncios_prueba.py`, que comprueba los límites de Etsy): títulos, descripciones ES/EN y 13 etiquetas de los 5 anuncios de prueba.
- `modelo/VEREDICTO.md` → **v5**.

**Resultados (estimaciones, no garantías)**
- P(≥ 500 €): BB + inmobiliarias en Etsy-EN **66 % → 37 %** (mediana 784 → 300 €); BB + ambos sectores en Etsy-EN **42 %**; un solo producto **11 %** (P(0 ventas) 24 %).
- Resultado **bimodal**: si Etsy-EN arranca se suele superar 500 € con holgura; si no, casi nunca.
- Nueva regla: ≥ 260 visitas de los 5 anuncios en el mes 2 → seguir (≈ 65 %); 130–259 → ajustar; 45–129 → repensar; < 45 → volver a Fase 1.

**Decisiones**
- Veredicto v5: **NO con los supuestos actuales**, pero se puede convertir en SÍ con un dato barato (la prueba de Etsy-EN, ≈ 1 $). La prueba pasa a ser el **paso n.º 1** de la Fase 3: no se construye el catálogo completo antes de medir.
- Psicólogos también en inglés (+5 puntos).

**Aprendizaje honesto**
- El Día 9 sospeché que el modelo era optimista, y lo era: no admitía que un canal pudiera dar cero visitas. Las probabilidades de los Días 5–9 estaban infladas aproximadamente al doble. Desde hoy todo canal nuevo lleva su probabilidad de "canal muerto".

**Bloqueos**: elección de idea (🔴). La rama por defecto sigue en el Día 1 (🔴: nuevo PR desde `2hgi05`, que incluye todo).

**Primera tarea de mañana**: maquetas de referencia (SVG/HTML) de las plantillas #1–#4 para Canva; después buscar palancas que bajen la probabilidad de canal muerto del SEO.

---

## Día 11 — 2026-11-18 (Fase 2→3: maquetas · elección pendiente)

**Avances**
- Continuidad: la sesión volvió a arrancar en el Día 1 (rama `tkfnj4`) y **llegó a rehacer otro Día 2 entero** antes de que lo detectara al revisar las ramas. Integré `2hgi05` (Día 10) y anulé el duplicado. Ya van **≈ 22 sesiones perdidas**. No hay `RESPUESTA_HUMANO.md` en ninguna rama; los PR #1 y #2 siguen abiertos.
- `producto/maquetas/`: `maquetas.py` → 36 SVG (#1 A/B, #2 post/story, #3, #4 × 3 paletas × ES/EN) e `index.html` con medidas, colores hex, tipografías (Playfair Display + Montserrat) y reglas de montaje en Canva. Revisado visualmente con capturas: corregí dos desbordes de texto ("NUEVO EN CARTERA" y "UNDER CONTRACT").

**Aprendizaje honesto**
- Mientras la rama por defecto siga en el Día 1, cada sesión gasta tiempo en recuperar el estado o, peor, repite trabajo sin enterarse. Es lo que más frena el proyecto, por delante de la elección de idea.

**Bloqueos**: elección de idea (🔴, desde el Día 4). Continuidad (🔴: fusionar el PR nuevo de `tkfnj4`).

**Primera tarea de mañana**: diseños C y D de #1, carrusel #6 y los 5 mockups del anuncio de Etsy.

---

## Día 12 — 2026-11-19 (Fase 2→3: maquetas completas para la prueba · mockups de Etsy · elección pendiente)

**Avances**
- Continuidad: la sesión volvió a arrancar en el Día 1 (rama `ucgjlr`). Esta vez lo detecté **antes de trabajar** e integré `tkfnj4` (Día 11). No hay `RESPUESTA_HUMANO.md` en ninguna rama y los PR #1, #2 y #3 siguen abiertos sin fusionar.
- `producto/maquetas/`: #1 diseños **C** (dos columnas) y **D** (collage de 3 fotos), carrusel **#6** de compradores y **#6b** de vendedores (7 diapositivas cada uno; el anuncio 4 de Etsy prometía 2 carruseles y solo había uno). 132 SVG. Revisión visual: corregí un titular que tocaba el borde ("CARTERA") y las portadas de carrusel en inglés (ahora se parten en líneas).
- `producto/mockups/` (nuevo): 5 mockups del anuncio ancla #1 Just Listed en ES y EN (portada, cuadrícula de perfil, detalle en el móvil, 3 paletas, qué incluye), en PNG de 2700×2025 (4:3, con lo importante dentro del cuadrado central).
- `simulador/dia12.py` → `resultados/dia12.md`: barrido de la probabilidad de canal muerto, canal a canal. `investigacion/14_PALANCAS_CANALES.md`.

**Resultados (estimaciones, no garantías)**
- Por cada 0,1 menos de probabilidad de canal muerto, P(≥ 500 €) del catálogo `BB+2EN` sube: **Etsy-EN +4,4 pp**, Etsy-ES +1,4, SEO +1,3, redes +0,2.
- Bajar el SEO de 0,6 a 0,2, algo muy difícil según Ahrefs (solo el 2–6 % de las páginas nuevas llega al top 10 en un año), daría 42 → 48 %. Bajar Etsy-EN de 0,4 a 0,2 daría 42 → **52 %**.

**Decisiones**
- **No se invierte en SEO** más allá de lo básico. La palanca es la **calidad de los anuncios de Etsy-EN** (portada, título, etiquetas, nº de anuncios). Pinterest se usará para llevar tráfico a esos anuncios, no como canal propio.
- Descarto la tarea "palancas para bajar el p_muerto del SEO" de la cola: el modelo dice que rinde poco.

**Aprendizaje honesto**
- Medir antes de trabajar ahorró horas: la tarea que tocaba (mejorar el SEO) era la de menor rendimiento. Los mockups de hoy sí atacan el canal que más pesa.
- Los mockups llevan degradados en lugar de fotos. Para publicar en Etsy hacen falta fotos de stock reales dentro de Canva.

**Bloqueos**: elección de idea (🔴, desde el Día 4). Continuidad (🔴: fusionar un PR; hoy hay uno nuevo desde `ucgjlr`).

**Primera tarea de mañana**: buscar datos (no anécdotas) sobre qué da impresiones a un anuncio nuevo de Etsy y traducirlo al `p_muerto` de Etsy-EN; después, mockups de los anuncios 2–5.

---

## Día 13 — 2026-11-21 (Fase 2→3: cómo arranca un anuncio nuevo en Etsy · brecha de valor · elección pendiente)

**Avances**
- Continuidad: la sesión volvió a arrancar en el Día 1 (rama `sff658`). Lo detecté **antes de trabajar** e hice fast-forward a `ucgjlr` (Día 12). No hay `RESPUESTA_HUMANO.md` en ninguna rama; los PR #1–#5 siguen abiertos y la rama por defecto sigue en el Día 1.
- `investigacion/15_ETSY_NUEVOS_ANUNCIOS.md`: Etsy da a cada anuncio nuevo un **empujón corto** (horas–días, no oficial) y después lo coloca según el **Listing Quality Score** (clics, favoritos, compras). Renovar no sirve. Competencia en "real estate instagram template": ≈ 8.600 anuncios [S débil]; packs de 50–1.000+ diseños por 9–47 $.
- **Hallazgo:** nuestros anuncios de prueba dan 4 diseños por 9 $ → 10–100× menos diseños por dólar que el anuncio de al lado. Es probable que el empujón se queme sin clics.
- `simulador/dia13.py` → `resultados/dia13.md`: rejilla p_muerto de Etsy-EN × conversión de Etsy-EN para `BB+2EN`.

**Resultados (estimaciones, no garantías)**
- Oferta actual (p_muerto 0,6, conversión ×0,5): **P(≥ 500 €) ≈ 28,5 %**, mediana 187 €.
- Supuesto v5 (0,4, ×1): 41,3 % (cuadra con el Día 10).
- Pack completo como ancla (0,35, ×0,9): **43,0 %**, mediana 369 €. Corregir la brecha vale ≈ **+15 pp**.

**Decisiones**
- Cambio de plan para la prueba de Etsy-EN: el **anuncio ancla pasa a ser el pack base completo** (≈ 38 diseños × 3 paletas × ES/EN, 19–24 $); los anuncios sueltos bajan a 4–6 $ y sirven de puerta de entrada. Diferenciador: **"strategy included"** (calendario de 30 días) + versión en español.
- Consecuencia: hay que montar el pack completo en Canva **antes** de la prueba (≈ 10–15 h de Adrián [E]).

**Aprendizaje honesto**
- El supuesto v5 de Etsy-EN (p_muerto 0,4) era probablemente **optimista para la oferta que teníamos**. Con los 5 anuncios tal cual, el veredicto real estaría más cerca del 28–34 % que del 42 %.

**Bloqueos**: elección de idea (🔴, desde el Día 4). Continuidad (🔴: fusionar el PR de hoy, que incluye todo).

**Primera tarea de mañana**: rehacer `producto/ANUNCIOS_PRUEBA.md` con la oferta nueva (ancla = pack completo) y diseñar el calendario de 30 días.

---

## Día 14 — 2026-11-22 (Fase 2→3: calendario de 30 días · anuncios v2 · punto de control de los sueltos)

**Avances**
- Continuidad: la sesión volvió a arrancar en el Día 1 (rama `b5hizx`). Lo detecté **antes de trabajar** e hice fast-forward a `sff658` (Día 13). No hay `RESPUESTA_HUMANO.md` en ninguna rama; los PR #1–#6 siguen abiertos sin fusionar.
- `producto/calendario/` (nuevo): calendario de 30 días en ES y EN (HTML, PDF de 1 página A4 horizontal y CSV). Cada día dice **qué plantilla del pack** usar, el formato, el objetivo y una idea. Usa las 10 plantillas, ninguna dos días seguidos. Revisado con captura.
- `producto/ANUNCIOS_PRUEBA.md` **v2**: ancla = pack completo a **22 $**; sueltos a 5/5/4/6 $; el 5.º anuncio pasa a ser "calendario + carrusel". Todo indica "English & Spanish".
- **Corrección:** el pack base tiene **34 diseños** por idioma, no ≈ 38 (el desglose suma 34). Corregido en `12_ESPEC` y vigilado con una aserción.
- `investigacion/16_CALENDARIO_DIFERENCIADOR.md`: ya se venden calendarios para agentes en Etsy (365 días, anuales) y en Payhip (kit de 30 días ≈ 12 $). El calendario solo **no** diferencia; la combinación "calendario ligado al pack + bilingüe" parece poco común [E].
- `simulador/dia14.py` → `resultados/dia14.md` (punto de control).

**Resultados (estimaciones, no garantías)**
- Un suelto a 5 $ deja **2,80 €** netos (frente a ≈ 13,4 € del pack): las comisiones fijas de Etsy pesan mucho.
- P(≥ 500 €) de `BB+2EN`: referencia 43,0 % → **34,8–48,2 %** con la oferta v2. Si los sueltos **canibalizan** el pack, baja (41 → 35 %); si traen compradores **nuevos**, sube (47–48 %).
- Subir los sueltos a 7–8 $ cambia ±1 pp: el precio del suelto no es la palanca.

**Decisiones**
- Mantener los sueltos a 4–6 $, con texto que enseña lo que trae el pack, y **nueva regla en la prueba**: si en el mes 2 más del 50 % de las ventas son sueltos y hay ≤ 1 venta del pack → retirar los sueltos (`11_PLAN_VALIDACION_ETSY_EN.md` §6).
- Veredicto: **sigue en NO** (ningún caso llega al 50 %). Nota añadida en `modelo/VEREDICTO.md`.

**Aprendizaje honesto**
- Iba a vender "strategy included" como algo único y no lo es; buscarlo antes de escribir el título evitó una afirmación falsa. Lo mismo con el "38 diseños": los números del anuncio hay que sumarlos, no copiarlos.

**Bloqueos**: elección de idea (🔴, desde el Día 4). Continuidad (🔴: fusionar el PR de hoy, que incluye todo).

**Primera tarea de mañana**: mockups de Etsy del anuncio ancla v2 y maquetas SVG de las plantillas #5 y #7–#10 (las que faltan para que Adrián pueda montar el pack completo).

---

## Día 15 — 2026-11-23 (continuidad rota otra vez; sin avance de producto)

**Qué pasó**
- La sesión volvió a arrancar en el **Día 1** (rama por defecto `2gx72p`). Es la 7.ª vez. Esta vez **no** lo detecté al empezar: rehíce el Día 2 entero (demanda y competencia, TAM de L1, descarte de L10). Lo vi al ir a abrir el PR, porque ya había 7 PR abiertos.
- Revisé las 36 ramas: **no hay `RESPUESTA_HUMANO.md`** en ninguna. La más avanzada era `b5hizx` (Día 14).
- Anulé el Día 2 duplicado con un merge de `b5hizx` que da prioridad a esa rama. Lo único nuevo (la política de Etsy para menores, verificada) ya estaba en `02_PLATAFORMAS_Y_COSTES.md`. La rama `rzx5pl` tiene ahora el mismo contenido que `b5hizx` más esta entrada.

**Aprendizaje honesto**
- El protocolo de inicio tiene que mirar los PR abiertos y las ramas remotas **antes** de leer `ESTADO.json`. No hay que fiarse de la rama por defecto: mientras nadie fusione, cada sesión empieza con el estado del Día 1.

**Bloqueos (🔴)**: 1) fusionar el PR de hoy, o cambiar la rama por defecto; 2) elegir la idea (pendiente desde el Día 4).

**Primera tarea de mañana** (sin cambios desde el Día 14): mockups de Etsy del anuncio ancla v2 y maquetas SVG #5 y #7–#10.

---

## Día 16 — 2026-11-24 (continuidad rota otra vez, 8.ª vez; sin avance de producto)

**Qué pasó**
- La sesión volvió a arrancar en el **Día 1** (rama por defecto `2gx72p`, `ESTADO.json` con `dia_global: 2`). Igual que el Día 15, no lo detecté al empezar: rehíce el Día 2 (demanda y competencia, TAM/SAM/SOM, una versión 1 de finalistas sobre estudiantes / Canva para negocios / imprimibles, y edad mínima en Etsy y Gumroad). Lo vi al ir a abrir el PR y encontrar 8 PR abiertos.
- Comparé con `rzx5pl` (Día 15): todo lo de hoy ya estaba (licencia de Canva, INE DIRCE, edad en Etsy, descarte de L10). **Anulo el duplicado** con un merge que conserva exactamente el árbol de `rzx5pl`, más esta entrada.
- No hay `RESPUESTA_HUMANO.md` en la rama más avanzada.

**Aprendizaje honesto**
- Ya lo apunté el Día 15 y no sirvió, porque esa nota está en una rama que la sesión siguiente no lee. Desde dentro de la tarea no se puede arreglar: la rama por defecto la tiene que cambiar el humano. Por eso este aviso va también por notificación.

**Bloqueos (🔴)**: 1) cambiar la rama por defecto a `claude/confident-tesla-bc2ql2` o fusionar su PR; 2) elegir la idea (pendiente desde el Día 4).

**Primera tarea de la próxima sesión** (sin cambios desde el Día 14): antes que nada, `git ls-remote` + lista de PR abiertos y ponerse sobre la rama más avanzada; después, mockups de Etsy del anuncio ancla v2 y maquetas SVG #5 y #7–#10.

---

## Día 17 — 2026-11-25 (continuidad rota otra vez, 9.ª vez; sin avance de producto)

**Qué pasó**
- La sesión volvió a arrancar en el **Día 1** (rama por defecto `2gx72p`). Rehíce el Día 2: demanda y competencia de L1, L2, L3, L5 y L11, descarte de L10 y edad mínima en las plataformas. Lo vi al ir a abrir el PR y encontrar 9 PR abiertos.
- No hay `RESPUESTA_HUMANO.md` en ninguna de las 38 ramas. La más avanzada era `bc2ql2` (Día 16).
- **Anulo el duplicado** con un merge que conserva el árbol de `bc2ql2`. Lo único que aportaba algo nuevo eran los términos de Payhip y Lemon Squeezy leídos directamente (ninguno fija una edad explícita; Payhip depende de PayPal, que exige 18+). Lo he añadido a `02_PLATAFORMAS_Y_COSTES.md`.

**Bloqueos (🔴)**: 1) cambiar la rama por defecto a `claude/confident-tesla-dcbtqp` o fusionar su PR (y cerrar los #1–#9); 2) elegir la idea (pendiente desde el Día 4).

**Primera tarea de la próxima sesión** (sin cambios desde el Día 14): mockups de Etsy del anuncio ancla v2 y maquetas SVG #5 y #7–#10.

---

## Día 18 — 2026-11-26 (Fase 2, preparando Fase 3: pack completo en maquetas)

**Qué pasó con la continuidad**
- La sesión volvió a arrancar en el **Día 1** (10.ª vez, rama `lilbm4`). Esta vez lo detecté **al inicio** con `git fetch`: hice fast-forward a `dcbtqp` (Día 17) sin rehacer nada.
- No hay `RESPUESTA_HUMANO.md` en ninguna rama, así que la elección de idea sigue pendiente. Seguí con trabajo para B que no depende de esa decisión.

**Avances**
- `producto/maquetas/maquetas.py`: nuevas maquetas **#5 Bajada de precio (A, B), #7 Testimonio (A, B), #8 Preséntate (A, B), #9 Story de visita (3), #10 Portadas de destacadas (hoja de 12 iconos)**, y los segundos diseños que faltaban: **#2 post B, #2 story B, #3 B y #4 B**. Con esto están las **34 maquetas** que promete la especificación y el anuncio ancla de Etsy (216 SVG: 3 paletas × ES/EN). Las revisé renderizadas: corregí la línea del tachado de #5A y el texto cortado de #8B.
- `producto/maquetas/README.md`: tabla con las 34 maquetas y sus archivos. Aviso: los testimonios son de relleno y no se pueden publicar como reales.
- `web/` v1: las tarjetas usan las maquetas reales (`web/assets/`) y hay una galería de 8 diseños. La oferta dice ahora "34 diseños + calendario de 30 días", como en Etsy (antes decía "38+", que no cuadraba). Corregido el modo oscuro. Comprobada en 390 px de ancho, sin scroll horizontal.

**Aprendizaje / riesgo detectado**
- El **Pack Agencia (29 €)** de la web promete 10 posts de temporada y 3 paletas extra que no existen. No se puede vender así: hay que crearlos o quitar la tarjeta (anotado en `web/README.md`). El simulador usa el nivel de 29 € en los escenarios "niv"/catálogo, así que conviene decidirlo antes de la Fase 3.
- El simulador no se ha vuelto a correr: hoy no ha cambiado ningún parámetro (las maquetas no son el producto final de Canva).

**Bloqueos (🔴)**: 1) cambiar la rama por defecto a `claude/confident-tesla-lilbm4` (o fusionar su PR); 2) elegir la idea (pendiente desde el Día 4).

**Primera tarea de la próxima sesión**: `git fetch` y ponerse sobre la rama más avanzada. Después, mockups de Etsy del anuncio ancla v2 y guía de uso en PDF para el comprador.

---

## Día 19 — 2026-11-27 (Fase 2, preparando Fase 3: anuncio ancla y guía del comprador)

**Continuidad**
- La sesión volvió a arrancar en el **Día 1** (11.ª vez, rama `ivpvmb`). Lo detecté **al inicio** con `git fetch` e hice fast-forward a `lilbm4` (Día 18) sin rehacer nada.
- No hay `RESPUESTA_HUMANO.md` en ninguna rama. La elección de idea sigue pendiente, así que seguí con trabajo para B que no depende de esa decisión.

**Avances**
- `producto/mockups/mockups_pack.py`: **7 imágenes del anuncio ancla v2** (pack completo de 22 $), en ES y EN: portada, todo lo que incluye, calendario de 30 días, bilingüe, stories y destacadas, tres paletas y qué recibes. Las revisé renderizadas y recoloqué la portada, el calendario y las stories, que quedaban descentrados.
- `producto/guia/`: **guía del comprador en PDF (ES/EN, A4, 2 páginas)**. Lleva 5 pasos para editar en Canva, una tabla con los 10 grupos de plantillas (comprueba que suman 34) y sus enlaces, trucos, aviso de responsabilidad y licencia. Los enlaces de Canva salen como "[enlace pendiente]" hasta que Adrián monte las plantillas (🔴).
- `web/index.html`: **oculta la tarjeta del Pack Agencia (29 €)**. Prometía 10 posts de temporada y 3 paletas extra que no existen. La web queda con un solo pack (17 €), coherente con Etsy.

**Riesgo / aprendizaje**
- Al ocultar el nivel de 29 €, la web ya no es la del escenario "niv" del simulador. Los escenarios de catálogo (BB+2EN, 42 %) usaban ese nivel como empuje de ticket medio. Mañana hay que volver a correr el simulador con un solo nivel para no arrastrar una probabilidad que la oferta real ya no respalda.
- El simulador no se ha corrido hoy: los mockups y la guía no cambian ningún parámetro.

**Bloqueos (🔴)**: 1) cambiar la rama por defecto a `claude/confident-tesla-ivpvmb` (o fusionar su PR); 2) elegir la idea (pendiente desde el Día 4); 3) cuando se elija B: enlaces de Canva en la guía.

**Primera tarea de la próxima sesión**: `git fetch` y ponerse sobre la rama más avanzada. Después, volver a correr el simulador sin el Pack Agencia y anotar cuánto cambia P(≥500 €).

---

## Día 20 — 2026-11-28 (Fase 2, preparando Fase 3: oferta real en el simulador y paquete de Etsy)

**Continuidad**
- La sesión volvió a arrancar en el **Día 1** (12.ª vez, rama `npcn86`). Lo detecté al inicio con `git fetch` e hice fast-forward a `ivpvmb` (Día 19). No hay `RESPUESTA_HUMANO.md` en ninguna rama.

**Avances**
- **Punto de control del simulador** (`simulador/dia20.py` → `resultados/dia20.md`): quité el Pack Agencia (29 €) de todas las piezas, porque la web ya no lo vende. Resultados para el catálogo `BB+2EN` en el escenario `oferta_grande`:
  - con Pack Agencia (referencia del Día 13): **43,0 %**;
  - un solo nivel a 17 € en todos los canales: 39,1 %;
  - **un solo nivel con el ancla de 22 $ en Etsy-EN (la oferta real): 42,0 %**, es decir, −1,0 pp;
  - con un 30 % de ventas sueltas a 5 $: 37,7 % si sustituyen al pack y 43,4 % si son ventas extra.
- **Paquete de lanzamiento del anuncio ancla** en `entregables/paquete_etsy_anuncio1/`. Lo genera `producto/paquete_etsy.py`, que además comprueba los límites: título de 140 caracteres como máximo, 13 etiquetas de hasta 20 y hasta 5 archivos digitales de 20 MB, límite verificado en la ayuda de Etsy. Incluye:
  - textos en texto plano, en inglés y en español, para copiar y pegar;
  - `LEEME.md`, una lista de 9 pasos en orden con los 🔴 marcados;
  - `MANIFIESTO.json` con las imágenes y los PDF;
  - un `--zip` opcional (10 MB, fuera de git).
- **Incoherencia corregida**: los anuncios prometían una "guía de 1 página" y la guía tiene 2. He corregido `anuncios_prueba.py` y regenerado `ANUNCIOS_PRUEBA.md`.

**Aprendizaje**
- Que el Pack Agencia desapareciera casi no cambia la probabilidad: su efecto lo compensa el ancla de 22 $, que deja más neto por venta (13,98 € frente a 11,66 € a 17 €). El riesgo principal sigue siendo que el canal Etsy-EN arranque o no. El nivel de precios importa mucho menos.
- El veredicto sigue en **NO** con supuestos conservadores. La nueva cifra de referencia es el 42,0 %.

**Bloqueos (🔴)**:
1. Cambiar la rama por defecto a `claude/confident-tesla-npcn86`, o fusionar su PR.
2. Elegir la idea (pendiente desde el Día 4).
3. Para publicar: cuenta de Canva, enlaces en la guía, fotos de stock con licencia y cuenta de Etsy del adulto (ver la lista del paquete).

**Primera tarea de la próxima sesión**: `git fetch` y ponerse sobre la rama más avanzada. Después, especificación del pack del segundo sector (psicólogos).
