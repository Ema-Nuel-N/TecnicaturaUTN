package caja;

public class PruebaCaja {
    public static void main(String[] args) {   
        
        Caja caja1 = new Caja();
        double ancho = 4;
        double alto = 8;
        double profundidad = 2;
        
        double resultado = caja1.sacarElVolumen(ancho, alto, profundidad);
        System.out.println("El volumen es: "+resultado);
    }
}
