#Segundo Ejercicio Calcular Las Notas Promediadas
nota1 = float (input("ingresa la nota a calificar"))
nota2 = float (input("ingresa la nota a calificar"))
nota3 = float (input("ingresa la nota a calificar"))

peso1 = 0.36
peso2 = 0.29
peso3 = 0.33

#Obtener promedio de notas
promedio = (nota1 * peso1)+(nota2 * peso2)+(nota3 * peso3)

#Imprimir el resultado del promedio
print("Promedio total del estudiante en la asignatura es", promedio)