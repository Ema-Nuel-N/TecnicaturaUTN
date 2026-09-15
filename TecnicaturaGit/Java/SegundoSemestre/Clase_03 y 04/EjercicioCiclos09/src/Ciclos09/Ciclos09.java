/* Ejercicio 09: Scanner y JOptionPane Pedir dia, mes y año de una fecha
e indicar si la fecha es correcta . Suponinedo que todos los meses tienen 30 días.
*/
package Ciclos09;

import javax.swing.JOptionPane;
public class Ciclos09 {
    public static void main(String[] args) {
         // Declaramos las variables
        int dia, mes, año;        

        // Leemos las cadenas y pedimos al usuario los datos
        dia = Integer.parseInt(JOptionPane.showInputDialog("Digiete el Dia: "));
        mes = Integer.parseInt(JOptionPane.showInputDialog("Digiete el Mes: "));
        año = Integer.parseInt(JOptionPane.showInputDialog("Digiete el Año: "));

        if ((dia >=1 && dia <=30) && (mes >= 1 && mes <= 12) && (año >0)){
            JOptionPane.showMessageDialog(null, "La fecha es correcta: " + dia + "/" + mes + "/" + año );
        }
        else{
            JOptionPane.showMessageDialog(null, "La fecha ingresada es incorrecta, uno o mas datos ingresados no son correctos");
        }
    }
        
}
