class Aritmetica:
    """
    El nombre de este tipo de comentario es: DocString
    esto es documentación de la clase en python
    Vamos a hacer en esta clase algunas operaciones de: suma, resta, multiplicacion y más
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    #Método para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    #Método para restar
    def restar(self):
        return self.operandoA - self.operandoB

    #Método para multiplicar
    def multiplicar(self):
        return self.operandoA * self.operandoB

    #Método para dividir
    def dividir(self):
        return self.operandoA / self.operandoB
#Suma
aritmetica1 = Aritmetica(7, 9) # Le pasamos los argumentos para los operandos
print(f"La suma de los números es: {aritmetica1.sumar()}")

#Resta
print(f"La resta de los números es: {aritmetica1.restar()}")

#Multiplicación
print(f"La multiplicación de los números es: {aritmetica1.multiplicar()}")

#División
print(f"La división de los números es: {aritmetica1.dividir():.2f}") # :.2f es para que muestre solo 2 números luego de la coma

