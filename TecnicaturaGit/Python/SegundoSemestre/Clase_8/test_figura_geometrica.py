from Clase_8.FiguraGeometrica import FiguraGeometrica
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Creación de objeto clase Cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(8, "Azul")
cuadrado1.alto = 7
cuadrado1.ancho = cuadrado1.alto
print(cuadrado1)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()} Color: {cuadrado1.get_color()}')

print("Creación de objeto clase Rectangulo".center(50, "-"))
rectangulo1 = Rectangulo(3,9, "Rojo")
rectangulo1.ancho = 8
print(rectangulo1)
print(f'Cálculo del área del rectangulo: {rectangulo1.calcular_area()} Color: {rectangulo1.get_color()}')

# MRO = Method  Resolution Order
#print(rectangulo1.mro())

#figura1 = FiguraGeometrica() #No se puede instanciar, es abstracta
print(Cuadrado.mro())

