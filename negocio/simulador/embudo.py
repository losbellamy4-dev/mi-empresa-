"""Simulador genérico de embudo para un producto digital (esqueleto, día 2).

Modelo mensual:
    visitas_m   = visitas_iniciales * (1 + crecimiento) ** m      (limitado por techo_visitas)
    ventas_m    ~ Binomial(visitas_m, conversion)                (en Monte Carlo)
    neto_venta  = precio * (1 - comision_pct) - comision_fija
    neto_m      = ventas_m * neto_venta - coste_fijo_mensual

Todos los parámetros son PROVISIONALES hasta calibrarlos en la Fase 2.
Solo usa la biblioteca estándar de Python.
"""

import json
import random
import statistics
from pathlib import Path

UMBRAL_EUR = 500
MESES = 7
RESULTADOS = Path(__file__).parent / "resultados"

# Escenarios deterministas. Fuentes: investigacion/02 y 04.
ESCENARIOS = {
    "pesimista": dict(precio=5.0, conversion=0.005, visitas_iniciales=50, crecimiento=0.15,
                      techo_visitas=600, comision_pct=0.12, comision_fija=0.30, coste_fijo_mensual=1.0),
    "base":      dict(precio=7.0, conversion=0.01, visitas_iniciales=150, crecimiento=0.25,
                      techo_visitas=1500, comision_pct=0.10, comision_fija=0.30, coste_fijo_mensual=1.0),
    "optimista": dict(precio=9.0, conversion=0.03, visitas_iniciales=300, crecimiento=0.35,
                      techo_visitas=4000, comision_pct=0.08, comision_fija=0.30, coste_fijo_mensual=1.0),
}

# Rangos para Monte Carlo (uniforme entre mín. y máx.).
RANGOS = {
    "precio": (4.0, 10.0),
    "conversion": (0.005, 0.03),
    "visitas_iniciales": (20, 300),
    "crecimiento": (0.0, 0.35),
    "techo_visitas": (300, 4000),
    "comision_pct": (0.07, 0.15),
    "comision_fija": (0.30, 0.30),
    "coste_fijo_mensual": (1.0, 1.0),  # dominio ~12 €/año
}


def visitas_mes(p, m):
    return min(p["techo_visitas"], p["visitas_iniciales"] * (1 + p["crecimiento"]) ** m)


def neto_por_venta(p):
    return p["precio"] * (1 - p["comision_pct"]) - p["comision_fija"]


def simular_determinista(p, meses=MESES):
    filas, acumulado = [], 0.0
    for m in range(meses):
        v = visitas_mes(p, m)
        ventas = v * p["conversion"]
        neto = ventas * neto_por_venta(p) - p["coste_fijo_mensual"]
        acumulado += neto
        filas.append(dict(mes=m + 1, visitas=round(v), ventas=round(ventas, 2),
                          neto=round(neto, 2), acumulado=round(acumulado, 2)))
    return filas


def binomial(rng, n, prob):
    # Aproximación suficiente para n pequeño/medio sin numpy.
    n = int(round(n))
    if n * prob > 30:
        return max(0, round(rng.gauss(n * prob, (n * prob * (1 - prob)) ** 0.5)))
    return sum(1 for _ in range(n) if rng.random() < prob)


def simular_estocastico(p, rng, meses=MESES):
    acumulado = 0.0
    for m in range(meses):
        ventas = binomial(rng, visitas_mes(p, m), p["conversion"])
        acumulado += ventas * neto_por_venta(p) - p["coste_fijo_mensual"]
    return acumulado


def monte_carlo(n=5000, semilla=42):
    rng = random.Random(semilla)
    resultados, muestras = [], []
    for _ in range(n):
        p = {k: rng.uniform(lo, hi) for k, (lo, hi) in RANGOS.items()}
        r = simular_estocastico(p, rng)
        resultados.append(r)
        muestras.append((p, r))
    resultados.sort()
    q = lambda f: round(resultados[int(f * (n - 1))], 2)
    return dict(
        corridas=n,
        prob_supera_umbral=round(sum(r >= UMBRAL_EUR for r in resultados) / n, 4),
        p10=q(0.10), mediana=q(0.50), p90=q(0.90),
        media=round(statistics.fmean(resultados), 2),
    ), muestras


def sensibilidad(muestras):
    """Correlación de Spearman aproximada (por rangos) de cada parámetro con el resultado."""
    def rangos(xs):
        orden = sorted(range(len(xs)), key=xs.__getitem__)
        r = [0] * len(xs)
        for i, idx in enumerate(orden):
            r[idx] = i
        return r
    ry = rangos([r for _, r in muestras])
    out = {}
    for k, (lo, hi) in RANGOS.items():
        if lo == hi:
            continue
        rx = rangos([p[k] for p, _ in muestras])
        out[k] = round(statistics.correlation(rx, ry), 3)
    return dict(sorted(out.items(), key=lambda kv: -abs(kv[1])))


def main():
    RESULTADOS.mkdir(parents=True, exist_ok=True)
    salida = {"umbral_eur": UMBRAL_EUR, "meses": MESES, "escenarios": {}}
    for nombre, p in ESCENARIOS.items():
        filas = simular_determinista(p)
        salida["escenarios"][nombre] = {"parametros": p, "meses": filas,
                                        "total_neto": filas[-1]["acumulado"]}
        print(f"{nombre:>10}: {filas[-1]['acumulado']:8.2f} € netos en {MESES} meses")
    mc, muestras = monte_carlo()
    salida["monte_carlo"] = mc
    salida["sensibilidad_spearman"] = sensibilidad(muestras)
    print("Monte Carlo:", mc)
    print("Sensibilidad:", salida["sensibilidad_spearman"])
    print("AVISO: probabilidad estimada por un modelo provisional, no una garantía.")
    (RESULTADOS / "embudo_generico_dia2.json").write_text(
        json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
