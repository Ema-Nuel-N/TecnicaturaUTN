/*
Ejercicio 2: Leer un número e indicar si es positivo o
negativo. El proceso se repetira hasta que se introduzca
un cero 0
*/
package Ciclos02;

import java.util.Scanner;


public class Ejercicio02_Scanner {
    public static void main(String[] args) {
        int numero;
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if (numero > 0){
                System.out.println("El número "+numero+" es Positivo");
            }else{
                System.out.println("El número "+numero+" es Negativo");
            }
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa finalizo por ingresar 0");
    }
}
