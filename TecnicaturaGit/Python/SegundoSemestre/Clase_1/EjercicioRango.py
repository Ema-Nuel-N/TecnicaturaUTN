
#Sintaxis de range(inicio<opcional>, fin <requerido>,incremento <opcional>)

# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir los numeros divisibles entre 3
# Ejemplo de ejecución: 0, 3, 6, 9
# Solución:
print("Rango de 0 a 10 e imprimir numeros divisibles entre 3")
for num in range(11):
    if num % 3 == 0:
        print(num)

# Ejercicio 2: Crear un rango de números de 2 a 6
# Ejemplo de ejecución: 2,3,4,5,6
# Solución:
rango = range(2,7)
print("Rango de numeros de 2 a 6")
for num in rango:
    print(num)

# Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1
# Ejemplo de ejecución: 3,5,7,9
# Solución:
print("Rango de 3 a 10 con incremento de 2 en 2")
for num in range(3,10,2):
    print(num)
