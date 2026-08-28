/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo,
y mostrar cuántos números se han introducido.
Lo hacemos primero con la clase Scanner
Luego lo hacemos con la clase JOptionPane
*/
package Ciclo04;
import javax.swing.JOptionPane;

public class Ejercicio04JOption {
    public static void main(String[] args) {
        
        String numeros = "";
        
        String numero = JOptionPane.showInputDialog("Digite un número: ");
        
        while (Integer.parseInt(numero) >= 0){
            numeros = numeros + numero + ", ";
            numero = JOptionPane.showInputDialog("Digite un número para almacenarlo(negativo para finalizar): ");
        }
        JOptionPane.showMessageDialog(null,"Los números son: "+numeros);
    }
}
