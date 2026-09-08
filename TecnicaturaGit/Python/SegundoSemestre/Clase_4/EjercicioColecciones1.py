#Ejercicio 1: Eliminar duplicados de una lista
#Escriba un programa donde tenga una lista y que a continuación
#elimine los elementos repetidos, por ultimo mostrar la lista

lista = [1,2,2,2,3,3,4,5,6,6,7,8,9,9,10,12,11,10,]
print(f"Lista original: {lista}")
lista_sin_repetidos = list(set(lista))
print(f"Lista sin repetidos: {lista_sin_repetidos}")