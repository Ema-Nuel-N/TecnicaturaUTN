
import java.util.Scanner;


public class Ejercicio4 {
    
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Ingrese el primer numero: ");
        int num1 = Integer.parseInt(entrada.nextLine());
        
        System.out.println("Ingrese el segundo numero: ");
        int num2 =Integer.parseInt(entrada.nextLine());
        
        String msj = "Los números son iguales";
        
        int mayor = (num1 > num2) ? num1 : num2;
        var resultado = (num1 == num2) ? msj : mayor;

        if (resultado == msj){
            System.out.println(msj);
        } else {
            System.out.println("El mayor es: "+ mayor);
        }
     
           
        
        entrada.close();
    }
}
