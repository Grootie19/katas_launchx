# Crear un programa que permita al usuario añadir planetas a una lista

# Declaracion de variables
from hashlib import new

new_planet = ''
planets = []

# Para terminar la lista el usuario ingresa la palabra 'done'
while new_planet.lower() != 'done':
    planets.append(new_planet)
    new_planet = input("Nombre del planeta a agregar: ")

print (planets)