
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo",57.000,false);
//        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //Modificar a través de los métodos
        System.out.println("persona1: "+persona1);
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; //Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre); //Error
//        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
//        System.out.println("persona1 el resultado para su sueldo: "+persona1.getSueldo());
//        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());        
        System.out.println("persona1: "+persona1);
        //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial
        //y imprimir, luego modificar sus valores y volver a imprimir
        
        Persona persona2 = new Persona("Emmanuel Nunes",100.000,true);
//        System.out.println("El nombre de persona2 es: "+persona2.getNombre());
//        System.out.println("El sueldo de persona2 es: "+persona2.getSueldo());
//        System.out.println("persona2 está eliminado?: "+persona2.isEliminado());
        System.out.println("persona2: "+persona2); //Método toString para imprimir Facilmente todo
//        //Modificacion de sus valores
        persona2.setNombre("Emanuel Nuñez");
        persona2.setSueldo(950.000);
        persona2.setEliminado(false);
//        //Impresión de los nuevos valores
//        System.out.println("El nombre de persona2 es: "+persona2.getNombre());
//        System.out.println("El sueldo de persona2 es: "+persona2.getSueldo());
//        System.out.println("persona2 está eliminado?: "+persona2.isEliminado());
//        

        System.out.println("persona2: "+persona2);
    }
    
}
