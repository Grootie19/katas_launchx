# Acomodar información sobre distintas lunas
# La información debe presentarse en un formato tabular eg.

# Gravity Facts about Ganymede
# -------------------------------------------------------------------------------
# Planet Name: Mars
# Gravity on Ganymede: 1.4300000000000002 m/s2

# Datos a utilizar
# Moon, gravedad 0.00162 km/s, planet Earth

satName = "Moon"
gravity = 0.00162
planetName = "Earth"

# satName = "Ganímedes"
# gravity = 0.00143
# planetName = "Marte"

# Titulo

titulo = (f"Gravity Facts about {satName}\n")

# Plantilla
datos = (f"""-----------------------------
Planet Name: > {planetName}
Gravity on {satName}: > {gravity*1000} m/s2""")

combText = (f"{titulo}{datos}")

print(combText)

# print (combText.format(satName = satName, gravity = gravity*1000, planetName = planetName))