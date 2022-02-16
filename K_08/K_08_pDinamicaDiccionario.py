# Calcular el número total de lunas en el SS
# Calcila el promedio de lunas que tiene un planeta

# Planetas y lunas

planet_moons = {
    'mercurio' : 0,
    'venus' : 0,
    'tierra' : 1,
    'marte' : 2,
    'jupiter' : 79,
    'saturno' : 82,
    'urano' : 27,
    'neptuno' : 14,
    'pluton' : 5,
    'haumea' : 2,
    'makemake' : 1,
    'eris' : 1,
}
total_moons = 0
planets = (len(planet_moons))

for moons in planet_moons.values():
    total_moons = total_moons + moons

print(f"El nuestro sistema solar hay {planets} planetas")
print(f"Y existen {total_moons} lunas")
print(f"Se podría decir que en promedio un planeta tiene {round(total_moons/planets)} lunas, pero nah")
