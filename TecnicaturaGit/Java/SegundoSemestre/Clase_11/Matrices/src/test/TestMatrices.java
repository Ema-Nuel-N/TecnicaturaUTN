
package test;

import domain.Persona;

public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int[3][2];
        System.out.println("edades = " + edades);
        edades[0][0] = 5; //Llenado manual
        edades[0][1] = 7; //Es una diferente columna
        edades[1][0] = 8;
        edades[1][1] = 4;
        edades[2][0] = 2;
        edades[2][1] = 3;
        
        System.out.println("edades 0-0 = " + edades[0][0]);
        System.out.println("edades 0-1 = " + edades[0][1]);
        System.out.println("edades 1-0 = " + edades[1][0]);
        System.out.println("edades 1-1 = " + edades[1][1]);
        System.out.println("edades 2-0 = " + edades[2][0]);
        System.out.println("edades 2-1 = " + edades[2][1]);
        System.out.println("Recorremos la matriz a través del ciclo for");
        for (int filas = 0; filas < edades.length; filas++) {
            for (int col = 0; col < edades[filas].length; col++) {
                System.out.println("edades "+filas+"-"+col+": "+edades[filas][col]);
            }
        }
        //Sintaxis Clásica
        //String frutas[][] = new String [3][2];
        
        //Sintaxis Simplificada
        String frutas [][] = {{"Limón","Pomelo"},{"Ciruela","Kiwi"},{"Banana","Manzana"}};
        imprimir(frutas);
        
//        for (int i = 0; i < frutas.length; i++) {
//            for (int j = 0; j < edades[i].length; j++) {
//                System.out.println("edades "+i+"-"+j+": "+frutas[i][j]);
//            }
//        }
        
        //Creamos una matriz de objetos
        Persona personas[][] = new Persona[2][3];
        //Asignamos valores a la matriz
        personas[0][0] = new Persona("Emanuel");
        personas[0][1] = new Persona("Marta");
        personas[0][2] = new Persona("Pepe");
        personas[1][0] = new Persona("Pato");
        personas[1][1] = new Persona("Tobi");
        personas[1][2] = new Persona("Lana");
        imprimir(personas);
    }
   
    public static void imprimir(Object matriz[][]){
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.println("matriz "+i+"-"+j+": "+matriz[i][j]);
            }
        }        
    }
}
