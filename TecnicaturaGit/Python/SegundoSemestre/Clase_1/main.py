# Lista = Ema , Abru , Natalia, Martu
nombres = ['Ema','Abru','Martu','Milo']
print(nombres)
'''
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1]) #Inverso para conocer el último
'''
print(nombres[0:2]) # Solo muestra el indice 0, 1 pero no el indice 2
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) # Indices a mostrar 0, 1, 2
# Desde el indice indicado hasta el final
print(nombres[1: ])
# Modificamos un valor
nombres[1] = "Abril"
nombres[2] = "Martina"
nombres[0] = "Emanuel"
print(nombres)
# Iterar una lista
for nombre in nombres: # nombre es singular, la lista es plural
    print(nombre)
#Preguntamos cuantos elementos tiene una lista
print(len(nombres)) #Le pasamos como parametro la lista
#Agregamos un elemento
nombres.append("Kiu")
print(nombres)
#Insertar un elemento en un indice especifico
nombres.insert(4, "Silver")
print(nombres)
nombres.insert(3, "Devora")
print(nombres)

#Eliminamos un elemento
nombres.remove("Devora")
print(nombres)

#Eliminar el ultimo elemento
nombres.pop()
print(nombres)

#Eliminar un indice especifico
del nombres[2]# del significa delete(eliminar)
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
del nombres
#print(nombres) #Aqui nos mostrara un error

#Definimos una Tupla
cocina = ("cuchara","cuchillo","tenedor")
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])
# Ejemplo
verduras = ("papa",)# Una tupla necesita aunque sea de un elemento la coma
# de lo contrario solo seria un tipo str (cadena)

# Recorremos los elementos de la tupla
for cocinar in cocina: #Print esta usando \n para saltos de líneas
    print(cocinar, end=" ") #Usamos end= para eliminar los saltos de líneas

cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print("\n",cocina)

#del cocina #Esto es para eliminar una tupla