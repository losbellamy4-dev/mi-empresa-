# 🔴 ACCIÓN REQUERIDA (actualizado el Día 8, 2026-11-12)

> **Novedad del Día 8:** vender también el pack de inmobiliarias **en inglés en Etsy** (misma tienda, anuncios traducidos) sube la probabilidad estimada del catálogo B de **42 % a ≈ 66 %** (caso base 603 €). Hotmart apenas ayuda. Por primera vez el modelo conservador **supera 500 € en el caso base**, aunque apoyado en un solo dato de Etsy-EN. Detalle: `modelo/VEREDICTO.md` v4.
>
> ⚠️ **Continuidad (lo más urgente):** del 30-oct al 11-nov, **14 sesiones seguidas** rehicieron el "Día 2" desde cero porque arrancan desde la rama por defecto (Día 1). Hoy lo he recuperado todo en **`claude/confident-tesla-2loft6`**. Cambia la rama por defecto a esa (GitHub → Settings → General → Default branch) para no perder más días. Gratis, 2 minutos.

## 1. Elegir la idea de negocio (pendiente desde el Día 4)
**Quién:** Adrián (con un adulto si quiere opinar)

El Día 6 probé en el simulador varios ajustes de las ideas (`modelo/VEREDICTO.md` v2):

| | Idea | P(≥ 500 €) v1 | **P(≥ 500 €) v2 (mejor ajuste)** |
|---|---|---|---|
| A | Planificador para **opositores** + generador gratis | 22 % | 25 % (con versión premium a 24 €) |
| **B** | Plantillas Canva para **inmobiliarias** | 39 % | **43 %** con pack normal (17 €) + pack agencia (29 €) · **58 %** si después se añade un 2.º sector (catálogo) |
| C | Planner para **estudiantes** + generador gratis | 9 % | (sin ajustar; descartada en la práctica) |

\* Son estimaciones de un modelo con supuestos conservadores, no garantías. Un producto suelto **no** llega a 500 € en el caso base; un catálogo de dos se queda cerca (452–473 €) y supera los 500 € en la mediana del Monte Carlo.

**Mi recomendación (Día 8): B como catálogo por sectores (inmobiliarias + psicólogos), vendido en web propia en español + Etsy con anuncios en español e inglés.** Antes (Día 6): (primero inmobiliarias y, cuando esté terminado, un segundo sector, como clínicas estéticas o peluquerías), con dos niveles de precio. Descarté subir el precio único y el "producto escalera" de 4 €, porque en la simulación empeoran el resultado.

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
