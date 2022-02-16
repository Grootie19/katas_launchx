# Creación del diccionario

planeta = {
    'nombre' : 'Mars',
    'lunas' : 2
}

planeta.update ({
    'circunferencia (km)' : {
        'polar' : 6752,
        'equatorial' : 6792
    }
})

print(f"Nombre del planeta: {planeta['nombre']}\nNumero de lunas: {planeta['lunas']}\nSu Circunferencia es:\n    >Polar: {planeta['circunferencia (km)']['polar']}\n    >Equatorial: {planeta['circunferencia (km)']['equatorial']}")
