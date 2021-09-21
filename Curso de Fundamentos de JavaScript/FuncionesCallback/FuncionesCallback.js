function miFunction1() {
  console.log('funcion 1');
}

function miFuncion2() {
  console.log('funcion 2');
}

function imprimir(mensaje) {
  console.log(mensaje);
}

function suma(op1, op2, functionCallback) {
  let result = op1 + op2;
  functionCallback(result);
}

suma(5, 3, imprimir);

//Llamadas asíncronas con uso setTimeout

function miFuncionCallback() {
  console.log('Saludo asincrono despues de 3s');
}

setTimeout(miFuncionCallback, 3000);

setTimeout(() => console.log('Saludo asincrono despues de 2s'), 2000);

let reloj = () => {
  //fecha actual
  let fecha = new Date();
  console.log(
    `${fecha.getHours()}:${fecha.getMinutes()}:${fecha.getSeconds()}`
  );
};

setInterval(reloj, 1000);
