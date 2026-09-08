# Ejercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo

num = int(input("Ingrese un numero para calcular el factorial: "))
while num < 0:
    print("Error -> Debería ser un numero positivo")
    num = int(input("Ingrese un numero para calcular el factorial: "))

resultado = 1
for i in range(1, num+1):
    resultado *= i

print(f"El factorial es: {resultado}")