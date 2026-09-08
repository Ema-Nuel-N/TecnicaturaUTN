/*
Ejercicio3: Leer números hasta que se introduzca un cero
Para cada uno indicar si es par o impar.
Primero lo haremos con la clase Scanner
Luego con la clase JOptionPane
*/
package Ciclos03;
import java.util.Scanner;
        
        
public class Ejercicio03 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int numero;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(teclado.nextLine());
        while (numero != 0){
            if (numero % 2 == 0){
               System.out.println("Tu número es par");
            }
            else{
               System.out.println("Tu número es impar");
            }
            System.out.println("Digite otro número (0 para salir): ");
            numero = Integer.parseInt(teclado.nextLine());
        }
     
    }
}
