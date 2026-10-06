
class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tenér 2 atributos: altura y base
    el nombre del método será calcular_area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por
    el usuario y los objetos deben ser tres.
    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura

    def mostrar_detalle(self):
        print(f"El área del rectangulo es {self.calcular_area()}")

rectangulo1 = Rectangulo(int(input("Ingrese altura: ")), int(input("Ingrese base: ")))

rectangulo1.mostrar_detalle()

