# Datos interesantes acerca de a Luna
# La Luna es el unico satelite natural del planeta Tierra
# Estos son los datos más interesantes sobre la Luna y como afecta la vida aquí en la Tierra
# En promedio, la Luna se aleja de la Tierras 4cm cada año.
# Este alejamiento anual no representa ningún efecto inmediato significativo para la Tierra.
# La temperatura más alta en un día puede ser de 127 C.
# text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth.
# On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

# Texto dato
text = """Interesting facts about the Moon. The Moon is Earth's only satellite.
There are several interesting facts about the Moon and how it affects life here on Earth.
On average, the Moon moves 4cm away from the Earth every year.
This yearly drift is not significant enough to cause immediate effects on Earth.
The highest daylight temperature of the Moon is 127 C."""

# Divide el texto en cada oración
divText = text.split('\n')
# print (divText)

# Define palabras clave para busqueda
firstkw = 'average'
secondkw = 'temperature'
thirdkw = 'distance'

# Imprime los datos que contengan alguna de las pralabras claves
for fact in divText:
    factMin = fact.lower()
    if factMin.count(firstkw) > 0 or factMin.count(secondkw) or factMin.count(thirdkw):
        if factMin.endswith("c."):
            fact = fact.replace('C', 'Celsius')
        print(f"> {fact}")

