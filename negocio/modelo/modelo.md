# Modelo del negocio — Fase 2 (v1, Día 5, 2026-10-25)

**[V]** oficial · **[S]** secundaria · **[E]** estimación mía · **[M]** medido por mí.
Las fuentes de cada rango están en `../investigacion/06_BENCHMARKS_FASE2.md` y `07_BENCHMARKS_TRAFICO.md`.
El código que implementa estas ecuaciones es `../simulador/simulador.py`.

> El modelo estima si el negocio **puede** llegar a 500 € netos y con qué probabilidad **bajo estos supuestos**. No es una predicción ni una garantía.

## 1. Horizonte y calendario
- Se simulan `H = 12` meses desde el lanzamiento (criterio F5: ≥ 500 € en ≤ 12 meses).
- Mes de lanzamiento por defecto: **junio de 2027** (después de la entrega del 15 de mayo). También se simula un lanzamiento anticipado en **febrero de 2027** para medir cuánto vale publicar antes (decisión futura del humano).
- Estacionalidad `S(mes)` [E]: multiplicador por mes del calendario (media ≈ 1). Opositores: picos en septiembre y enero, valle en agosto. Estudiantes: pico en septiembre, valle en julio y agosto. Inmobiliarias: casi plana, con un pico suave en enero y septiembre.

## 2. Tráfico (tres canales)

**SEO (Google)**, con retraso de un dominio nuevo:

    V_seo(m) = 0                                       si m <= d
    V_seo(m) = V_seo_max · (1 − exp(−(m − d)/τ))       si m > d

`d` ∈ [3, 6] meses (los primeros clics llegan en los meses 4–6 [S]); `τ` ∈ [3, 9] meses; `V_seo_max` lognormal (visitas al mes en madurez).

**Redes del dueño (TikTok, Shorts, Pinterest)**:

    V_red(m) = V_red_base · ε_m · A(m)

`ε_m` es ruido lognormal mensual (σ = 0,6; un vídeo puede funcionar o no); `A(m)` vale 1 mientras el dueño sigue publicando y 0 a partir del mes en que lo deja (probabilidad de abandono `p_aband` = 6 % al mes [E, conservador]).

**Marketplace (Etsy; solo B y, de forma secundaria, C)**: `V_etsy(m) = V_etsy_max · (1 − exp(−m/τ_etsy))`, sin retraso de SEO porque Etsy indexa en unas 48 h [S].

Visitas totales: `V(m) = S(mes) · (V_seo + V_red + V_etsy)`.

## 3. Conversión
- **A y C (embudo en dos etapas):** visita → usa el generador gratis (`p_uso`) → compra el pack (`p_compra`).
  `ventas_web(m) ~ Poisson(V_web(m) · p_uso · p_compra)`.
  Referencia: visita → registro gratis ≈ 13 %, gratis → pago ≈ 2,6 % [S] → visita → pago ≈ 0,35 %.
- **B (directa):** `ventas_web(m) ~ Poisson(V_web(m) · p_directa)`.
- **Etsy:** `ventas_etsy(m) ~ Poisson(V_etsy(m) · p_etsy)`, con `p_etsy` de 1–3 % para una tienda típica [S].
- Reembolsos/contracargos: 3 % de las ventas [E].

## 4. Ingresos netos

    neto_web  = P/(1 + IVA) · (1 − 0,05 − 0,029) − 0,30                        (Payhip)
    neto_etsy = P/(1 + IVA) · (1 − 0,065 − 0,04 − 0,15·0,2) − 0,30 − 0,19      (Etsy; Offsite Ads en el 20 % de las ventas [E])
    Neto(12 meses) = Σ_m (ventas_web · neto_web + ventas_etsy · neto_etsy) · (1 − 0,03) − costes_fijos

`IVA = 21 %` (conservador: se asume que todas las ventas pagan IVA español). Costes fijos: dominio ≈ 15 €/año [S]. **Sin anuncios de pago** (cualquier gasto real es 🔴 del humano).

## 5. Incertidumbre
Cada parámetro incierto es una distribución: lognormal definida por su p5 y p95 (tráfico, conversiones) o uniforme (retrasos). Escenarios:
- **Pesimista:** todos los parámetros en su p10 desfavorable · **Base:** medianas · **Optimista:** p90 favorable.
- **Monte Carlo:** 20.000 corridas → mediana, p10–p90 y **P(Neto ≥ 500 €)**.
- **Sensibilidad (tornado):** cada parámetro se mueve a su p10 y su p90 con el resto en la mediana; se ordena por el cambio que provoca en el neto.

## 6. Supuestos conservadores elegidos a propósito
1. Sin audiencia previa; el tráfico de redes empieza siendo pequeño y puede desaparecer (abandono).
2. Todo el tráfico de Google tiene un retraso de 3–6 meses.
3. Toda venta paga IVA del 21 %, aunque haya ventas fuera de España.
4. No se modelan ventas recurrentes, subidas de precio ni productos nuevos (todo eso sería ganancia extra).
5. Rangos de tráfico sin datos absolutos de volumen de búsqueda (sin Keyword Planner): distribuciones **anchas** a propósito.

## 7. Ajustes de idea (v2, Día 6, 2026-10-27)
Implementados en `../simulador/simulador.py` (ganchos opcionales; sin ellos el resultado es idéntico a v1) y probados en `../simulador/ajustes.py`. Fuentes: `../investigacion/08_BENCHMARKS_AJUSTES.md`.

- **Elasticidad precio-conversión:** al subir el precio de `P_ref` a `P`, todas las conversiones se multiplican por `(P/P_ref)^−e`, con `e` ~ U(1, 2) [S/E]. La regla práctica "+10 % de precio → −20 % de conversión" en mercados saturados equivale a `e ≈ 2`, que es el extremo desfavorable.
- **Nivel premium:** se ofrece junto al pack normal; una fracción `f` ~ U(10 %, 30 %) de los compradores elige el premium [E]. Supuesto conservador: el premium **no** sube la conversión (no se modela el efecto ancla) y el ticket medio pasa a ser `(1−f)·P + f·P_premium`.
- **Escalera en Etsy:** el anuncio de Etsy vende un producto de 4 € en lugar del pack. Convierte `mult_tw` ~ U(1,5, 3) veces más [E], y una fracción `p_upsell` (lognormal, p5–p95 = 2–12 %) [E] compra después el pack en la web. Los vendedores citan un 2–8 % (y hasta un 50 % en ofertas de checkout) [S, fuentes comerciales]; aquí se usa un rango más bajo.
- **Catálogo de dos productos:** las redes del dueño se reparten (`red_base` a la mitad en cada producto) y el dominio se paga una sola vez. Se dan dos cotas:
  - *indep.:* los parámetros de cada producto se sortean por separado (cota optimista);
  - *correl.:* los parámetros comunes usan el mismo cuantil en ambos productos, de modo que si Etsy o la conversión fallan en uno, fallan en el otro (cota conservadora).
  En "BB" (B para un segundo sector), el segundo sector tiene la **mitad** de tráfico SEO y de Etsy, porque su demanda no está medida [E].
- **No modelado (riesgo a favor del modelo):** el doble trabajo que supone construir y mantener dos productos. Es la limitación principal del catálogo.
