# 🔴 ACCIÓN REQUERIDA (actualizado el Día 14, 2026-11-22)

> ⚠️ **Lo más urgente: continuidad.** Hoy la sesión ha vuelto a arrancar en el Día 1 (es la 6.ª vez que pasa, y lo detecté a tiempo). **Se arregla en un clic:** entra en GitHub → *Pull requests*, abre el **PR #7** (https://github.com/losbellamy4-dev/mi-empresa-/pull/7) de la rama `claude/confident-tesla-b5hizx`, que lleva los Días 2–14 y todo lo de los PR #1–#6, y pulsa "Ready for review" → **Merge**. Después cierra los PR #1–#6. Es gratis y no pide datos personales.
>
> **Novedades del Día 14:**
> - Ya está hecho el **calendario de 30 días** (en español e inglés, PDF de una página): `producto/calendario/`. Cada día dice qué plantilla del pack publicar.
> - Los textos de los anuncios de Etsy están en su **versión 2**: el anuncio principal es el pack completo a 22 $ y los sueltos cuestan 4–6 $. Corrección: el pack tiene **34 diseños**, no 38.
> - Ojo: en Etsy ya hay calendarios parecidos. Lo que nos diferencia es que el calendario va ligado a nuestras plantillas y que **todo viene en inglés y español**.
> - Simulador: entre **35 y 48 %** de probabilidad de llegar a 500 €. Depende de si los sueltos le quitan ventas al pack o traen clientes nuevos. Son estimaciones, no garantías.
>
> Recordatorio: **el veredicto es NO con los supuestos actuales**, porque ninguna opción llega al 50 %. Antes de la prueba de Etsy hace falta montar el pack completo en Canva (unas 10–15 h).

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
**Solución:** en GitHub → *Settings → General → Default branch*, cambia la rama por defecto a **`claude/confident-tesla-b5hizx`** (la más avanzada, Día 14; contiene todo lo anterior). Alternativa: fusionar esa rama en `claude/confident-tesla-2gx72p`. No cuesta dinero ni requiere datos personales.

## 3. (Opcional, gratis, con un adulto) Medir Etsy de verdad
Una cuenta gratuita de eRank (o de vendedor en Etsy) enseña el volumen real de búsqueda en Etsy de "plantillas inmobiliaria" y "plantillas psicologos". Es el dato que más incertidumbre quitaría al modelo. Si lo consigues, pégalo en `RESPUESTA_HUMANO.md`.
