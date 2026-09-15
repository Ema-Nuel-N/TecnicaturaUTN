# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# númericos, utilizando argumentos variables *args como parametros de la
# Función y agregar como resultado la suma de todos los valores pasados
# como argumento.
def sumar(*args):
    return sum(args)

resultado = sumar(1, 2, 3, 4, 5)
print(resultado)