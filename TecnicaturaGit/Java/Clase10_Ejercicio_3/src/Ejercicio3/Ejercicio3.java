package Ejercicio3;
import java.util.Scanner;
public class Ejercicio3 {
    public static void main(String[] args) {
        /*Ejercicio 3: La calificacion final de un estudiante de informática

se calcula con base a las calificaciones de cuatro aspectos de su

rendimiento académico: participación, primer examen parcial, segundo

examen parcial y examen final. Sabiendo que las calificaciones anteriores

entran a la calificación final con ponderaciones de 10%, 25%, 25%

y 40%, Hacer un programa que calcule e imprima la calificación final

obtenida por un estudiante. 

Que el usuario digite las calificaciones de estos 4 datos y así podremos tener,

la calificación final.


*/
        Scanner entrada = new Scanner(System.in);
        System.out.print("A continuación digita las notas de ");
        
        System.out.print("Participación: ");
        double participacion = entrada.nextDouble();
        
        System.out.print("Primer Examen: ");
        double primer_examen = entrada.nextDouble();
        
        System.out.print("Segundo Examen: ");
        double segundo_examen = entrada.nextDouble();
        
        System.out.print("Examen Final: ");
        double examen_final = entrada.nextDouble();
        
        double calFinal = ((participacion * 0.10) 
                + (primer_examen * 0.25) 
                + (segundo_examen * 0.25) 
                + (examen_final * 0.40));
        System.out.print("\ncalFinal = " + calFinal + "\n");
    }
}
