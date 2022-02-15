# Crea la lista de planetas
planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Neptuno']

namePlanet = input("Planeta que buscamos: ") 

planetasL = []

for planetaM in planetas[0:]:
    planetasL.append(planetaM.lower())
    print(planetasL)