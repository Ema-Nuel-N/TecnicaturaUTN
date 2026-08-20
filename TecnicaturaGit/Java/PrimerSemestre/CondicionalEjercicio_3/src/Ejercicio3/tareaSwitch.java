package Ejercicio3;
import java.util.Scanner;
public class tareaSwitch {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un número de 0 al 10:");
        var calificaciones = Integer.parseInt(entrada.nextLine());
        var calificacion = "Calificación Desconocida";
        switch(calificaciones){
            case 0: case 1: case 2: case 3: case 4: case 5:
                calificacion = "F";
                break;
            case 6:
                calificacion = "D";
            case 7:
                calificacion = "C";
            case 8:
                calificacion = "B";
            case 9: case 10:
                calificacion = "A";
        }
        System.out.println("calificacion = " + calificacion);
    }
}
