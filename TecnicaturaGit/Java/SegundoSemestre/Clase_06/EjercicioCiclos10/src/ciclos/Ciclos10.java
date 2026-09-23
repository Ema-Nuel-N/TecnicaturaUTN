/*
Ejercicio 10: Pedir 10 números y escribir la suma total
Hacerlo con la clase Scanner y JOptionPane
*/
package ciclos;

import java.util.Scanner;

public class Ciclos10 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        
        int num, suma = 0;
        for (int i = 1; i <= 10; i++){
            System.out.println("Digite un número: ");
            num = Integer.parseInt(teclado.nextLine());
            suma += num;
        }
        System.out.println("\nLa suma total es: "+suma);
    }
}
