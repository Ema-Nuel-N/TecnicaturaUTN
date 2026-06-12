
import java.util.Scanner;


public class Ejercicio3 {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Ingrese la base del rectangulo: ");
        //double base = entrada.nextDouble();
        double base = Double.parseDouble(entrada.nextLine());
        
        System.out.println("Ingrese la altura del rectangulo: ");
        //double altura = entrada.nextDouble();
        double altura = Double.parseDouble(entrada.nextLine());
        
        double area = base * altura;
        double perimetro = 2 * (base + altura);
        
        System.out.println("Area: "+ area);
        System.out.println("Perimetro: "+ perimetro);
    }
}