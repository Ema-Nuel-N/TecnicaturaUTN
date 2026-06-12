# Ejercicio 5 : Calcular el factorial de un número mayor o igual a 0.

num = int(input("Ingrese un numero: "))

while num < 0:
    print("El número debe ser mayor o igual a 0")
    num = int(input("Ingrese un numero: "))

i = 1
factorial = 1

while i <=num:
    factorial *= i
    i += 1

print(f"El factorial es: {factorial}")