/*
Ejercicio 10: Pedir 10 números y escribir la suma total
Hacerlo con la clase Scanner y JOptionPane
*/
package ciclos;
import javax.swing.JOptionPane;

public class Ejercicio10 {
    public static void main(String[] args) {
        int num, suma = 0;
        for (int i = 1; i <= 10; i++){
            num = Integer.parseInt(JOptionPane.showInputDialog("Digite un número"));
            suma += num;
        }
        JOptionPane.showMessageDialog(null,"\nLa suma total es: "+suma);
    }
}
