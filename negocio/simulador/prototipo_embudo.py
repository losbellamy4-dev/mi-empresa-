"""
PROTOTIPO (preparación de Fase 2) — simulador de embudo genérico con Monte Carlo.

Aún NO es el simulador oficial: la idea no está elegida y los rangos son
preliminares (ver investigacion/02 y 04). Sirve para:
  1) tener la estructura lista para la Fase 2;
  2) dar una primera intuición de qué variables mandan.

Modelo mensual:
  visitas_m = suma de canales (cada canal crece linealmente hasta su techo)
  ventas_m  ~ Binomial(visitas_m, conversion)
  neto_m    = ventas_m * (precio * (1 - comision_pct) - comision_fija) - costes_fijos_m

Riesgo de canal: con probabilidad p_fallo_canal un canal "no arranca" y
aporta solo el 10 % de lo previsto (modela el caso típico de 0 tracción).

Uso:  python3 prototipo_embudo.py
"""
import json
import random
import statistics
from pathlib import Path

UMBRAL = 500.0
MESES = 7          # horizonte de venta tras lanzar (supuesto conservador)
N_RUNS = 20000
SEED = 42


def tri(lo, mode, hi, rng):
    return rng.triangular(lo, hi, mode)


# Rangos PRELIMINARES para L1 (planners de estudio en español). Todo [E].
PARAMS_L1 = {
    "precio": (4.0, 6.0, 9.0),                  # € — competencia 4,99 $–12,50 $
    "comision_pct": (0.08, 0.12, 0.25),          # Payhip ~8 % ... Etsy hasta ~25 %
    "comision_fija": (0.25, 0.30, 0.50),         # € por venta
    "conversion": (0.005, 0.01, 0.03),           # visita->compra, conservador 1 %
    "costes_fijos_mes": (1.0, 1.25, 2.0),        # dominio ~15 €/año
    # canales: (techo de visitas/mes al final del horizonte: lo, modo, hi), p_fallo
    "canales": {
        "etsy_busqueda": ((50, 250, 900), 0.40),
        "pinterest": ((0, 150, 1500), 0.50),
        "seo_herramienta_gratis": ((0, 100, 1200), 0.60),
        "redes_menor (capado <16)": ((0, 30, 300), 0.70),
    },
}


def simular_una(params, rng):
    precio = tri(*params["precio"], rng)
    c_pct = tri(*params["comision_pct"], rng)
    c_fija = tri(*params["comision_fija"], rng)
    conv = tri(*params["conversion"], rng)
    fijos = tri(*params["costes_fijos_mes"], rng)
    techos = {}
    for nombre, (rango, p_fallo) in params["canales"].items():
        t = tri(*rango, rng)
        if rng.random() < p_fallo:
            t *= 0.10
        techos[nombre] = t
    neto_venta = precio * (1 - c_pct) - c_fija
    total = 0.0
    ventas_tot = 0
    for m in range(1, MESES + 1):
        rampa = m / MESES
        visitas = int(sum(t * rampa for t in techos.values()))
        # Binomial aproximada por suma de Bernoulli si es pequeño; normal si grande
        if visitas < 2000:
            ventas = sum(1 for _ in range(visitas) if rng.random() < conv)
        else:
            mu = visitas * conv
            ventas = max(0, round(rng.gauss(mu, (mu * (1 - conv)) ** 0.5)))
        ventas_tot += ventas
        total += ventas * neto_venta - fijos
    return total, ventas_tot, {"precio": precio, "conversion": conv, **techos}


def monte_carlo(params, n=N_RUNS, seed=SEED):
    rng = random.Random(seed)
    res = [simular_una(params, rng) for _ in range(n)]
    netos = sorted(r[0] for r in res)
    p = lambda q: netos[int(q * (len(netos) - 1))]
    prob = sum(1 for x in netos if x >= UMBRAL) / len(netos)
    # sensibilidad simple: correlación de cada input con el neto
    claves = list(res[0][2].keys())
    sens = {}
    for k in claves:
        xs = [r[2][k] for r in res]
        try:
            sens[k] = round(statistics.correlation(xs, [r[0] for r in res]), 3)
        except statistics.StatisticsError:
            sens[k] = None
    return {
        "runs": n,
        "meses": MESES,
        "neto_P10": round(p(0.10), 1),
        "neto_P50": round(p(0.50), 1),
        "neto_P90": round(p(0.90), 1),
        "prob_neto_>=_500": round(prob, 3),
        "ventas_mediana": statistics.median(r[1] for r in res),
        "sensibilidad_correlacion": dict(sorted(sens.items(), key=lambda kv: -abs(kv[1] or 0))),
        "aviso": "Estimación de un PROTOTIPO con supuestos preliminares; no es una garantía.",
    }


if __name__ == "__main__":
    out = monte_carlo(PARAMS_L1)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    dest = Path(__file__).parent / "resultados" / "prototipo_L1_dia2.json"
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"Guardado en {dest}")
