# Tipos int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (String)
miGrupoFavorito = "Nirvana:"
caracteristicas = "The Best Rock Band"
print("Mi grupo favorito es:",miGrupoFavorito,caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

#Tipos Boleanos (bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# Funcion input
#resultado = input("Digite un número: ")# regresa un dato tipo string
#print(resultado)

#Conversion de la entrada de datos
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ",resultado)
