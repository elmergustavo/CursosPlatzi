'use strict';
let resultado = '';

try {
  if (isNaN(resultado)) throw 'No es un numero';
  else if (resultado === '') throw 'Es una cadena vacia';
  else if (resultado >= 0) throw 'Es mayor o igual a cero';
  else if (resultado < 0) throw 'Valor menor que cero';
} catch (e) {
  console.log(e);
} finally {
  console.log('Termina la revision de errores');
}
console.log('Continuamos...');
