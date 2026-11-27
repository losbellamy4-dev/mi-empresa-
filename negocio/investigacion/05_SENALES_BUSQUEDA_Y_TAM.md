# Señales de búsqueda y primer TAM/SAM/SOM (Día 3, 2026-10-21)

**[V]** = fuente oficial · **[S]** = fuente secundaria · **[E]** = estimación mía · **[M]** = medido por mí hoy.

## 1. Método: autocompletado de Google como proxy de demanda

Sigo sin acceso a Keyword Planner ni a Google Trends. **Alternativa usada:** el autocompletado público de Google (`suggestqueries.google.com`, `hl=es`, `gl=es`). Google solo sugiere consultas que tienen un volumen mínimo de búsquedas, así que:
- **Aparece en el autocompletado** → hay demanda recurrente (no sabemos cuánta).
- **No aparece nada** → volumen muy bajo, probablemente < ~100 búsquedas/mes [E].

Es una señal **ordinal** (sí/no, más/menos), no un volumen. Script reproducible: `datos/autocompletado.py`; salida bruta: `datos/autocompletado_2026-10-21.json`. Nota: el parámetro `gl=mx` devolvió lo mismo que `gl=es`, así que esto no separa España de Latinoamérica.

## 2. Resultados [M]

### L5: plantillas Canva para negocios locales
| Consulta | ¿Sugiere? | Lectura |
|---|---|---|
| "plantillas instagram peluquería / restaurante / estética / fisioterapia / gimnasio / academia / psicólogo / tienda de ropa" | **No, en ningún caso** | Los oficios concretos casi no se buscan con esa forma |
| "plantillas canva para …" | Sí: **inmobiliarias**, psicólogos, restaurante, iglesias, negocios, empresas | Solo algunos verticales tienen búsqueda propia |
| "plantillas inmobiliarias …" | Sí, 10 variantes: "para redes sociales", "canva", "para instagram", "gratis" | **El vertical inmobiliario es el único con demanda clara y repetida** |
| "plantillas para estética" | Sí: "promociones estéticas de belleza", "publicidad de estética", "medicina estética" | Segundo vertical con señal |
| "ideas de post para …" | Sí: restaurantes, uñas | Demanda de **ideas/calendario**, no solo de diseño |
| "plantillas para redes sociales" | Sí, pero dominado por "gratis", "freepik", "canva" | El público genérico busca gratis |

**Conclusión L5 [E]:** la idea genérica "plantillas por oficio" **no tiene tráfico de búsqueda**. Hay que estrecharla a un vertical con señal. **Inmobiliarias** es el más fuerte: mercado identificable y con dinero, y el agente inmobiliario publica muchos anuncios de pisos en Instagram. Estética/uñas es el segundo.

### L1 + L7: planners de estudio para estudiantes
| Consulta | ¿Sugiere? | Lectura |
|---|---|---|
| "planner estudiante" | Sí: "pdf", "2026", "gratis", "semanal" | Hay demanda, muy orientada a lo gratis |
| "planner goodnotes" | Sí, 10 variantes, casi todas "gratis/free" | Igual |
| "plantilla horario de estudio" | Sí: "pdf", **"selectividad"**, **"oposiciones"**, "semanal", "excel" | Hay demanda para L7 (generador) |
| "organizador de estudio" | Sí: **"oposiciones"**, "ia", "online", "app", "universitarios" | Aparece la intención de herramienta (L7) |
| "plantillas para estudiar" | Sí: **"oposiciones"**, inglés, anatomía | |
| "agenda para estudiantes" | Sí: derecho, medicina, enfermería, universitarios, **secundaria** | Los universitarios dominan |

**Conclusión L1 [E]:** hay demanda, pero sesgada a "gratis". Un planner gratis como imán más una versión de pago es el modelo coherente. **Hallazgo nuevo:** "oposiciones" aparece en 3 de 5 familias de búsqueda de estudio.

## 3. Idea nueva: L13, planificador de estudio para opositores

Detectada hoy por las búsquedas. Pasa el filtro F1–F8 (lo detallo abajo).

- **Comprador:** un adulto con dinero que ya gasta en preparación (academias, test). Necesidad intensa y larga (estudian 1–3 años) y muy organizada por temas, lo que encaja con una herramienta.
- **Mercado [S]:** solo en la convocatoria estatal de 2025 (AGE) hubo **más de 150.000 inscritos** para 17.266 plazas: más de 60.000 en Administrativo y más de 50.000 en Auxiliar ([CSIF](https://www.csif.es/eu/noticia/portada/aragonadministraciongeneraldelestado/articulo/91256)). La Guardia Civil tuvo **28.437** aspirantes para 2.030 plazas ([digitaldeleon](https://digitaldeleon.com/nacional/mas-de-28-000-aspirantes-participaron-en-la-oposicion-de-la-guardia-civil)). A eso se suman docentes, sanidad, autonómicas y locales. Una encuesta de OpositaTest habla de más de 12 M de personas que "han opositado o se lo plantean" ([OpositaTest](https://blog.opositatest.com/?p=94808)), cifra inflada y no útil para el SAM.
- **Competencia y precios [S]:**
  - Planificador Oposiciones en Notion (Carlysh Teacher): **5 €** ([gumroad](https://carlyshteacher.gumroad.com/l/opoplan))
  - Planificador Excel de repasos espaciados "Oposiciones 2026": **3,99 €** en oferta ([payhip](https://payhip.com/b/ihdmv))
  - RindeOpos: plantilla Notion y kit de arranque, sin precio visible ([gumroad](https://rindeopos.gumroad.com))
  - **Redopositor "Planificador Pro"**: generador de cronograma + 20 plantillas, **49 € precio fundador / 79 €** ([redopositor](https://redopositor.com/productos/planificador-pro/))
  - Hay oferta, pero poca y dispersa. El tramo de 10–20 € (herramienta completa sin ser curso) parece poco cubierto [E].
- **Ambigüedad a vigilar:** "plantilla oposiciones guardia civil / seguridad social" se refiere casi seguro a la **plantilla de respuestas** del examen, no a un planner. No cuento esas búsquedas como demanda.
- **F8 (credibilidad):** un planificador es una herramienta y **no requiere ser experto en el temario** (no se vende contenido de temas ni se promete aprobar). Riesgo: el canal de contenido es menos natural para un chico de 14 años que en L1. Debe venderse como herramienta, no como consejo.
- **Sinergia:** el mismo motor que L7 (generador de horario) sirve para estudiantes (L1) y opositores (L13): **un producto, dos públicos**. Opositores pagan más; estudiantes aportan tráfico y el canal propio del dueño.

## 4. TAM / SAM / SOM, primera versión (todo el SAM/SOM es [E] conservador)

Neto por venta en web propia (Payhip 5 % + pasarela ~2,9 % + 0,30 €, sin IVA 21 %), con la misma fórmula que el Día 2: 7 € → 5,08 € · 12 € → ~8,83 € · 15 € → 11,17 €.

| Idea | TAM (personas o empresas) | SAM (alcanzables y con propensión a pagar) | SOM en 7–12 meses (recién llegado) | Ingreso SOM |
|---|---|---|---|---|
| **L5 inmobiliarias** | 60.683 empresas inmobiliarias por cuenta de terceros, ene-2025 [S] ([vivara](https://www.vivara.io/en/blog/operaciones/boom-inmobiliarias-2025-oportunidad/)) + Latinoamérica sin cuantificar | × 55 % que usa redes [S] (IONOS/YouGov, pymes) × 30 % que pagaría por plantillas [E] ≈ **10.000** | 0,1–0,5 % del SAM = **10–50 compras** a 15 € | **112–559 €** |
| **L1 + L7 estudiantes** | 2,79 M de alumnos de ESO y Bachillerato [V] | × 5 % que usa planner digital y pagaría (o lo pagan sus padres) [E] ≈ **140.000** | 0,01–0,05 % = **14–70 compras** a 7 € | **71–355 €** |
| **L13 opositores** | ≥ 300.000 opositores activos/año [E] (solo la AGE suma más de 150.000 [S]) | × 10 % que usa herramientas digitales de planificación y pagaría [E] ≈ **30.000** | 0,1–0,3 % = **30–90 compras** a 12 € | **265–795 €** |

**Lectura honesta:**
- Ninguna idea llega a 500 € con certeza ni en su rango bajo. Las tres dependen sobre todo de la **tasa de captura** (SOM %), que es justo lo que hay que modelar en el simulador con distribución y no con un número fijo.
- **L13 y L5 tienen el mejor rango; L1 sola no llega**, pero aporta tráfico y canal propio. La combinación **L7 (motor gratis) → L1 (barato) + L13 (premium)** reparte riesgo.
- Los % de SAM son supuestos míos sin fuente directa. Prioridad para mañana: encontrar un dato real que sustituya alguno (p. ej., % de opositores que usan academias online o apps).

## 5. Filtro F1–F8 de L13

F1 ✅ (web estática + Payhip) · F2 ✅ · F3 ✅ · F4 ✅ · F5 ⚠️ (rango 265–795 €) · F6 ✅ (cuenta del adulto) · F7 ✅ (descarga automática) · F8 ✅/⚠️ (herramienta sí, consejo de estudio no) → **PASA**.
