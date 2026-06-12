//Ejercicio 1: Calcular estación del año
/*
let mes = 4;
let estacion;
if (mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
}
else if (mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if (mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if (mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Valor incorrecto";
}
console.log("El valor correspondiente a la estación es: " + estacion)

//Ejercicio 2: Hora del día
/*
de 6 a 11 nos saluda: Good Morning
de 12 a 16 nos saluda: Good Afternoom
de 17 a 19 nos saluda: Good Evening
de 20 a 23 nos saluda: Good Night
Trabajaremos con 24 horas

let horaDia = 23;
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Good Morning";
}
else if (horaDia >= 12 && horaDia <= 16){
    mensaje = "Good Afternoom";
}
else if (horaDia >= 17 && horaDia <= 19){
    mensaje = "Good Evening";
}
else if (horaDia >= 20 && horaDia <= 23){
    mensaje = "Good Night";
}
else {
    mensaje = "Valor incorrecto";
}
console.log(mensaje)

//Estructura switch(La sintaxis es igual a Java)
switch(mes){//No solo se puede utilizar números, también cadenas
    case 12: case 1: case 2:
        estacion = "Verano";
        break
    case 3: case 4: case 5:
        estacion = "Otoño"
        break
    case 6: case 7: case 8:
        estacion = "Invierno"
        break
    case 9: case 10: case 11:
        estacion = "Primavera"
        break
    default:
        estacion = "Valor incorrecto";
}
console.log("Bienvenido a la estación de: "+estacion)

//Evitar repetir tu codigo
//Dry don't repeat yourself
//let days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"];
let days = 7;
switch (days){
    case 1:
        console.log("Hoy es Lunes");
        break;
    case 2:
        console.log("Hoy es Martes");
        break;
    case 3:
        console.log("Hoy es Miércoles");
        break;
    case 4:
        console.log("Hoy es Jueves");
        break;
    case 5:
        console.log("Hoy es Viernes");
        break;
    case 6:
        console.log("Hoy es Sábado");
        break;
    case 7:
        console.log("Hoy es Domingo");
        break;
    default:
        console.log("Día inexistente");
}
//Esta es la opción mejorada
let days2 = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"];
function getDay(n){
    if (n < 1 || n > 7){
        throw new Error('Out of range')
    }
    return days2[n-1];
}
console.log(getDay(5))
*/
//Ejercicio: Meses del año con switch, deben simplificar y agregar eficacia con el concepto
//  Dry don't repeat yourself: Evitar repetir tu código
//  Crear una función como la de getDay para los meses del año
//Con switch (39 lineas de código)
let mes = 3;
switch (mes){
    case 1:
        console.log("Enero");
        break;
    case 2:
        console.log("Febrero");
        break;
    case 3:
        console.log("Marzo");
        break;
    case 4:
        console.log("Abril");
        break;
    case 5:
        console.log("Mayo");
        break;
    case 6:
        console.log("Junio");
        break;
    case 7:
        console.log("Julio");
        break;
    case 8:
        console.log("Agosto");
        break;
    case 9:
        console.log("Septiembre");
        break;
    case 10:
        console.log("Octubre");
        break;
    case 11:
        console.log("Noviembre");
        break;
    case 12:
        console.log("Diciembre");
        break;
    default:
        console.log("Mes inexistente");
    }
//Esta es la opción mejorada (8 lineas de código)
let meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
function getMonth(n){
    if (n < 1 || n > 12) {
        throw new Error('Out of range')
    }
    return meses[n-1];
}
console.log(getMonth(3))