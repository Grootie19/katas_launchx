# Convertir los valores de cadena en números
# utilizar inputs

# Variables
inNamePlanet_01 = input("Nombre del primer Planeta: ")
inDistPlanet_01 = int(input("Distancia al sol: "))
inNamePlanet_02 = input("Nombre del segundo Planeta: ")
inDistPlanet_02 = int(input("Distancia al sol: "))

# Input devulve valores de tipo cadena

#Convertir cadenas a números
# inDistPlanet_01 = int(inDistPlanet_01)
# inDistPlanet_02 = int(inDistPlanet_02)
# Elima este bloque ta que se puede hacer la conversión desde la solicitud de los datos

operacion = inDistPlanet_01 - inDistPlanet_02

print(f"La distancia entre {inNamePlanet_01} y {inNamePlanet_02} es: {abs(operacion)}")


