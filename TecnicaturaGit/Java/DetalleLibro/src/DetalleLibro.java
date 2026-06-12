
import java.util.Scanner;

public class DetalleLibro {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el nombre del libro: ");
        var titulo = entrada.nextLine();
        System.out.println("Digite el nombre del autor: ");
        var nombre = entrada.nextLine();
        System.out.println(titulo + " fue escrito por " + nombre);
}   
}
