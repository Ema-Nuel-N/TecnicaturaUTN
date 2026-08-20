
package Leccion2;

import java.util.Scanner;

public class Leccion2 {
    public static void main(String[] args) {
//        var condicion = true;
//        if (condicion){
//            System.out.println("Condición Verdadera");//condicional simple
//        }
//        else{
//            System.out.println("Condición Falsa");//Condicional doble
//        }
//        
//        var numero = 5;
//        var numeroTexto = "Número desconocido";
//        if (numero == 1){
//            numeroTexto = "Número Uno";
//        }
//        else if(numero == 2){
//            numeroTexto = "Número Dos";
//        }
//        else if (numero == 3){
//            numeroTexto = "Número Tres";
//        }
//        else if (numero == 4){
//            numeroTexto = "Número Cuatro";
//        }
//        else {
//            numeroTexto = "Número no encontrado";
//        }
//        
//        System.out.println("numeroTexto = " + numeroTexto);
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digita un número del 1 al 4:");
        var numero = Integer.parseInt(entrada.nextLine());
        var numTexto = "Número desconocido";
        switch(numero){
          case 1 :
              numTexto = "Número Uno";
              break;
          case 2 :
              numTexto = "Número Dos";
              break;
          case 3 :
              numTexto = "Número Tres";
              break;
          case 4 :
              numTexto = "Número Cuatro";
              break;
          default:
              numTexto = "Número desconocido";

        }
        System.out.println("numTexto = " + numTexto);
    }
}
