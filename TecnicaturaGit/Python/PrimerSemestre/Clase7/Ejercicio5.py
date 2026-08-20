num = float(input("Ingrese un valor del 0 al 10: "))
if 9 == num == 10:
    print("Calificación A")
elif 8 <= num < 9:
    print("Calificación B")
elif 7 <= num < 8:
    print("Calificación C")
elif 6 <= num < 7:
    print("Calificación D")
elif 0 <= num < 6:
    print("Calificación F")
else:
    print("Valor ingresado: Invalido")