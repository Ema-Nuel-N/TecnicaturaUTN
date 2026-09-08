# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por ejemplo:
# Si digita el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

num = int(input("Ingrese un numero para multiplicar: "))
lista = [1,2,3,4,5,6,7,8,9,10]
listaMulti = []
for numero in lista:
    listaMulti.append(numero * num)

print(listaMulti)