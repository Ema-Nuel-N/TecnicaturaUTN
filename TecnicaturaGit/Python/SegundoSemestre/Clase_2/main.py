#Tipo set
planetas = {'Marte','Jupiter','Venus'}
print(len(planetas)) #Usamos la función len = lenght significa largo

#Revisar si un elemento existe dentro del set
print('Venus' in planetas)

#Agregar un elemento
planetas.add('Tierra') #add es una función
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Venus') # Esta función ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard('Tierras') # Esta función no nos presenta ningún error
print(planetas)

# Limpiar set o conjunto
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
#print(planetas) # al eliminar nos muestra un error

# 'Maradona':10 Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administracón de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrolo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:
    print(termino)

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): # Estamos usando una función
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una función para acceder al valor
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario) # devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('PK')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario
#print(diccionario) # El diccionario se borro

# Concatenamos listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1 + lista2 # Concatenamos
print(lista3)

lista3.extend([7,8,9,1]) # Función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Función para ubicar en que indice esta el valor ingresado
# print(lista3.index(0)) # esto daría un error por no ser el elemento parte de la lista

# Como saber cuántos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay en la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento, en python es una función
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) # Ordenar descendentemente
print(lista3)

# Repaso de Tuplas
tupla = (4, 'Hola', 6.58,[1,2,3],4,'Hola') # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) # Acción booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tuplas a lista y de lista a tupla