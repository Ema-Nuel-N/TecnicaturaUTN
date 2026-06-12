
import java.util.Scanner;

public class Ejercicio9 {
    public static void main(String[] args) {
   
        try (Scanner teclado = new Scanner(System.in)){
            double compra;
            double descuento;
            double precioFinal;
            
            System.out.println("Digite la cantidad a pagar:");
            compra = teclado.nextDouble();
            
            if(compra > 100){
                descuento = compra * 0.20;                
            } else{
                descuento = 0;
            }
            
            precioFinal = compra - descuento;
            
            System.out.println("El precio a pagar es = " + precioFinal);
        }
        
    }
}
