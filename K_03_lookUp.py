# Avisar que es posible el avistamiento de un asteroide
# El asteroide tiene una velocidad mayor o igual a 20 km/s
import random as rm
from turtle import st
# Velocidad actual del asteroide : 19 km/s

#Variable
velActual = 19
lati = rm.randint(111111, 999999)
long = rm.randint(111111, 999999)

#Prueba (Condicion)

if velActual >= 20 and velActual <= 25:
    # Instrucción
    print("Mira al cielo, es problable que veas un asteroide, podrás verlo si estás en las siguientes coordenadas:\n"+str(lati) + "\n" +str(long))

elif velActual >= 8 and velActual <= 19:
    # Instrucción
    print("Un asteroide se dirige a la tierra, pero es muy poco probable su avistamiento")

elif velActual < 8:
    # Instrucción
    print("La velocidad del asteroide es demasiado baja para causar un avistamiento")

else:
    # Instrucción
    print("Un asteroide viene en camino, SU VELOCIDAD ES SUPERIOR AL RANGO CRITICO.\nPunto de impacto estimado \n"+str(lati) + "\n" +str(long))

