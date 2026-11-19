# 🔴 ACCIÓN REQUERIDA (actualizado el Día 12, 2026-11-19)

> ⚠️ **Lo más urgente: continuidad.** Hoy la sesión volvió a arrancar en el Día 1 (esta vez lo detecté a tiempo). **Arreglo en un clic:** en GitHub → *Pull requests*, abre el **PR #4** (https://github.com/losbellamy4-dev/mi-empresa-/pull/4) de la rama `claude/confident-tesla-ucgjlr`, Días 2–12, incluye todo lo de los PR #1–#3) → "Ready for review" → **Merge**. Después cierra los PR #1, #2 y #3. Es gratis y no pide datos personales.
>
> **Novedades del Día 12:**
> - Ya están **todas las maquetas que necesitan los 5 anuncios de prueba**: 4 diseños de "Nuevo en cartera", "Puertas abiertas", "Vendido/Reservado" y 2 carruseles. Ábrelas en `negocio/producto/maquetas/index.html`.
> - Hay **5 imágenes de anuncio para Etsy** (ES y EN) en `negocio/producto/mockups/png/`. Para publicarlas hay que poner fotos de stock gratuitas en Canva (un adulto revisa la licencia).
> - El simulador dice que trabajar el SEO de Google rinde poco. Lo que más mueve la probabilidad de llegar a 500 € es que los anuncios de **Etsy en inglés** funcionen.
>
> Recordatorio: **veredicto v5 = NO con los supuestos actuales** (la mejor opción ≈ 42 %). Se puede convertir en SÍ con la prueba de 5 anuncios en Etsy-EN (≈ 1 $, la gestiona un adulto).

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
