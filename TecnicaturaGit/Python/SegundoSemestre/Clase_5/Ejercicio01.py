# Ejercicio 10: No repetir carácteres
# Hacer un programa que pida por teclado, luego
# meter los caracteres en una lista sin repetir caracteres

lista = []

caracter = input("Escriba a continuación un carácter: ")
lista.append(caracter)

while True:
    caracter = input("Escriba otro carácter o digite x para salir: ")
    if caracter == "x":
        break
    lista.append(caracter)

lista_sin_repetidos = list(set(lista))
lista_sin_repetidos.sort()
print(f"La lista ordenada sin repetir carácteres es: {lista_sin_repetidos}")