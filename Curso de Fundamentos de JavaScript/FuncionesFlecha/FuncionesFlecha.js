//Forma clasica
function miFuncion() {
  console.log('Saludos desde mi función clasica');
}

// miFuncion();

// Funcion anonima
let miFuncionAnonima = function () {
  console.log('Saludos desde mi funcion anonima');
};

//Las funciones flecha son fuciones anonimas que se le asignan a una variable pero la diferencia es que quitamos la palabra reservada function y agregamos un mayor que despues de los parentesis

//Con las arrow function no aplica el concepto de hoisting ya que utilizamos let o const
// const miArrowFunction = () => {
//   console.log('Saludos desde mi arrow function');
// };

//Si la funcion solo va a contener una linea de codigo no hace falta abrir el cuerpo de la funcion y la funcion retorna algo no hará falta tampoco colocar la palabra return

const miArrowFunction = () => console.log('Saludos desde mi arrow function');

const saludar = () => {
  return 'Saludos desde función flecha';
};

const regresaObjeto = () => ({ nombre: 'Juan' });

const funcionConParametros = (mensaje) => console.log(mensaje);

funcionConParametros('Saludos con Parametros');

// console.log(saludar());
// console.log(regresaObjeto());
// miFuncionAnonima();
// miArrowFunction();
