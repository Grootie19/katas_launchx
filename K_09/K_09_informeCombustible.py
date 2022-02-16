# Realizar un informe de del combustible restante en diferentes ubicaciones de la nave

# Funcion para leer 3 tanques de combustible y calcular el promedio

def combustible(dep1, dep2, dep3):
    tCombustible = dep1 + dep2 + dep3
    return round(tCombustible/3, 2)

print(combustible(0, 1, 1))
