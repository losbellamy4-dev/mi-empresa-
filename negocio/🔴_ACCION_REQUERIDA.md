# 🔴 ACCIÓN REQUERIDA (actualizado el Día 15, 2026-11-23)

> ⚠️ **Lo más urgente sigue siendo la continuidad (7.ª vez).** Hoy la sesión volvió a arrancar en el Día 1 y **se perdió el día entero** rehaciendo trabajo que ya existía. **Se arregla en 1 minuto, gratis y sin datos personales:** en GitHub → *Settings → General → Default branch*, cambia la rama por defecto a **`claude/confident-tesla-rzx5pl`**. La otra opción es fusionar el PR más reciente (el de esa rama, que lo incluye todo) en `claude/confident-tesla-2gx72p` y cerrar los PR antiguos (#1–#7).
>
> Mientras no se haga, cada sesión empieza en el Día 1 y la mayoría de los días se pierden.
>
> Recordatorio: la **elección de idea** (A/B/C) sigue pendiente desde el Día 4. La recomendación es B. Se responde en `negocio/RESPUESTA_HUMANO.md`.

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
