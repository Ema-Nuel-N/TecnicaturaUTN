from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(5, "Azul")
print(cuadrado1)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()} Color: {cuadrado1.get_color()}')

rectangulo1 = Rectangulo(5,3, "Rojo")
print(rectangulo1)
print(f'Cálculo del área del rectangulo: {rectangulo1.calcular_area()} Color: {rectangulo1.get_color()}')

# MRO = Method  Resolution Order
#print(rectangulo1.mro())