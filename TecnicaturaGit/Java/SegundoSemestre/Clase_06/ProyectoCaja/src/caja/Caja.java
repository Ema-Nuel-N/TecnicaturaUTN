package caja;

public class Caja {
    double ancho;
    double alto;
    double profundidad;
    
    //Método para sacar el volumen
    

    
    public double sacarElVolumen(double ancho, double alto, double profundidad){
        
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
        return this.calcularVolumen();
    }
    
        public double calcularVolumen(){
        double volumen = ancho * alto * profundidad;
 
        return volumen;
    }
}

