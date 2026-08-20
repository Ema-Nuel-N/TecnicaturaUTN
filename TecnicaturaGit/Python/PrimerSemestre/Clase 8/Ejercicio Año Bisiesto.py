#Diseñar un programa que ingresado un año, nos devuelva
#por consola si es un año bisiesto o no, repetir la acción
#hasta que el usuario lo decida.
opcion = 0
while opcion != 1:
    print("Comprobamos qué año es Bisiesto")
    num = int(input("Ingrese el año: "))
    if ((num % 4 == 0) and (num % 100 != 0) or num % 400 == 0):
        print("El Año es Bisiesto")
    else:
        print("El Año no es Bisiesto")

    opcion = int(input("Para salir digite 1: "))