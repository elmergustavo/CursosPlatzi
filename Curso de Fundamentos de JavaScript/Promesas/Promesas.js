//Objeto de tipo promesa, que resive dos parametros
//Estos parametros seran dos funciones callbacks
//*la primera es cuando la promesa se cumpla y la segunda es por si no se cumple la promesa

//*recordando que esto es un objeto
// let miPromesa = new Promise((resolved, rejected) => {
//   //* en caso de que el codigo sea exitoso mandamos a llamar la funcion de resolved
//   //* en caso contrario llamamos la funcion rejected

//   let expresion = false;
//   if (expresion) {
//     resolved('Resolvió correcto');
//   } else {
//     rejected('Se produjo un error');
//   }
// });

//* then recibe dos argumentos, que seran dos funciones de tipo flecha
//* estas seran la funcion callback en caso de que se resuelva correctamente y la segunda seria en caso que no se resuelva
//* el segundo argumento tambien lo podemos sacar del then pero lo colocariamos en un .catch
// miPromesa
//   .then(
//     (valor) => console.log(valor) //* Primer argumento
//     (error) => console.log(error) //* Segundo argumento, esto tambien seria el catch
//   )
//   .catch((error) => console.log(error));

//* No es necesario utilizar el argumento del error, lo comun siempre sera trabajar con la funcion callback cuando se resuelve correctamente

let promesa = new Promise((resolved) => {
  console.log('Inicio promesa');
  setTimeout(() => resolved('Saludos con promesa timeout'), 3000);
  console.log('Fin promesa');
});

promesa.then((valor) => console.log(valor));
