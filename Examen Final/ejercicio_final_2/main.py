"""
2.
Utilizar el concepto de módulo necesariamente. Y escribir un programa
para el manejo de listas el cuál cumplirá los siguientes requerimientos (2 ptos):
Reglas:
-
Crear una función que le permitirá almacenar X números aleatorios
en una lista y finalmente los imprimirá por consola al llamar la función. X
solo puede ser entero. No otro tipo de dato. Y también un índice existente
en la lista (usar para esto excepciones)
-
Crear una función que le permita almacenar los números no repetidos
de la lista anterior, la función retornará este valor para que pueda
ser impreso por consola.
-
Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y
otra lista para ordenarlas de menor a mayor, retornar este valor e imprimirlos por consola.
-
Crear una función para indicar cuál es el mayor número par de
la lista (lista de la regla 2), retornar este valor e imprimirlo por consola.
-
Crear el archivo main.py,
"""

from funciones import genera_lista, no_repetidos, ordenar

try:
    total = int(input("Ingrese Cantidad de números aleatorios: "))
except ValueError:
    print("Debe ingresar un número entero.")

lista = genera_lista(total)

lista_sin_repetidos = no_repetidos(lista)

ordenar(lista_sin_repetidos)

