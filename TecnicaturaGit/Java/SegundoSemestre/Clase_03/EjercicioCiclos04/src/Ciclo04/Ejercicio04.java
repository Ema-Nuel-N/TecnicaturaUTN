/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo,
y mostrar cuántos números se han introducido.
Lo hacemos primero con la clase Scanner
Luego lo hacemos con la clase JOptionPane
*/
package Ciclo04;
import java.util.Scanner;

public class Ejercicio04 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        String numeros = "";
        
        System.out.println("Digite un número para almacenarlo: ");
        String numero = teclado.nextLine();
        
        while (Integer.parseInt(numero) >= 0){
            numeros = numeros + numero + ", ";
            
            System.out.println("Digite un número para almacenarlo(negativo para finalizar): ");
            numero = (teclado.nextLine());
        }
        System.out.println("Los números son: "+numeros);
    }
}
