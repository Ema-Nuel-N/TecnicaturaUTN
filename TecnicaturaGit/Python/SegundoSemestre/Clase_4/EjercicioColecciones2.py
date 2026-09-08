# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuación
# cree las siguientes listas (en las que no deben haber repetición)
# 1 Lista de palabras que aparece en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas

lista1 = ["python", "java", "javascript", "html", "css"]
lista2 = ["python", "java", "c++", "php", "css"]

lista1 = set(lista1)
lista2 = set(lista2)

print(f"Todas las listas son: {lista1 | lista2}")
print(f"Solo la primera lista {lista1 - lista2}")
print(f"Solo la segunda lista {lista2 - lista1}")
print(f"lista de palabras que aparecen en ambas: {lista1 & lista2}")