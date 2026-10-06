class Persona: # Creamos una clase

    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llama método Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni # Este atributo esta encapsulado de manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): # self es igual a this
        print(f"La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.edad} {self._dni}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}")


persona1 = Persona("Emanuel","Nuñez", 47683345,19) # Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f"El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Edad {persona1.edad}")

persona2 = Persona("Ariel","Betancud", 28682235,45)
print(f"El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Edad {persona2.edad}")

persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = 40
print(f"El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Edad {persona1.edad}")

# Los atributos son: características
# Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o nos dara error
persona1.telefono = 12342123 # Creamos un atributo local, únicamente para el objeto persona1, no se comparte
print(f"Este es el teléfono de {persona1.nombre}: {persona1.telefono}")

#print(persona2.telefono) El objeto persona2 no tiene este atributo, da error
persona3 = Persona('Rogelio','Romero', 29432254, 22, 'Telefono', '261114232', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso =105, CFavorito='Negro', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()
# print(persona3._dni) #Esto no se debe de utilizar (Está encapsulado), esto dice que desconocemos python
# persona3.__nombre # Está totalmente encapsulado