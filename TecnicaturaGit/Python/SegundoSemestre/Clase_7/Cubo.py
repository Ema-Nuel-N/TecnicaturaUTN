class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad, con
    un método calcular_volumen que tendrá la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores.
    """
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

    def mostrar_detalle(self):
        print(f"El volumen es: {self.calcular_volumen()}")

cubo1 = Cubo(int(input("Digite el ancho: ")),int(input("Digite la altura: ")),int(input("Digite la profundidad: ")))
cubo1.mostrar_detalle()
