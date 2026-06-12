#Ejercicio 1: Calcular la suma "N" Primeros Números

num = int(input("Digite la cantidad de números a sumarse: "))

suma = 0

for i in range(num):
    suma += 1

print(f"La suma es: {suma}")