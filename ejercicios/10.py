from functools import reduce

lista_de_cadenas = ["Hola", " ", "mundo", "!"]

cadena_concatenada = reduce(lambda x, y: x + y, lista_de_cadenas, "")

print("Lista de cadenas:", lista_de_cadenas)
print("Cadena concatenada:", cadena_concatenada)
