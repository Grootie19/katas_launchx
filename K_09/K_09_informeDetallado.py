# Informe detallado del estado de combustible haciendo uso de argumentos de palabra clave
# Aspectos que deberá incluir el informe
# Hora de prelanzamiento
# Tiempo de vuelo
# Destino
# Tanque externo
# Tanque interno
from datetime import timedelta, datetime


def informeMision(nDestino,  tVuelo, *minToLauch, **tanques):
    combustibleTotal = 0
    minutos = sum(minToLauch)
    hSalida = timedelta(minutes=minutos) + datetime.now()
    llegada = hSalida + timedelta(minutes=tVuelo)

    for capTanque in tanques.values():
        combustibleTotal += capTanque

    informe = f"""- Faltan: {minutos} minutos para el prelanzamiento
- Hora de despegue estimada: {hSalida.strftime("%H: %M")}
- El tiempo de vuelo esperado es de: {tVuelo} minutos
- Destino:  {nDestino}
- Se estima llegar el dia: {llegada.strftime("%A")} a las {llegada.strftime("%H: %M")} 
- La nave cuenta con {combustibleTotal} toneladas de combustible
distribuidos en {len(tanques)}
"""

    for nTanque, capacidad in tanques.items():
        informe += f"   > {nTanque} con una capacidad de {capacidad} toneladas\n"

    return informe

print(informeMision('Luna', 120, 60, 30, 30, externo = 100, interno = 60, adicional = 20))

