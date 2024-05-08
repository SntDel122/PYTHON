def multiple(numero):
    #primero declaramos una funcion condicional
    if numero % 5 == 0:
        #comprobamos si un numero es multiple de cinco
        return True
        #solo devolvemos true si lo es
    else:
        return False
    
numeros = [2,5,10,23,50,33]
resultados = []

#iterar sobre cada numero en la lista de "numeros"
for num in numeros:
    #llamar a la funcion 'multiple' y agregar el resultado
    resultados.append(multiple(num))

#imprimir los resultados
print(resultados)