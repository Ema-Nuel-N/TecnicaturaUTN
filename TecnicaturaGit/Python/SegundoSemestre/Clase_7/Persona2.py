class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre}, {self._apellido}, {self._edad}")

    @property
    def nombre(self): # Método Getter
        print('Estamos utilizando el método get')
        return self._nombre

    @property
    def apellido(self):
        print('Estamos utilizando el método get')
        return self._apellido

    @property
    def edad(self):
        print('Estamos utilizando el método get')
        return self._edad

    @nombre.setter
    def nombre(self,nombre): #Método Setter
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @apellido.setter
    def apellido(self,apellido):
        print('Estamos utilizando el método set')
        self._apellido = apellido

    @edad.setter
    def edad(self,edad):
        self._edad = edad

    def __del__(self):
        print(f'Persona5: {self._nombre}, {self._apellido}, {self._edad}')
if __name__ == '__main__':
    persona1 = Persona2 ('Ariel', 'Betancud', 41)
    print(persona1.nombre) # Llamamos al método getter
    print(persona1.apellido)
    print(persona1.edad)

    persona1.nombre = 'Juan Pedro' # Llamamos al método setter
    print(persona1.nombre) # Otra vez con el método getter
    print(persona1.mostrar_detalle()) # Llamamos al método mostrar_detalles

    #Atributo read-only sería la edad porque no tiene el método set
    print(persona1.edad)

    persona2 = Persona2 ('Emanuel', 'Ramirez', 19)
    print(persona2.nombre) #Llamamos al método getter
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Marcelo' # Llamamos al método setter
    print(persona2.nombre)
    persona2.edad = 59
    print(persona2.edad)
    print(persona2.mostrar_detalle())

    persona3 = Persona2 ('Juan', 'Marcelo', 41)
    print(persona3.nombre) #Llamamos al método getter
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Emanuel'
    persona3.edad = 19
    print(persona3.mostrar_detalle())

    persona4 = Persona2 ('Juan', 'Marcelo', 41)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Adrian'
    persona4.edad = 59
    print(persona4.mostrar_detalle())

    print(__name__)
