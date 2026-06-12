
import java.util.Scanner;


public class Ejercicio7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        final double salario = 1000;
        System.out.println("Valor del Coche: $");
        double valCar = entrada.nextDouble();
        System.out.println("Cuantos carros vendió?: ");
        int carros = entrada.nextInt();
        double comision = carros * 150;
        double porCoche = (valCar * 5)/ 100;
        double valVenta = porCoche * carros;
        double resultado = salario + comision + valVenta; 
        System.out.println("Comision: $"+ comision);
        System.out.println("5% de la venta por cada coche: $" + porCoche);
        System.out.println("5% de la venta por todos los coches: $" + valVenta);        
        System.out.println("Salario mensual: $"+ resultado);
       
        
    }
}
