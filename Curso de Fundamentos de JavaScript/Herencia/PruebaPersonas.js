class Persona {
  static contadorPersonas = 0;

  constructor(nombre, apellido, edad) {
    this._idPersona = ++Persona.contadorPersonas;
    this._nombre = nombre;
    this._apellido = apellido;
    this._edad = edad;
  }

  get idPersona() {
    return this._idPersona;
  }

  get nombre() {
    return this._nombre;
  }

  get apellido() {
    return this._apellido;
  }

  get edad() {
    return this._edad;
  }

  set nombre(nombre) {
    this._nombre = nombre;
  }

  set apellido(apellido) {
    this._apellido = apellido;
  }

  set edad(edad) {
    this._edad = edad;
  }

  toString() {
    return `id Persona: ${this._idPersona}, nombre: ${this._nombre}, apellido: ${this._apellido}, edad: ${this._edad}`;
  }
}

class Cliente extends Persona {
  static contadorCliente = 0;

  constructor(nombre, apellido, edad, fechaRegistro) {
    super(nombre, apellido, edad);
    this._idCliente = ++Cliente.contadorCliente;
    this._fechaRegistro = fechaRegistro;
  }

  get idCliente() {
    return this._idCliente;
  }

  get fechaRegistro() {
    return this._fechaRegistro;
  }

  set fechaRegistro(fechaRegistro) {
    this._fechaRegistro = fechaRegistro;
  }

  toString() {
    return `${super.toString()}, idCliente: ${
      this._idCliente
    }, fechaRegistro: ${this._fechaRegistro}`;
  }
}

class Empleado extends Persona {
  static contadorEmpleado = 0;

  constructor(nombre, apellido, edad, sueldo) {
    super(nombre, apellido, edad);
    this._idEmpleado = ++Empleado.contadorEmpleado;
    this._sueldo = sueldo;
  }

  get idEmpleado() {
    return this._idEmpleado;
  }

  get sueldo() {
    return this._sueldo;
  }

  set sueldo(sueldo) {
    this._sueldo = sueldo;
  }

  toString() {
    return `${super.toString()}, idEmpleado: ${this._idEmpleado}, sueldo: ${
      this._sueldo
    }`;
  }
}

//Prueba clase Persona

let persona1 = new Persona('Sergio', 'Pérez', 22);
let persona2 = new Persona('Akira', 'Moralez', 21);

console.log(persona1.toString());
console.log(persona2.toString());

let empleado1 = new Empleado('Ramiro', 'Guzman', 22, 200000);

console.log(empleado1.toString());

let cliente1 = new Cliente('Juan', 'Utria', 24, new Date());
console.log(cliente1.toString());
