//Ejercicio para encontrar números pares e impares
let parInpar = 10;
if(parInpar % 2 == 0){
    console.log("Es un numero par")
} 
else {
    console.log("Es un numero impar")
}

//Ejercicio: es mayor de edad
let edad = 18, adulto = 18;
if( edad >= adulto){
    console.log("Usted es una persona adulta")
}
else{
    console.log("Usted es una persona menor de edad")
}

//Ejercicio: Dentro de un rango
let dentoRango = 10; //Aquí vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if( dentoRango >= valMin && dentoRango <= valMax){
    console.log("Estas dentro del rango establecido")
}
else{
    console.log("Esta fuera del rango establecido")
}
//Ejercicio Puede asistir el padre al juego?
let vacaciones = false;
let dia_libre = false;
console.log("Puede el Padre asistir al juego?")
if (vacaciones || dia_libre) {
    console.log("Puede asistir al juego")
} 
else{
    console.log("No puede asistir al juego")
}
//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2)

let numero = 10;
resultado2 = numero % 2 == 0 ? "Par" : "Impar";
console.log(resultado2)

//Convertir String a Number
let miNumero = "17";//Es una cadena
console.log(typeof miNumero);

let edad2 = Number(miNumero);//Es una función 
console.log(typeof edad2);
//Funcion isNaN
if (isNaN(edad2)){//No es un número = is Not a Number(devuelve un resultado booleano)
    console.log("Esta variable no contiene solo numeros")
}else{
    if (edad2 >= 18){
        console.log("Puede votar");
    }else{
        console.log("Muy joven para votar");
    }
}

//Operador ternario
let resultado3 = edad2 >= 18 ? "Puede votar" : "Muy joven para votar";
console.log(resultado3)
