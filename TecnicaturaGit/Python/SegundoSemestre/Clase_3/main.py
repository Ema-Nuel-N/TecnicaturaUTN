# Repaso de set o conjunto
# Para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1) #Preguntamos si el número 3 NO esta en el conjunto1

#Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Nos devuelve como respuesta un booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # la línea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elemento tienen en común
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) # Aquí preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si comparten elementos en común
print(conjunto1.isdisjoint(conjunto2)) #No hay cosas en común

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo':'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del diccionarioNuevo['Azul']
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ema': {'Edad': 19, 'Altura': 1.78},'Abril':[19, 1.59], 'Martina': [19, 1.62]}
print(diccionario2['Martina'])

seleccionArgentina = {
    10:{'Nombre': 'Lionel Messi', 'Edad': 39, 'Altura': 1.70, 'Precio': '50 Millones', 'Posición': 'Extremo Derecho'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    9:{'Nombre': 'Julían Álvarez', 'Edad': 26, 'Altura': 1.70, 'Precio': '120 Millones', 'Posición': 'Delantero Centro'},
    24:{'Nombre': 'Enzo Fernandez', 'Edad': 24, 'Altura': 1.78, 'Precio': '100 Millones', 'Posición': 'Mediocampista Central'},
    13:{'Nombre': 'Cristian Romero', 'Edad': 28, 'Altura': 1.85, 'Precio': '50 Millones', 'Posición': 'Defensa Central'},
    6:{'Nombre': 'Lisandro Martinez', 'Edad': 28, 'Altura': 1.75, 'Precio': '45 Millones', 'Posición': 'Defensa Central'},
    23:{'Nombre': 'Emiliano Martínez', 'Edad': 32, 'Altura': 1.95, 'Precio': '35 Millones', 'Posición': 'Arquero'},
    22:{'Nombre': 'Lautaro Martínez', 'Edad': 27, 'Altura': 1.74, 'Precio': '85 Millones', 'Posición': 'Delantero'},
    7:{'Nombre': 'Alexis Mac Allister', 'Edad': 26, 'Altura': 1.74, 'Precio': '70 Millones', 'Posición': 'Mediocampista'}

}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Como tarea agregar por lo menos 4 jugadores mas al diccionario: seleccionArgentina
print("Tenemos cargados en el diccionario la cantidad de: ", end="")
print(len(seleccionArgentina))

# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # Quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila quedo de la siguiente forma: {pila}')

# Colas con listas
# Estructura de datos de tipo fifo (first input / first output)
cola = ['Abril','Martina','Emanuel','Graciela','Monica']

# Agregamos elementos al final de la cola
cola.append('Ulises')
cola.append('Marcas')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el/la client@: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el/la client@: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el/la client@: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el/la client@: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el/la client@: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el/la client@: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el/la client@: {seRetira}')
print(cola)

