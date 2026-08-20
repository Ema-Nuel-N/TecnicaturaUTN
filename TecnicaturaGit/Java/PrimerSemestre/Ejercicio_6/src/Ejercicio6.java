
import java.util.Scanner;


public class Ejercicio6 {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite a continuación");
        System.out.println("Dolares de Guillermo: ");
        Double guille = entrada.nextDouble();
        
        Double luis = (guille / 2);
        Double juan = (luis/2)+(luis);
        System.out.println("Guillermo tiene = $" + guille);
        System.out.println("Luis tiene = $" + luis);
        System.out.println("Juan tiene = $" + juan);
    }
}
