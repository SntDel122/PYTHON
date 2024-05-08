from functools import reduce

lista = [1, 5, 9, 3, 7, 2]

maximo = reduce(lambda x, y: x if x > y else y, lista)

print("El máximo elemento de la lista es:", maximo)
