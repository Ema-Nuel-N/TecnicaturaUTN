# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro
# de un rango, por ejemplo:
#                           suma de números pares del 2 al 30
#                           suma = 240
num1 = int(input("Ingrese el inicio del rango: "))
num2 = int(input("Ingrese el final del rango: "))
lista = list(range(num1, num2+1))
suma = 0
for numero in lista:
    if numero % 2 == 0:
        suma += numero

print(f"En el rango entre {num1} y {num2}, la suma de números pares total es: {suma}")