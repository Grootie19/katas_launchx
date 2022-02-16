# Realizar un informe de del combustible restante en diferentes ubicaciones de la nave

# Funcion para leer 3 tanques de combustible y calcular el promedio

from audioop import lin2adpcm


def combustible(cantidad):
    tCombustible = sum(cantidad)
    return tCombustible

def promedio(*argu):
    prom = combustible(argu) / len(argu)
    return prom


print(round(promedio(6, 5, 5), 2))
    



