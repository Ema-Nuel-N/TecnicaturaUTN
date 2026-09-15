/*
Ejercicio 8: Pedir un número N, y mostrar todos los números del 1 al N.
*/
package Ciclos08;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ciclos08 {
    public static void main(String[] args) {
        JOptionPane.showMessageDialog(null, "Como prefiere ejecutar el programa?");
        int opcion = Integer.parseInt(JOptionPane.showInputDialog("1. Scanner | 2. JOption"));
        
        while(opcion < 1 || opcion > 2){
            opcion = Integer.parseInt(JOptionPane.showInputDialog("Error -> Debería ser 1 o 2, vuelva a digitar la opción"));
        }
        
        if (opcion == 1){
            scanner();
        }else{
            JOption();
        }
        
        
        
        
    }    
        
        
    public static void scanner(){
        Scanner teclado = new Scanner(System.in);
            
        System.out.println("Inserte un número N: ");
        int n = Integer.parseInt(teclado.nextLine());
        
        for (int i = 1; i<n+1; i++){
            System.out.println(i);
        }
    }
    
    public static void JOption(){
        int num = Integer.parseInt(JOptionPane.showInputDialog("Inserte un número N:"));
        
        for (int i = 1; i <= num; i++){
            JOptionPane.showMessageDialog(null, i);
        }
    }
    
}


