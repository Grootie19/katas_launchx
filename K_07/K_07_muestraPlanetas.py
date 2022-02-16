# Mostrar la lista de planetas que el usuario haya ingresado

# Codigo anterior
# Declaracion de variables

new_planet = ''
planets = []

# Para terminar la lista el usuario ingresa la palabra 'done'
while new_planet.lower() != 'done':
    planets.append(new_planet)
    new_planet = input("Nombre del planeta a agregar: ")

planets.pop(0)

item = 0
for planeta in planets:
    print(f"{item+1}.- {planets[item]}")
    item += 1
