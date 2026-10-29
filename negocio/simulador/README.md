# Simulador ("gemelo digital")

- `simulador.py` — simulador de Fase 2. Ecuaciones en `../modelo/modelo.md`. Desde el Día 6 admite ajustes opcionales (elasticidad, nivel premium, escalera) sin cambiar los resultados de v1.
  `python3 simulador.py [n_corridas] [semilla]` → `resultados/resultados_fase2.md`, `.json`, `hist_*.svg`, `tornado_*.svg`.
- `ajustes.py` — (Día 6) prueba variantes de las ideas: precio, premium, escalera y catálogos (con cotas independiente y correlacionada).
  `python3 ajustes.py [n_corridas] [semilla]` → `resultados/ajustes_v2.md` y `.json` (≈ 12 s).
- `sim_preview.py` — vista previa del Día 4 (histórica; sobreestimaba A y C).

Solo usa la librería estándar de Python.
- `dia7.py` — (Día 7) sensibilidad de B y BB al rango de visitas de Etsy (v2 20–800, v3 10–400, estrés 5–200) y tornado del catálogo BB.
  `python3 dia7.py [n_corridas] [semilla]` → `resultados/dia7.md`, `.json` y `tornado_BB.svg` (≈ 7 s).
