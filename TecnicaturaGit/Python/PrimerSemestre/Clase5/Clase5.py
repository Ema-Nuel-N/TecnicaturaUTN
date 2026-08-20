# Operadores Lógicos

a = False
b = True
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)

# Ejercicio: Valor dentro de un rango

valor = int(input("Digite un número: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo) and valor <= valorMaximo
if dentroRango:
    print(f"El valor {valor} esta dentro del rango")
else:
    print(f"El valor {valor} no esta dentro del rango")

# Ejercicio con el operador or, Operador not

vacaciones = False
diaDescanso = False
if  not (vacaciones or diaDescanso):
    print("Tiene trabajo que hacer")
else:
    print("Puede asistir al juego")