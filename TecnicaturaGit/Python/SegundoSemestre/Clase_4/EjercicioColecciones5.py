# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los números del 1 al 10, luego modificar los
# elementos de la lista multiplicandolos por un valor ingresado por el usuario

lista = list(range(1, 11))

multiplicar = int(input("Ingrese un numero que multiplique: "))

for numero in lista:
    print(numero * multiplicar)