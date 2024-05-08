from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = filter(lambda x: x % 2 == 0, lista)

suma_pares = reduce(lambda x, y: x + y, numeros_pares, 0)

print("Lista original:", lista)
print("Números pares:", list(numeros_pares))
print("Suma de números pares:", suma_pares)
