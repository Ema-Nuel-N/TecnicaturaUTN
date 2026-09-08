import math # Importamos la clase math para hacer uso de la función sqrt(raíz cuadrada)
from turtledemo import nim

#Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) #Definimos la tupla
#Crear una lista que solo incluya los números menores a 5
#e imprima por consola [1, 3, 2]

lista = []
for i in tupla:
    if i < 5:
        lista.append(i)
print(lista)

# Ejerccicio de matemáticas
# Para sacar la raíz cuadrada de un número positivo
numero = int(input("Ingrese un numero: "))
while numero < 0:
    print("Error -> Debería ser un numero positivo")
    numero = int(input("Ingrese un numero: "))

print(f"\nSu raíz cuadrada es: {math.sqrt(numero):.2f}")
