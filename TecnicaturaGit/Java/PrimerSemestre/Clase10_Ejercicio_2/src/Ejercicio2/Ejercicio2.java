package Ejercicio2;
import java.util.Scanner;
 
public class Ejercicio2 {
    public static void main(String[] args) {
        /*

Ejercicio 2: Hacer un programa que calcule el cuadro de una suma,

el usuario debe ingresar el valor de a y el valor de b.

Formula: (a+b)2=a2+b2+2*a*b

Para esto deberán utilizar la clase Math y un método llamado pow


 */
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Digite el valor de A:");
        double a = entrada.nextDouble();
        System.out.print("Digite el valor de B:");
        double b = entrada.nextDouble();
        
        var formula = Math.pow((a + b), 2);
        var formulaDirecta = Math.pow(a, 2) + Math.pow(b,2) + (2*a*b);
        System.out.println("formula = "+formula);
        System.out.println("formulaDirecta = " + formulaDirecta);
    }
    
}
