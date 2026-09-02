/*
Ejercicio 5: Realizar un juego para adivinar un número,
para ello generar un número aleatorio entre 0-100, y 
luego ir pidiendo números indicando "es mayor" o 
"es menor" según sea mayor o menor con respecto a N 
El proceso termina cuando el usuario acierta y mostramos
el número de intentos hechos.
*/
package Ciclos05;
import javax.swing.JOptionPane;


public class Ejercicio05JOption {
    public static void main(String[] args) {
        int min = 0;
        int max = 100;
        int numPlayer;
        int contador = 1;
        int numero = (int)(Math.random() * (max - min + 1)) + min;
        
        JOptionPane.showMessageDialog(null,"Vamos a jugar a un juego, tenes que adivinar mi número");
        JOptionPane.showMessageDialog(null,"te voy a dar pistas hasta que lo encuentres!! :)");
        numPlayer = Integer.parseInt(JOptionPane.showInputDialog("Probá un número: "));
        while(numPlayer != numero){
            contador++;
            if (numPlayer > numero){
                JOptionPane.showMessageDialog(null,"es menor");
            }
            else{
                JOptionPane.showMessageDialog(null,"es mayor");
            }
            numPlayer = Integer.parseInt(JOptionPane.showInputDialog("Proba otro número: "));
        }
        JOptionPane.showMessageDialog(null,"Adivinaste!! mi número era "+numero+", Número de intentos: "+contador);
              
    }
}
