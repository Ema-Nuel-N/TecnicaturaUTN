/*
Ejercicio 5: Realizar un juego para adivinar un número,
para ello generar un número aleatorio entre 0-100, y 
luego ir pidiendo números indicando "es mayor" o 
"es menor" según sea mayor o menor con respecto a N 
El proceso termina cuando el usuario acierta y mostramos
el número de intentos hechos.
*/
package Ciclos05;
import java.util.Scanner;

public class Ejercicio05 {
    public static void main(String[] args) {
        int min = 0;
        int max = 100;
        int numPlayer;
        int contador = 1;
        int numero = (int)(Math.random() * (max - min + 1)) + min;
        
        Scanner teclado = new Scanner(System.in);
        
        System.out.println("Vamos a jugar a un juego, tenes que adivinar mi número");
        System.out.println("te voy a dar pistas hasta que lo encuentres!! :)");
        System.out.println("Proba un número: ");
        numPlayer = Integer.parseInt(teclado.nextLine());
        while(numPlayer != numero){
            contador++;
            if (numPlayer > numero){
                System.out.println("es menor");
            }
            else{
                System.out.println("es mayor");
            }
            System.out.println("Proba otro número: ");
            numPlayer = Integer.parseInt(teclado.nextLine());
        }
        System.out.println("Adivinaste!! mi número era "+numero+", Número de intentos: "+contador);
              
    }
}
