# /negocio — Proyecto de micro-negocio digital

- `ESTADO.json` → en qué fase está el proyecto y qué toca después.
- `BITACORA.md` → diario de cada sesión.
- `🔴_ACCION_REQUERIDA.md` → aparecerá solo cuando haga falta que un humano decida o actúe.
- `RESPUESTA_HUMANO.md` → crea este archivo para responder a una decisión pendiente.
- `investigacion/` → Fase 1. `modelo/` y `simulador/` → Fase 2. `web/` → Fase 3. `entregables/` → checkpoints y entrega final.

## Nota de continuidad (para la tarea programada)
Cada sesión puede arrancar en una rama `claude/*` distinta, y alguna puede partir de un estado antiguo. **Al iniciar:** `git fetch origin` y comprobar qué rama tiene el `dia_global` más alto en `negocio/ESTADO.json` (`git log --all`); integrar esa rama antes de trabajar.
