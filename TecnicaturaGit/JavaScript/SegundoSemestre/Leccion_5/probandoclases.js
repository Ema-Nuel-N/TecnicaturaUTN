class Persona {
    constructor(nombre, apellido, edad){
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    //get
    get nombre(){
        return this._nombre;
    }

    get apellido(){
        return this._apellido;
    }
    get edad(){
        return this._edad;
    }
    //set
    set nombre(nombre){
        this._nombre = nombre;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    set edad(edad){
        this._edad = edad;
    }
}

persona1 = new Persona("Emanuel","Nuñez", 19);
persona2 = new Persona("Abril","Aguirre", 19);
persona3 = new Persona("Martina","Cardozo", 19);

console.log(persona1);

console.log(persona2);

console.log(persona3);

//Get
console.log("-------------------------------------------------------------------------")
console.log("                               PERSONAS                                  ")
console.log("---------------------------------Get-------------------------------------")
console.log(persona1.nombre + " " + persona1.apellido + " " + persona1.edad + " años");
console.log(persona2.nombre + " " + persona2.apellido + " " + persona2.edad + " años");
console.log(persona3.nombre + " " + persona3.apellido + " " + persona3.edad + " años");

//Set
persona1.nombre = "Marcelo";
persona2.nombre = "Milagro";
persona3.nombre = "De los milagros";

console.log("---------------------------------Set-------------------------------------")
console.log(persona1.nombre + " " + persona1.apellido + " " + persona1.edad + " años");
console.log(persona2.nombre + " " + persona2.apellido + " " + persona2.edad + " años");
console.log(persona3.nombre + " " + persona3.apellido + " " + persona3.edad + " años");

class Alumno extends Persona {
    constructor(nombre, apellido, edad, grado){
        super(nombre, apellido, edad);
        this._grado = grado;
    }

    get grado(){
        return this._grado;
    }

    set grado(grado){
        this._grado = grado;
    }
}

alumno1 = new Alumno("Emanuel","Nuñez", 19, "5to");
alumno2 = new Alumno("Abril","Aguirre", 19, "5to");
alumno3 = new Alumno("Martina","Cardozo", 19, "5to");

//Get
console.log("-------------------------------------------------------------------------")
console.log("                               ALUMNOS                                   ")
console.log("---------------------------------Get-------------------------------------")
console.log(alumno1.nombre + " " + alumno1.apellido + " " + alumno1.edad + " años" + " " + alumno1.grado);
console.log(alumno2.nombre + " " + alumno2.apellido + " " + alumno2.edad + " años" + " " + alumno2.grado);
console.log(alumno3.nombre + " " + alumno3.apellido + " " + alumno3.edad + " años" + " " + alumno3.grado);

//Set
console.log("---------------------------------Set-------------------------------------")
alumno1.nombre = "Marcelo";
alumno2.nombre = "Milagro";
alumno3.nombre = "De los milagros";

alumno1.edad = 20;
alumno2.edad = 20;
alumno3.edad = 20;

alumno1.grado = "6to";
alumno2.grado = "6to";
alumno3.grado = "6to";

console.log(alumno1.nombre + " " + alumno1.apellido + " " + alumno1.edad + " años" + " " + alumno1.grado);
console.log(alumno2.nombre + " " + alumno2.apellido + " " + alumno2.edad + " años" + " " + alumno2.grado);
console.log(alumno3.nombre + " " + alumno3.apellido + " " + alumno3.edad + " años" + " " + alumno3.grado);

class Profesor extends Alumno {
    constructor(nombre, apellido, edad, grado, materia){
        super(nombre, apellido, edad, grado);
        this._materia = materia;
    }

    get materia(){
        return this._materia;
    }

    set materia(materia){
        this._materia = materia;
    }
}

profesor1 = new Profesor("Emanuel","Nuñez", 26, "2do", "Programación");
profesor2 = new Profesor("Abril","Aguirre", 26, "2do", "Física");
profesor3 = new Profesor("Martina","Cardozo", 26, "2do", "Psicología");

//Get
console.log("-------------------------------------------------------------------------")
console.log("                               PROFESORES                                ")
console.log("---------------------------------Get-------------------------------------")
console.log(profesor1.nombre + " " + profesor1.apellido + " " + profesor1.edad + " años" + " " + profesor1.grado + " " + profesor1.materia);
console.log(profesor2.nombre + " " + profesor2.apellido + " " + profesor2.edad + " años" + " " + profesor2.grado + " " + profesor2.materia);
console.log(profesor3.nombre + " " + profesor3.apellido + " " + profesor3.edad + " años" + " " + profesor3.grado + " " + profesor3.materia);

//Set
console.log("---------------------------------Set-------------------------------------")
profesor1.nombre = "Marcelo";
profesor2.nombre = "Milagro";
profesor3.nombre = "De los milagros";

profesor1.edad = 30;
profesor2.edad = 30;
profesor3.edad = 30;

profesor1.grado = "6to";
profesor2.grado = "6to";
profesor3.grado = "6to";

profesor1.materia = "Programación Avanzada";
profesor2.materia = "Física Cuántica";
profesor3.materia = "Psicología Oscura";

console.log(profesor1.nombre + " " + profesor1.apellido + " " + profesor1.edad + " años" + " " + profesor1.grado + " " + profesor1.materia);
console.log(profesor2.nombre + " " + profesor2.apellido + " " + profesor2.edad + " años" + " " + profesor2.grado + " " + profesor2.materia);
console.log(profesor3.nombre + " " + profesor3.apellido + " " + profesor3.edad + " años" + " " + profesor3.grado + " " + profesor3.materia);