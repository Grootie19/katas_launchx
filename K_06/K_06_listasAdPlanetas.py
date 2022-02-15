# Crea la lista de planetas



planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Neptuno']

namePlanet = input("Planeta que buscamos: ") 

planetasL = []

# Nombres de planetas a minusculas
for planetaM in planetas[0:]:
    planetasL.append(planetaM.lower())

# Entrada del usuario a minusculas
namePlanetL = namePlanet.lower()

try:
# Busqueda con todas en minuscula
    posPlanet = (planetasL.index(namePlanetL))
    # print(planetasL.index(namePlanetL)) # Imprime la posicion del resultado de busqueda
except: 
    posPlanet = -1

# print(len(planetas))
# print(posPlanet)

if posPlanet == 0:
    print(f"""Has seleccionado el planeta {namePlanet}, este planeta ocupa la posición número {posPlanet+1} en el sistema solar
    Ningun planeta lo antecede
    Los planetas posteriores son {planetas[posPlanet+1:]}""")

elif posPlanet == len(planetas)-1:
    print(f"""Has seleccionado el planeta {namePlanet}, este planeta ocupa la posición número {posPlanet+1} en el sistema solar
    Los planetas que lo anteceden son {planetas[0:posPlanet]}
    Este es el ultimo planeta""")

else:
    print(f"""Has seleccionado el planeta {namePlanet}, este planeta ocupa la posición número {posPlanet+1} en el sistema solar
    Los planetas que lo anteceden son {planetas[0:posPlanet]}
    Los planetas posteriores son {planetas[posPlanet+1:]}""")
