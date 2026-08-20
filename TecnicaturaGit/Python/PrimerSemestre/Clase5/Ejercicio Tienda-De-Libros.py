#Ejercicio: Tienda de libros
print("Digite los siguientes datos:")
nombre = input("Digite el nombre del libro: ")
id = int(input("Digite el ID del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indicar si el libro es gratuito (True/False): )")
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito == False
else:
    envioGratuito = "El valor es incorrecto, debe escribir True/False"
print(f'''
        Nombre: {nombre}
        ID: {id}
        Precio: {precio}
        Envio Gratuito?: {envioGratuito}
''')