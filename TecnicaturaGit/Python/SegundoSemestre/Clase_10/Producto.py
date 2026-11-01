class Producto:
    contador_productos = 0 #Variable de la clase

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1 #Aumento para la variable de clase
        self._id_Producto = Producto.contador_productos # Asignación desde la variable de clase
        self._nombre = nombre
        self._precio = precio

    #Métodos getters and setters
    @property
    def nombre(self):
        return self._nombre
    @property
    def precio(self):
        return self._precio
    @property
    def id_Producto(self):
        return self._id_Producto

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @precio.setter
    def precio(self,precio):
        self._precio = precio
    #Sobre escribimos el método str
    def __str__(self):
        return f'Id Producto: {self._id_Producto}, Nombre: {self._nombre}, Precio: {self._precio}'

if __name__ == '__main__':
    producto1 = Producto('Camiseta', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 150.00)
    print(producto2)