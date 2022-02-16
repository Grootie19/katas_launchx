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
moons = 0
planets = (len(planet_moons))

for lunas in planet_moons.values():
    moons = moons + lunas

print(planets)
print(moons)
