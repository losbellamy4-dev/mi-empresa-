# 🔴 ACCIÓN REQUERIDA (actualizado el Día 13, 2026-11-21)

> ⚠️ **Lo más urgente: continuidad.** Hoy la sesión volvió a arrancar en el Día 1 (lo detecté a tiempo). **Arreglo en un clic:** en GitHub → *Pull requests*, abre el **PR #6** (https://github.com/losbellamy4-dev/mi-empresa-/pull/6) de la rama `claude/confident-tesla-sff658` (Días 2–13, incluye todo lo de los PR #1–#5) → "Ready for review" → **Merge**. Después cierra los PR #1–#5. Es gratis y no pide datos personales.
>
> **Novedad del Día 13 (importante para la idea B):**
> - En Etsy, un anuncio nuevo tiene **una sola oportunidad corta** de demostrar que la gente hace clic y compra. Nuestros anuncios de prueba daban 4 diseños por 9 $, cuando los de al lado dan 50–345 diseños por 15–47 $.
> - Con esa oferta, el simulador baja a **≈ 28 %** de probabilidad de llegar a 500 €. Si el anuncio principal es el **pack completo** (≈ 38 diseños × 3 paletas, 19–24 $), sube a **≈ 43 %**.
> - Por eso, antes de la prueba de Etsy hay que montar el pack completo en Canva (≈ 10–15 h). Detalle: `investigacion/15_ETSY_NUEVOS_ANUNCIOS.md`.
>
> Recordatorio: **veredicto = NO con los supuestos actuales** (mejor opción ≈ 43 %). Son estimaciones, no garantías.

## 1. Elegir la idea de negocio (pendiente desde el Día 4)
**Quién:** Adrián (con un adulto si quiere opinar)

> ⚠️ Las cifras de esta tabla son de antes de la corrección del Día 10 (estaban infladas ≈ ×2). Cifras actuales: `modelo/VEREDICTO.md` v5.

El Día 6 probé en el simulador varios ajustes de las ideas (`modelo/VEREDICTO.md` v2):

| | Idea | P(≥ 500 €) v1 | **P(≥ 500 €) v2 (mejor ajuste)** |
|---|---|---|---|
| A | Planificador para **opositores** + generador gratis | 22 % | 25 % (con versión premium a 24 €) |
| **B** | Plantillas Canva para **inmobiliarias** | 39 % | **43 %** con pack normal (17 €) + pack agencia (29 €) · **58 %** si después se añade un 2.º sector (catálogo) |
| C | Planner para **estudiantes** + generador gratis | 9 % | (sin ajustar; descartada en la práctica) |

\* Son estimaciones de un modelo con supuestos conservadores, no garantías. Un producto suelto **no** llega a 500 € en el caso base; un catálogo de dos se queda cerca (452–473 €) y supera los 500 € en la mediana del Monte Carlo.

**Mi recomendación (Día 10):** B sigue siendo la más fuerte, pero **ninguna idea pasa hoy del 50 %**; elegir B significa empezar por la prueba de Etsy-EN y decidir con su dato. Antes (Días 8–9): B como catálogo por sectores (inmobiliarias + psicólogos), vendido en web propia en español + Etsy con anuncios en español e inglés.** Antes (Día 6): (primero inmobiliarias y, cuando esté terminado, un segundo sector, como clínicas estéticas o peluquerías), con dos niveles de precio. Descarté subir el precio único y el "producto escalera" de 4 €, porque en la simulación empeoran el resultado.

### Cómo responder
Crea `negocio/RESPUESTA_HUMANO.md` en **cualquier rama** del repo (la tarea revisa todas) con:
```
Elijo: B
Comentarios: (opcional)
```

## 2. (URGENTE, 2 minutos) Arreglar la continuidad entre sesiones ⚠️ sigue pasando
Cada sesión diaria arranca desde la rama por defecto del repo (`claude/confident-tesla-2gx72p`), que sigue en el **Día 1**. El 24, 25, 26 y 28 de octubre, cuatro sesiones rehicieron el Día 2 desde cero (`kmq0em`, `odi82r`, `nksbhx`, `smd1j5`): **cuatro días perdidos de once**.
**Solución:** en GitHub → *Settings → General → Default branch*, cambia la rama por defecto a **`claude/confident-tesla-tkfnj4`** (la más avanzada, Día 11; contiene todo lo anterior). Alternativa: fusionar esa rama en `claude/confident-tesla-2gx72p`. No cuesta dinero ni requiere datos personales.

## 3. (Opcional, gratis, con un adulto) Medir Etsy de verdad
Una cuenta gratuita de eRank (o de vendedor en Etsy) enseña el volumen real de búsqueda en Etsy de "plantillas inmobiliaria" y "plantillas psicologos". Es el dato que más incertidumbre quitaría al modelo. Si lo consigues, pégalo en `RESPUESTA_HUMANO.md`.
