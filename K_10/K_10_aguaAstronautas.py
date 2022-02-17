def aguaRestante(astronautas, aguaR, diasR):
    usoDiario = astronautas * 11
    usoTotal = usoDiario * diasR
    aguaTotalR = aguaR - usoTotal

    if aguaTotalR < 0:
        raise RuntimeError(f"El agua se acabará en menos de {diasR} dias,no es suficiente para los {astronautas} astronautas")

    return f"Despues de {diasR} dias quedaran {aguaTotalR} litros de agua"

print(aguaRestante(5, 100, None))