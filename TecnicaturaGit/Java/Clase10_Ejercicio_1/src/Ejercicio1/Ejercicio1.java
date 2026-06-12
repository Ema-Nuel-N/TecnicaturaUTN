package Ejercicio1;
import java.util.Scanner;
public class Ejercicio1 {
    public static void main(String[] args) {
        /*

Ejercicio 1: Construir un programa que, dado un número total de

horas, devuelve el número de semanas, días y horas equivalentes.

Por ejemplo dado un total de 1000 horas debe mostrar 5 semanas,

6 días y 16 horas.


 */
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Digite la cantidad de horas: ");
        var horasTotales = Integer.parseInt(entrada.nextLine());
        var semanas = (int)(horasTotales / 168);
        var moduloSemana = horasTotales % 168;  
       
        var dias = (int) (moduloSemana / 24);
        var moduloDias = moduloSemana % 24;
 
        var horas = moduloDias;
        
        System.out.println("El total es de: "+ semanas + " Semanas " + dias + " Días " + horas + " Horas.");
    }
}
