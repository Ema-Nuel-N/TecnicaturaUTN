class Persona: # Creamos una clase

    def __init__(self, nombre, apellido, edad): # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} {self.apellido} {self.edad}")

persona1 = Persona("Emanuel","Nuñez",19) # Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f"El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Edad {persona1.edad}")

persona2 = Persona("Ariel","Betancud", 40)
print(f"El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Edad {persona2.edad}")

persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = 40
print(f"El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Edad {persona1.edad}")

# Los atributos son: características
# Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()