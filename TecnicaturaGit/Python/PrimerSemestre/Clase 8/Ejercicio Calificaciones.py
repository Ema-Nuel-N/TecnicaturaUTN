suma = 0
calificaciones_baja = 99999

for i in range(10):
    print(i + 1, ". Digite una calificación:")
    calificacion = float(input())

    suma += calificacion

    if calificacion < calificaciones_baja:
        calificaciones_baja = calificacion

calificacion_promedio = suma / 10

print(f"La calificación es: {calificacion_promedio}")
print(f"La calificación más baja es: {calificaciones_baja}")