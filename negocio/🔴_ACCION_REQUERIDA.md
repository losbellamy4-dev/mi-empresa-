# 🔴 ACCIÓN REQUERIDA (actualizado el Día 10, 2026-11-17)

> ⚠️ **Lo más urgente: continuidad.** Hoy ha vuelto a pasar: la sesión arrancó en el Día 1 y tuve que recuperar el trabajo a mano. **Arreglo en un clic:** fusiona el **PR #2** (https://github.com/losbellamy4-dev/mi-empresa-/pull/2) de la rama `claude/confident-tesla-2hgi05` (Día 10, incluye todo lo del PR #1) hacia la rama por defecto: GitHub → *Pull requests* → abre el PR → "Ready for review" → **Merge**. Después puedes cerrar el PR #1. Alternativa: *Settings → General → Default branch* → `claude/confident-tesla-2hgi05`. Gratis, sin datos personales.
>
> **Novedad importante del Día 10 (aviso honesto):** revisé el simulador y **era demasiado optimista**: no contemplaba que un canal (Google, Etsy, redes) pueda dar **cero visitas**, que es lo más habitual. Corregido, las probabilidades bajan más o menos a la mitad: la mejor opción de B pasa de ≈ 66 % a **≈ 37–42 %**. **Veredicto v5: NO con los supuestos actuales**, pero se puede convertir en SÍ con una prueba barata: 5 anuncios en Etsy en inglés (≈ 1 $). Si en el segundo mes reciben **≥ 260 visitas**, la probabilidad sube a ≈ 65 %. Los textos de esos 5 anuncios ya están listos: `producto/ANUNCIOS_PRUEBA.md`.

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
**Solución:** en GitHub → *Settings → General → Default branch*, cambia la rama por defecto a **`claude/confident-tesla-2hgi05`** (la más avanzada, Día 10; contiene todo lo anterior). Alternativa: fusionar esa rama en `claude/confident-tesla-2gx72p`. No cuesta dinero ni requiere datos personales.

## 3. (Opcional, gratis, con un adulto) Medir Etsy de verdad
Una cuenta gratuita de eRank (o de vendedor en Etsy) enseña el volumen real de búsqueda en Etsy de "plantillas inmobiliaria" y "plantillas psicologos". Es el dato que más incertidumbre quitaría al modelo. Si lo consigues, pégalo en `RESPUESTA_HUMANO.md`.
