# Ejercicio 8: Menú interactivo - Cajero automático
# Hacer un programa que simule un cajero automático con un saldo
# inicial de 1000$ y tendrá el siguiente menú de opciones:
#                1. Ingresar dinero en la cuenta
#                2. Retirar dinero de la cuenta
#                3. Mostrar dinero disponible
#                4. Salir
import time

saldoInicial = 1000
billetera = 0
opcion = int(input((f"""
                    Bienvenido a su cajero automático favorito!!!
                    ¿Que movimientos quiere hacer hoy?
                                    
                    1- Ingresar dinero en la cuenta
                    2- Retirar dinero en la cuenta
                    3- Mostrar dinero disponible
                    4- Salir

                    >""")))

while opcion > 4:
    print("Error -> Debería ser un número entre 1 y 4")
    opcion = int(input(f"""
                    Bienvenido a su cajero automático favorito!!!
                    ¿Que movimientos quiere hacer hoy?
                                    
                    1- Ingresar dinero en la cuenta
                    2- Retirar dinero en la cuenta
                    3- Mostrar dinero disponible
                    4- Salir
                                      
                    >"""))

while opcion != 4:

    match opcion:
        case 1:
            time.sleep(2)
            billetera = int(input((f"""
                            Cuanto desea ingresar?
                               
                            >""")))
            saldoInicial = saldoInicial + billetera
            time.sleep(2)

        case 2:
            time.sleep(2)
            billetera = int(input((f"""
                                    Cuanto desea retirar?
                                    
                                    >""")))
            saldoInicial = saldoInicial - billetera
            time.sleep(2)

        case 3:
            time.sleep(2)
            print(f"""
                        Su saldo actual es de: ${saldoInicial}                    
            """)
            time.sleep(2)

    opcion = int(input(f"""
                        Bienvenido a su cajero automático favorito!!!
                        ¿Que movimientos quiere hacer hoy?

                        1- Ingresar dinero en la cuenta
                        2- Retirar dinero en la cuenta
                        3- Mostrar dinero disponible
                        4- Salir
  
                        >"""))