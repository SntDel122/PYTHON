def es_par(n):
    return n % 2 == 0

#filtrar los numeros pares del rango del 1 al 50 y convertir el resultado en una lista
lista_pares = list(filter(es_par, range(1,50)))

#imprimir la lista de numeros pares
print(lista_pares)
