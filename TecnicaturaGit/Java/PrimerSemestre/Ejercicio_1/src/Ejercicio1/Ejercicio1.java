//Tienda de libros
package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el nombre del Libro: ");
        String nombreLibro = entrada.nextLine();        
        System.out.println("Digite el ID: ");
        int libroId = Integer.parseInt(entrada.nextLine());       
        System.out.println("Digite el precio: ");
        double precioLibro = Double.parseDouble(entrada.nextLine());               
        System.out.println("Envio gratuito? (true or false): ");
        boolean envioGratis = Boolean.parseBoolean(entrada.nextLine());
       
        System.out.println(nombreLibro+" #"+libroId);
        System.out.println("Precio del libro: $"+ precioLibro);
        System.out.println("El envio del libro gratuito es: "+envioGratis);
    }
}
