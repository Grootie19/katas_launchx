# Realizar un informe de del combustible restante en diferentes ubicaciones de la nave

# Funcion para leer 3 tanques de combustible y calcular el promedio

def combustible(cantidad):
    tCombustible = sum(cantidad)
    return tCombustible

# La funcion recibe los argumentos que el usuario introduzca, no importa cuantos
def promedio(*argu):
    prom = combustible(argu) / len(argu)
    return prom


print(round(promedio(6, 5, 5), 2))
    



