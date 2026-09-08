/*
Ejercicio 6: Pedir números hasta que se teclee un 0, mostrar
la suma de todos los números introducidos.
*/
package Ciclos06;

import java.util.Scanner;
        
public class Ciclos06 {
    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        
        System.out.println("Digite un número para sumarlo: ");
        
        int num = Integer.parseInt(teclado.nextLine());        
        int suma = 0;
        
        while (num != 0){
            suma+= num;
            System.out.println("Digite otro número para sumarlo (0 para terminar): ");
            num = Integer.parseInt(teclado.nextLine());  
        } 
        
        System.out.println("Suma total: "+ suma);
        
    }
    
}
