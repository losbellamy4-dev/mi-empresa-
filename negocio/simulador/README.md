# Simulador ("gemelo digital")

Estado: **esqueleto genérico (día 2)**. Todavía no está calibrado a una idea concreta, eso se hace en la Fase 2.

- `embudo.py` — modelo de embudo mensual (visitas → ventas → ingreso neto) con 3 escenarios y Monte Carlo.
  Solo usa la biblioteca estándar de Python (no hace falta instalar nada).
- Ejecutar: `python3 simulador/embudo.py` (los resultados se guardan en `simulador/resultados/`).

Los parámetros actuales son **provisionales** y salen de `investigacion/02_PLATAFORMAS_Y_COSTES.md` y `04_DEMANDA_Y_COMPETENCIA.md`.
La probabilidad que calcula es una estimación del modelo bajo esos supuestos, NO una garantía.
