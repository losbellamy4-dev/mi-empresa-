# 🔴 ACCIÓN REQUERIDA (actualizado el Día 9, 2026-11-16)

> ⚠️ **Lo más urgente: continuidad.** Ya son **21 sesiones perdidas**: cada día la tarea arranca desde la rama por defecto, que sigue en el Día 1, y rehace el "Día 2" (la última vez el 13, 14 y 15 de noviembre). **Ahora se arregla con un clic:** hay un **Pull Request borrador** de `claude/confident-tesla-9sf6u8` (Día 9) hacia la rama por defecto. Ábrelo en GitHub → *Pull requests* → "Ready for review" → **Merge**. Alternativa: *Settings → General → Default branch* → `claude/confident-tesla-9sf6u8`. Gratis, sin datos personales.
>
> **Novedad del Día 9:** ya está listo el plan para comprobar barato (≈ 1 $, 5 anuncios) si Etsy en inglés funciona, con una regla clara de seguir o parar (`investigacion/11_PLAN_VALIDACION_ETSY_EN.md`). También hay una especificación del pack (`investigacion/12_ESPEC_PACK_INMOBILIARIAS.md`) y un primer esqueleto de la web (`web/index.html`). Todo sirve si eliges B.
> Aviso honesto: mañana reviso un posible optimismo del simulador (casi nunca simula "0 ventas"), así que las probabilidades podrían bajar.

## 1. Elegir la idea de negocio (pendiente desde el Día 4)
**Quién:** Adrián (con un adulto si quiere opinar)

El Día 6 probé en el simulador varios ajustes de las ideas (`modelo/VEREDICTO.md` v2):

| | Idea | P(≥ 500 €) v1 | **P(≥ 500 €) v2 (mejor ajuste)** |
|---|---|---|---|
| A | Planificador para **opositores** + generador gratis | 22 % | 25 % (con versión premium a 24 €) |
| **B** | Plantillas Canva para **inmobiliarias** | 39 % | **43 %** con pack normal (17 €) + pack agencia (29 €) · **58 %** si después se añade un 2.º sector (catálogo) |
| C | Planner para **estudiantes** + generador gratis | 9 % | (sin ajustar; descartada en la práctica) |

\* Son estimaciones de un modelo con supuestos conservadores, no garantías. Un producto suelto **no** llega a 500 € en el caso base; un catálogo de dos se queda cerca (452–473 €) y supera los 500 € en la mediana del Monte Carlo.

**Mi recomendación (Días 8–9, sin cambios): B como catálogo por sectores (inmobiliarias + psicólogos), vendido en web propia en español + Etsy con anuncios en español e inglés.** Antes (Día 6): (primero inmobiliarias y, cuando esté terminado, un segundo sector, como clínicas estéticas o peluquerías), con dos niveles de precio. Descarté subir el precio único y el "producto escalera" de 4 €, porque en la simulación empeoran el resultado.

### Cómo responder
Crea `negocio/RESPUESTA_HUMANO.md` en **cualquier rama** del repo (la tarea revisa todas) con:
```
Elijo: B
Comentarios: (opcional)
```

## 2. (URGENTE, 2 minutos) Arreglar la continuidad entre sesiones ⚠️ sigue pasando
Cada sesión diaria arranca desde la rama por defecto del repo (`claude/confident-tesla-2gx72p`), que sigue en el **Día 1**. El 24, 25, 26 y 28 de octubre, cuatro sesiones rehicieron el Día 2 desde cero (`kmq0em`, `odi82r`, `nksbhx`, `smd1j5`): **cuatro días perdidos de once**.
**Solución:** en GitHub → *Settings → General → Default branch*, cambia la rama por defecto a **`claude/confident-tesla-2loft6`** (la más avanzada, Día 8; contiene todo lo anterior). Alternativa: fusionar esa rama en `claude/confident-tesla-2gx72p`. No cuesta dinero ni requiere datos personales.

## 3. (Opcional, gratis, con un adulto) Medir Etsy de verdad
Una cuenta gratuita de eRank (o de vendedor en Etsy) enseña el volumen real de búsqueda en Etsy de "plantillas inmobiliaria" y "plantillas psicologos". Es el dato que más incertidumbre quitaría al modelo. Si lo consigues, pégalo en `RESPUESTA_HUMANO.md`.
