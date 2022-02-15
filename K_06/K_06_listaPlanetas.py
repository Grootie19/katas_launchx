# Crear la lista de planetas

planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']

# Imprime la cantidad de planetas que conforman la lista
print(len(planetas))

# Agregar a Pluton
planetas.append('Pluton')

print(f"En tu lista hay {len(planetas)}, el ultimo es: {planetas[-1]}")