
package test;

import domain.Persona;

public class PersonaPrueba {
    
    private int contador;
    
    public static void main(String[] args) {
        Persona persona1 = new Persona("Abril");
        System.out.println("persona1 = " + persona1);

        Persona persona2 = new Persona("Emanuel");
        System.out.println("persona2 = " + persona2);
        
        imprimir(persona1);
        imprimir(persona2);
        //this.contador; //No se puede referenciar desde un contexto estático
        PersonaPrueba personaP1 = new PersonaPrueba();
        System.out.println(personaP1.contador);
    }
    
    public static void imprimir(Persona persona){
        System.out.println("persona = " + persona);
    }
    
    public int getContador(){
        imprimir(new Persona("Liliana"));
        return this.contador;
    }
}
