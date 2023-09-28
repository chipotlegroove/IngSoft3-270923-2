def resta(lista_numeros):
    resta = lista_numeros[0]
    for numero in lista_numeros[1:]:
        resta -= numero
    return resta