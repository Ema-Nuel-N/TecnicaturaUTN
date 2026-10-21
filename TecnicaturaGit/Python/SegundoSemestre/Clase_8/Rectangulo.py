from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, largura, altura, color):
        FiguraGeometrica.__init__(self, largura, altura)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.get_ancho() * self.get_alto()

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}'