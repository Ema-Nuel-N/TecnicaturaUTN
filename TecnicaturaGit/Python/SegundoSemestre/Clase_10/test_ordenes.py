from Clase_10.Orden import Orden
from Clase_10.Producto import Producto

producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Zapatillas', 200.00)
producto4 = Producto('Buso', 500.00)
producto5 = Producto('Gorra Nike', 350.00)
producto6 = Producto('Blusa', 75.00)
producto7 = Producto('Sweter', 95.00)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4, producto5]

orden1 = Orden(productos1)
orden1.agregar_producto(producto6)
orden1.agregar_producto(producto7)
print(orden1)
print(f'Total de la orden {orden1.id_orden}: {orden1.calcular_total()}')
orden2 = Orden(productos2)
orden2.agregar_producto(producto6)
orden2.agregar_producto(producto2)
print(orden2)
print(f'Total de la orden {orden2.id_orden}: {orden2.calcular_total()}')

