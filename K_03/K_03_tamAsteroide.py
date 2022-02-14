# Los asteroides < 25 metros muy probablemente se quemen
# Si un asteroide > 25 y < 1000: mucho daño
# Velocidad del asteroide > 25 -> Advertencia
# Velocidad del asteroide > 20 -> Visible

# Variables
dimAsteroide = 11
velAsteroide = 24

#Prueba (Condición)
print(f"Velocidad: {velAsteroide} \nDimension: {dimAsteroide}")
if velAsteroide > 25:
    #Instruccion
    print("ASTEROIDE EN VELOCIDAD CRITICA, ")

    #Segunda condicion
    if dimAsteroide > 25 and dimAsteroide < 1000:
        #Instrucción
        print("Daño estimado: GRAVE")

    elif dimAsteroide >= 1000:
        #Instrucción
        print("Daño estimado: DEVASTACION INMINENTE")

    elif dimAsteroide < 25:
        print("Daño estimado: ESCASO")

elif velAsteroide >= 20 and velAsteroide <=25:
    #Instrucción
    print("Asteroide entrando a la atmosfera, es posible que puedas verlo, de acuerdo a su tamaño el riesgo al impactar es: ")

    #Segunda condicion
    if dimAsteroide > 25 and dimAsteroide < 1000:
        #Instrucción
        print("MODERADO")

    elif dimAsteroide >= 1000:
        #Instrucción
        print("GRAVE")

    elif dimAsteroide < 25:
        print("ESCASO")

elif velAsteroide < 20 and velAsteroide < 0:
    #Instrucción
    print("Asteroide aproximandose a baja velocidad, las posibilidades de avistamiento son escasas")

    #Segunda condicion
    if dimAsteroide > 25 and dimAsteroide < 1000:
        #Instrucción
        print("BAJO")

    elif dimAsteroide >= 1000:
        #Instrucción
        print("MODERADO")

    elif dimAsteroide < 25:
        print("NULO")

else:
    print("No hay datos de asteroides actualmente")
