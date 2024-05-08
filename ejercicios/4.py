from functools import reduce

lista = [1, 5, 9, 3, 7, 2]
valor_dado = 4

elementos_mayores = filter(lambda x: x > valor_dado, lista)

cantidad_elementos_mayores = reduce(lambda acc, _: acc + 1, elementos_mayores, 0)

print("Cantidad de elementos mayores que", valor_dado, "en la lista:", cantidad_elementos_mayores)
