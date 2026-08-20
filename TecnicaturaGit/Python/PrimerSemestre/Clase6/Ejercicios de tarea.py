import math
'''
#Ejercicio 1:
a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))
operacion = ((3+5*8)< 3 and ((-6/3 * 4) + 2 < 2)) or (a > b)
if operacion == True:
    print(f"Operacion Logica {operacion}")
elif operacion == False:
    print(f"Operacion Logica {operacion}")
'''
'''
#Ejercicio 2:
a = 10
b = 5
c = a

a = b
b = c
print(f'''
#        {a}
#        {b}
''')
'''
#Ejercicio 3:

radio = float(input("Digite el valor de radio: "))

area = math.pi * (radio**2)
long = 2 * math.pi * radio

print(f'''
        Área: {area}
        Longitud: {long}

''')
