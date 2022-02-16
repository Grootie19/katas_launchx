# Informe detallado del estado de combustible haciendo uso de argumentos de palabra clave
# Aspectos que deberá incluir el informe
# Hora de prelanzamiento
# Tiempo de vuelo
# Destino
# Tanque externo
# Tanque interno

def informeMision (hLaunch, tVuelo, nDestino, cTanqueExt, cTanqueInt):
    
    return f""""La hora de lanzamiento aproximada es: {hLaunch}
    Tiempo de vuelo esperado: {tVuelo}
    Destino:  {nDestino}
    Capacidad del tanque externo: {cTanqueExt}
    Capacidad del tanque interno: {cTanqueInt}
    """

print(informeMision('14:00', 50, 'Luna', 800, 500))

