
import java.util.Scanner;


public class Ejercicio5 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        System.out.println("Vamos a sumar tus notas!!");
        
        System.out.println("Digite su primera Calificacion: ");
        Double priCal = Double.parseDouble(entrada.nextLine());
        
        System.out.println("Digite su segunda Calificacion: ");
        Double segCal = Double.parseDouble(entrada.nextLine());
        
        System.out.println("Digite su tercera Calificacion: ");
        Double terCal = Double.parseDouble(entrada.nextLine());
        
        Double resultado = (priCal + segCal + terCal);
        System.out.println("Su suma total de las notas: " + resultado);
    }
    
}
