import random

def genera_lista(numero):
    lista = []

    for n in range(numero):
        lista.append(random.randint(1, 50))
    print(lista)
    return lista

def no_repetidos(lista):
    no_repetidos = list(set(lista))
    print("Lista sin números repetidos:", no_repetidos)
    return no_repetidos

def ordenar(lista):
    ascendente = sorted(lista)
    descendente = sorted(lista, reverse=True)
    print("Lista descendente:", descendente)
    print("Lista ascendente:", ascendente)
    return descendente, ascendente