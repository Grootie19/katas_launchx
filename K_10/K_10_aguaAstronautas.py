from click import argument


def aguaRestante(astronautas, aguaR, diasR):
    for arg in [astronautas, aguaR, diasR]:
        try:
            # si es arg es un entero la siguiente operacion funciona
            argument / 10
        except TypeError:
            # TypeError sera iniciado solo si no hay el tipo de dato correcto
            # Arroja la misma exepcion pero con un mensaje de error
            raise TypeError(f"Todos los argumentos deben ser de tipo entero, y se recibio: '{arg}'")

    usoDiario = astronautas * 11
    usoTotal = usoDiario * diasR
    aguaTotalR = aguaR - usoTotal

    if aguaTotalR < 0:
        raise RuntimeError(f"El agua se acabará en menos de {diasR} dias,no es suficiente para los {astronautas} astronautas")

    return f"Despues de {diasR} dias quedaran {aguaTotalR} litros de agua"

print(aguaRestante("3", "200", None))