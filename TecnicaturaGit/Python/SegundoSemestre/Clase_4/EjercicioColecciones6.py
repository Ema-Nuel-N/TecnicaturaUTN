# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario
# introduzca un número 0, nuestro programa dejaría de insertar.
# Por último, mostrar los números ordenados de menor a mayor

lista = []

while True:

    num = int(input("Ingrese un numero (0 para finalizar): "))
    if num == 0:
        break
    lista.append(num)

lista.sort()
for numero in lista:
    print(numero)