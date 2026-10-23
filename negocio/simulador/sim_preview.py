"""Vista previa del simulador (preparación de Fase 2, Día 4).

NO es el simulador final. Sirve para comparar las 3 finalistas con el mismo
modelo de embudo sencillo antes de que el humano elija:

    visitas(m)  = V_max * (1 - exp(-m / tau))      # crecimiento tipo SEO
    ventas(m)   ~ Poisson(visitas(m) * conversion)
    neto        = sum(ventas * neto_por_venta) - costes_fijos

Los parámetros son supuestos [E] marcados en PARAMS. Solo usa la librería
estándar (sin numpy) para que corra en cualquier sesión.

Uso: python3 sim_preview.py [n_corridas]
"""
import math
import random
import statistics
import sys
from pathlib import Path

UMBRAL = 500.0
MESES = 12            # horizonte de F5: <= 12 meses tras lanzar
COSTE_FIJO = 15.0     # dominio ~12 €/año + margen [S, Día 1]
IVA = 0.21
COMISION = 0.05 + 0.029   # Payhip 5 % + pasarela ~2,9 % [S, Día 1]
FIJO_PASARELA = 0.30


def neto_por_venta(precio):
    base = precio / (1 + IVA)
    return base * (1 - COMISION) - FIJO_PASARELA


# Distribuciones lognormales dadas por (p5, p95). Todo [E] salvo el precio.
PARAMS = {
    "A_opositores": {"precio": 15, "vmax": (80, 4000), "conv": (0.002, 0.03), "tau": (2, 8)},
    "B_inmobiliarias": {"precio": 17, "vmax": (40, 1500), "conv": (0.004, 0.03), "tau": (1, 6)},
    "C_estudiantes": {"precio": 7, "vmax": (150, 8000), "conv": (0.001, 0.015), "tau": (2, 8)},
}


def lognormal_p5_p95(rng, p5, p95):
    mu = (math.log(p5) + math.log(p95)) / 2
    sigma = (math.log(p95) - math.log(p5)) / (2 * 1.6449)
    return rng.lognormvariate(mu, sigma)


def poisson(rng, lam):
    if lam > 50:  # aproximación normal para lambdas grandes
        return max(0, round(rng.gauss(lam, math.sqrt(lam))))
    l, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= l:
            return k
        k += 1


def corrida(rng, p):
    vmax = lognormal_p5_p95(rng, *p["vmax"])
    conv = min(lognormal_p5_p95(rng, *p["conv"]), 0.10)
    tau = rng.uniform(*p["tau"])
    ventas = sum(poisson(rng, vmax * (1 - math.exp(-m / tau)) * conv) for m in range(1, MESES + 1))
    return ventas * neto_por_venta(p["precio"]) - COSTE_FIJO


def escenario_fijo(p, cuantil):
    """Pesimista/base/optimista: todos los parámetros en p5 / mediana / p95."""
    def q(a, b):
        return {"p5": a, "p50": math.sqrt(a * b), "p95": b}[cuantil]
    vmax, conv = q(*p["vmax"]), q(*p["conv"])
    tau = {"p5": p["tau"][1], "p50": sum(p["tau"]) / 2, "p95": p["tau"][0]}[cuantil]
    visitas = sum(vmax * (1 - math.exp(-m / tau)) for m in range(1, MESES + 1))
    return visitas * conv * neto_por_venta(p["precio"]) - COSTE_FIJO


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    rng = random.Random(42)
    lineas = [
        "# Vista previa de simulación de las finalistas (Día 4)",
        "",
        f"Monte Carlo con {n} corridas por idea, horizonte de {MESES} meses tras lanzar, semilla 42.",
        "**Estimación del modelo con supuestos [E], no una garantía.** El simulador de Fase 2 sustituirá estos rangos por datos investigados.",
        "",
        "| Idea | Neto/venta | Pesimista (p5) | Base (mediana) | Optimista (p95) | MC mediana | MC p10–p90 | P(≥ 500 €) |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for nombre, p in PARAMS.items():
        res = sorted(corrida(rng, p) for _ in range(n))
        prob = sum(r >= UMBRAL for r in res) / n
        dec = statistics.quantiles(res, n=10)
        lineas.append(
            f"| {nombre} | {neto_por_venta(p['precio']):.2f} € | {escenario_fijo(p, 'p5'):.0f} € | "
            f"{escenario_fijo(p, 'p50'):.0f} € | {escenario_fijo(p, 'p95'):.0f} € | "
            f"{statistics.median(res):.0f} € | {dec[0]:.0f}–{dec[-1]:.0f} € | **{prob:.0%}** |"
        )
    lineas += ["", "Parámetros (p5–p95 de lognormales): " + "; ".join(
        f"{k}: visitas/mes maduras {v['vmax']}, conversión {v['conv']}, tau {v['tau']} meses"
        for k, v in PARAMS.items())]
    salida = "\n".join(lineas) + "\n"
    out = Path(__file__).parent / "resultados" / "preview_finalistas.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(salida, encoding="utf-8")
    print(salida)


if __name__ == "__main__":
    main()
