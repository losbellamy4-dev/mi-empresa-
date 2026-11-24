# SIGUIENTE: escribir el modelo (Fase 2). Empezar por investigar benchmarks reales:
# - visitas orgánicas típicas de un anuncio nuevo en Etsy / Hotmart; alcance medio de vídeos de cuentas nuevas en TikTok
# - conversión visita→compra en producto digital (rango conservador 0,5–3 %, ver investigacion/02)
# - estacionalidad escolar (picos septiembre / enero / mayo) para A y C
# - parámetros por finalista: precio y neto en investigacion/FINALISTAS.md y 05_TAM_SAM_SOM.md

# Modelo del negocio (borrador pendiente — Fase 2)

Estructura prevista del embudo (igual para A, B y C, con parámetros distintos):

ventas_mes = Σ_canales (visitas_canal_mes × conversión_canal) × factor_estacional_mes
neto_mes   = ventas_mes × (precio × (1 − comisión_%) − comisión_fija) − costes_fijos_mes
acumulado  = Σ neto_mes durante el horizonte (12 meses tras lanzar)

Objetivo: P(acumulado ≥ 500 €) mediante Monte Carlo con supuestos conservadores.
