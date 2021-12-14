# Notas Curso Básico de JavaScript

¿Cómo nace Javascript?
Nace con la necesidad de generar dinamismo en las páginas web y que a su vez los usuarios y las empresas pudieran interactuar unos con otros.

¿Qué es Javascript?
Es un lenguaje interpretado, orientado a objetos, débilmente tipado y dinámico.

Débilmente tipado
Se pueden hacer operaciones entre tipos distintos de datos (enteros con strings, booleanos con enteros, etc). Ejemplo:


```js
4 + "7"; // 47
4 * "7"; // 28
2 + true; // 3
false - 3; // -3
```
Dinámico
Corre directamente en la etapa de Runetime sin una etapa de compilación previa. Esto permite probar nuestro código inmediatamente; pero también es lo que hace que los errores se muestren hasta que se ejecuta el programa.

¿Realmente es Javascript un lenguaje interpretado?
Si, y la razón es que le navegador lee linea por linea nuestro código el cuál le indica lo que tiene que hacer, sin la necesidad de compilar. Todo esto es controlado por el motor de Javascript V8 del navegador

Javascript es Basckwards Compatible
Todas las funciones nuevas que salen de Javascript no dañarán el trabajo ya hecho, pero no se podrá utilizar en nuestro entorno de trabajo inmediatamente. Para solucionar esto está Babel que permite utilizar las nuevas características del lenguaje pero lo transforma a una versión que el navegador pueda entender.

Aporte creado por Diego Martínez

![](https://static.platzi.com/media/user_upload/Dise%C3%B1o%20sin%20t%C3%ADtulo-3115bd9f-ec1c-425d-aa60-8462f4ffe7a3.jpg)
![](https://static.platzi.com/media/user_upload/2020-06-10_22h18_14-dca71009-4f9a-44de-8252-d2835d443ba5.jpg)

1.- JavaScript tiene una comunidad enorme de desarrolladores que te pueden ir ayudando a generar diferentes cosas.

Si solo estuvieras interesado en trabajar aplicaciones web tienes muchos frameworks y librerías construidas en JavaScript que te van a ayudar a hacer proyectos de forma mucho mas rápida, eficiente y robusta (Angular, View, React,entre otros)

Si no quieres trabajar solo en aplicaciones Web puedes utilizar JavaScript con un framework que se llama React Native para poder construir aplicaciones nativas como Android y IOS.

Puedes construir aplicaciones de escritorio con JavaScript, usando un framework llamado Electron, pueden correr en Mac o Windows.

También puedes trabajar en la parte del Back-end o **IOT **(Internet Od Things) es un concepto que se refiere a una interconexion digital de objetos cotidianos con Internet. Esto con un Framework llamado NodeJS, el cual es un entorno de ejecución de JavaScript que corre directamente en el Back-end.

Porqué JavaScript?

3 Lenguajes estándares: HTML5 - CSS3 - JS

HTML: Para maquetar la información. Texto, imagenes, videos, etc.
CSS: Para darle estilo a la información.
JS: Programación para que la página sea dinámica o generar una app web.

En el 2019 la W3C decidió y subió como nuevo estandar y lenguaje WA (WebAssembly). Es un lenguaje nuevo a utilizar para construir productos web. Con este no será necesario utilizar HTML, CSS y JS para hacer productos web.

JS tiene una comunidad enorme de devs que ayudan a generar diferentes cosas. Para apps web hay muchos frameworks y librerías construidas en JS, que ayudan a desarrollar proyectos de una manera mucho más rápida, eficiente y robusta.
Angular, Vue, React son algunos de los frameworks que podemos utilizar para hacer productos web.

Si no sólo quieres hacer productos web podemos utilizar un framework llamado React Native, para poder construir aplicaciones nativas para Android y IOS.
Electron: framework JS que nos permite desarrollar aplicaciones para escritorio, tanto para Mac como para Windows.

En toda web y app tenemos 2 partes. El Front-end y el Back-end.

Front-end: Es todo lo que se ve en nuestra web/app y con lo que podemos interactuar.
Back-end: Va manejando las bases de datos, las interacciones y peticiones que el Front-end le va a pedir.

Node.JS es un entorno de ejecución de JS que corre en el Back-end. Permite trabajar aplicaciones IOT (Internet de las cosas), hace inteligente ciertos dispositivos conectados a internet.

![](https://static.platzi.com/media/user_upload/CU01112E_1-f9d2b6fc-f60c-4bf4-a61d-6bf9df36b268.jpg)

![](https://static.platzi.com/media/user_upload/169c0df8121445d6c2848875d91521c7-f6097583-9431-489d-ba3d-263cfdb5e7e9.jpg)

![](https://static.platzi.com/media/user_upload/Untitled%20%281%29-9e7855fe-dc07-4942-a617-b23a1cd197e8.jpg)

Dentro de JavaScript tenemos tres formas de declarar una variable las cuales son: var, const y let.

Var: Era la forma en que se declaraban las variables hasta ECMAScript 5. Casi ya no se usa porque es de forma global y tiene las siguientes características:

o Se puede reinicializar: osea todas las variables se inicializan, por ejemplo:
Var pokemonType = ‘electric’ entonces reinicializar es:
Var pokemonType = ‘grass’ osea la misma variable con diferentes datos el último dato predomina.
o Se puede reasignar: osea la variable ya inicializada le reasignamos otro valor por ejemplo: inicializamos la variable: Var pokemonType = ‘electric’ ahora la reasignamos pokemonType = ‘grass’ ya no va var
o Su alcance es función global: osea inicializamos la variable, pero la podemos llamar desde cualquier bloque (una llave abierta y una cerrada {}) pero hay que tener mucho cuidado con ello ya que puede haber peligro, no es recomendable usar VAR.

const y let es la forma en que se declaran las variables a partir de ECMAScript 6,

const: sirve para declarar variables que nunca van a ser modificadas:
o No se puede reinicilizar: es una const única no puede haber otra inicializada con el mismo nombre. const pokemonType = ‘electric’ no puede haber:
const pokemonType = ‘grass’
o No se pude re asignar: una vez que la hayamos inicializado no la podemos reasignar solo con su nombre: const pokemonType = ‘electric’ no puede ejecutarse:
pokemonType = ‘grass’
o No es inmutable: osea no puede cambiar con objetos:

Let: Son variables que pueden ser modificadas, se pueden cambiar:
o No se puede reinicilizar: es una const única no puede haber otra inicializada con el mismo nombre. let pokemonType = ‘electric’ no puede haber:
let pokemonType = ‘grass’
o Se puede reasignar: Osea la variable ya inicializada le reasignamos otro valor por ejemplo: inicializamos la variable: let pokemonType = ‘electric’ ahora la reasignamos pokemonType = ‘grass’
o Su contexto de es bloque: Solo funciona dentro de un bloque {}, fuera de ello no.

![](https://static.platzi.com/media/user_upload/JavaScript-4e0b4a50-c2ef-40af-b403-a1e4e7a64436.jpg)
![](https://static.platzi.com/media/user_upload/4%29Variables-4a4aaccd-6f03-417a-bf37-76fdfd8f5752.jpg)

![](https://static.platzi.com/media/user_upload/JavaScript%20%281%29-997fdbe2-5817-4e30-a6b4-71f2bf6c53e2.jpg)

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions

¿Qué es una función declarativa y una expresiva?

Cuando hablamos de funciones en JavaScript, tenemos dos tipos de funciones: Funciones Declarativas (function declaration / function statement) y Expresiones de función (function expression / funciones anónimas).

Funciones Declarativas:
En las funciones declarativas, utilizamos la palabra reservada function al inicio para poder declarar la función:

```js
function saludar(nombre) {
	console.log(`Hola ${nombre}`);
}

saludar('Diego');
```

Expresión de función:
En la expresión de función, la declaración se inicia con la palabra reservada var, donde se generará una variable que guardará una función anónima.

```js
var nombre = function(nombre){
    console.log(`Hola ${nombre}`)
}

nombre(‘Diego’);
```

En la expresión de función, la función podría o no llevar nombre, aunque es más común que se hagan anónimas.

Diferencias:
A las funciones declarativas se les aplica hoisting, y a la expresión de función, no. Ya que el hoisting solo se aplica en las palabras reservadas var y function.

Lo que quiere decir que con las funciones declarativas, podemos mandar llamar la función antes de que ésta sea declarada, y con la expresión de función, no, tendríamos que declararla primero, y después mandarla llamar.

https://developer.mozilla.org/en-US/docs/Glossary/Hoisting

![](https://static.platzi.com/media/user_upload/104445629_117809673305290_4160707404159566859_o-a02739b8-c1a8-473d-85d2-352c59737fa2.jpg)
![](https://static.platzi.com/media/user_upload/104163704_117809719971952_9118532895000404646_o-169e2b3c-6a01-40da-bd02-eda818e172a2.jpg)
![](https://static.platzi.com/media/user_upload/105683156_117809693305288_8565633926620774673_o-63faf1ed-9e1d-4240-9030-a96af41dbd19.jpg)
![](https://static.platzi.com/media/user_upload/103781043_117809739971950_5385296868813498879_o-e9174953-890b-4ed1-a834-779072bfd230.jpg)
![](https://static.platzi.com/media/user_upload/103952006_117809733305284_7198650990608055435_o-4ffacc83-a616-41ab-824e-2dd4793a70ec.jpg)
![](https://static.platzi.com/media/user_upload/104771822_117809763305281_3701417390702872195_o-4d913f45-2028-47a7-8263-850dcbd739ce.jpg)
![](https://static.platzi.com/media/user_upload/104303933_117809836638607_410047023428968429_o-dcaeee63-a643-4bea-9d4c-432a0537990a.jpg)
![](https://static.platzi.com/media/user_upload/104358902_117815513304706_639858807487491016_o-7627d953-974e-46ae-be7e-cb94b0006ec0.jpg)

![](https://static.platzi.com/media/user_upload/3Captura-c10a7418-6e1a-4da2-9fd8-ee81d87a8e66.jpg)


https://www.youtube.com/watch?v=uI6o97A4IrI

Coerción es la forma en la que podemos cambiar un tipo de valor a otro, existen dos tipos de coerción:
Coerción implícita = es cuando el lenguaje nos ayuda a cambiar el tipo de valor.
Coerción explicita = es cuando obligamos a que cambie el tipo de valor.

```js
//Ejemplos de Coerción:

var a = 4 + "7"; //Convierte a 4 en un string y lo concatena con el "7", por esto regresa un string de valor "47"

4 * "7"; //Convierte al "7" en un número y realiza la operación, por esto devuelve 28

var a = 20;
var b = a + ""; //Aquí concatenamos para convertir la variable a string (coerción implícita)
console.log(b); 

var c = String(a); //Aquí obligamos a la variable a convertirse en string (coerción explícita)
console.log(c);

var d = Number(c); //Aquí obligamos a la variable a convertirse en número (coerción explícita)
console.log(d);
```
## Valores: Truthy y Falsy

```js
//Ejemplos en los que Boolean devuelve Falso:
Boolean(0); //false
Boolean(null); //false
Boolean(NaN); //false
Boolean(undefined); //false
Boolean(false); //false
Boolean(""); //false

//Ejemplos en los que Boolean devuelve verdadero:
Boolean(1); //true para 1 o cualquier número diferente de cero (0)
Boolean("a"); //true para cualquier caracter o espacio en blanco en el string
Boolean([]); //true aunque el array esté vacío
Boolean({}); //true aunque el objeto esté vacío
Boolean(function(){}); //Cualquier función es verdadera también
Boolean(-1); // true
```
https://developer.mozilla.org/es/docs/Glossary/Truthy

## Operadores: Asignación, Comparación y Aritméticos.

* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators

```js
//Operadores binarios:
3 + 2 //Suma
50 - 10 // Resta
10 * 20 //Multiplicación
20 / 2 //División

"Diego " + "De Granda" //concatenación de strings

//Operadores unitarios:
!false //negación de la negación = true

//Operadores de asignación:
var a = 1; //Asignamos un valor a la variable

//Operadores para comparar:
3 == "3"; //Compara los valores y devuelve "true" en este caso

3 === "3"; //Compara y valida los tipos y valores. Devuelve "falso" en este caso

5 < 3 //Compara y valida si el 5 es menor a 3
5 > 3 //Compara y valida si el 5 es mayor a 3
5 <= 6 //Compara y valida si el 5 es menor o igual al 6
5 >= 6 //Compara y valida si el 5 es mayor o igual al 6

a && b //Valida si ambas variables son verdaderas para que se cumpla la condición
a || b //Aquí se cumple la condición si alguna de las dos variables es verdadera

var edad = 40
edad++ //Incrementa el valor en 1

edad += 2 //Incrementa el valor por 2
```
![](https://image.slidesharecdn.com/javascript-js-141008104916-conversion-gate02/95/javascript-16-638.jpg?cb=1412765432)
![](https://static.platzi.com/media/user_upload/op-d80fe448-1104-41c1-ad8d-f88aaca3c9b8.jpg)

## Condicionales: If, Else, else if

```js
var op1 = "Piedra";
var op2 = "Papel";
var op3 = "Tijera";

var resultado = function(user, cpu){
    if(user != cpu){
        if(user === op1 && cpu === op3){
            console.log("el usuario GANO con "+ op1)
        }else if(user === op2 && cpu === op1){
            console.log( "el usuario GANO con " + op2)
        }else if(user === op3 && cpu === op2){
            console.log("el usuario GANO con " + op3)
        }else{
            console.log("La CPU Gano!!")
        }
    }else if(user === cpu){
        console.log("Empate")
    }
};

resultado(op1,op3) //el usuario GANO con Piedra```
```
## Arrays
https://devcode.la/tutoriales/manejo-de-arrays-en-javascript/


```js
var colores = [“rojo”, “azul”, “verde”, “amarillo”];

```

Reverse, metodo que establece que el array invierte los elementos


```js
colores.reverse();
["amarillo", "verde", "azul", "rojo", "anaranjado"]
```
Sort, metodo para ordenar alfabeticamente los array con datos de tipo String

```js
colores.sort();
["amarillo", "anaranjado", "azul", "rojo", "verde"]
```

Slice, método que puede contener uno o dos argumentos, que indiquen el inicio y parada de posiciones, pues devuelve los elementos contenidos en el array, de acuerdo a los argumentos indicados, por ejemplo si a colores, le agregamos colores.slice(1,3); obtendremos los que se encuentran en la posición 1, 2

```js
colores =  ["amarillo", "anaranjado", "azul", "rojo", "verde"]
colores.slice(1,3);
["anaranjado", "azul"]
```
Si solo se indica un argumento se tomará como inicio ese argumento y como final la última posición, entonces si usamos:

```js
colores.slice(2);
["azul", "rojo", "verde"]
```

var frutas = ["Manzana", "Plátano", "Cereza", "Fresas"];

console.log(frutas);

console.log(frutas.length); // lingitud o numero de elementos
console.log(frutas[n]); // acceder al elemento por medio de index

```js
//Mutar o alterar Array
var masFrutas = frutas.push("Uvas") //añadir elementos al final del array
var ultimo = frutas.pop()//Eliminar el último elemento del Array
var nuevaLongitud = frutas.unshift("Uvas");//añadir elemento al inicio del array
var borrarFruta = frutas.shift("Uvas");//Borrar elemento
var posicion = frutas.indexOf("Cereza");//Devuelve el index o posicion del elemento```
```
![](https://cdn.discordapp.com/attachments/328692261380685824/865328486779584523/1623252703192.png)

![](https://static.platzi.com/media/user_upload/download%20%2827%29-c7353da6-958d-4ecd-85e3-cfa574151a05.jpg)
![](https://static.platzi.com/media/user_upload/download%20%2828%29-3bffe0a0-0103-4e9f-b945-79753585fc92.jpg)

![](https://static.platzi.com/media/user_upload/js-array-sort-f6e80ce2-f3e6-463f-94f2-06add172e76d.jpg)

## Loops: For y For...of
![](https://static.platzi.com/media/user_upload/download%20%2829%29-91079620-a820-4b66-8f6a-3678df995094.jpg)

```js
var frutas = ["Manzana", "Pera", "Naranja", "Platano", "Uva"];

for (i = 0; i < frutas.length; i++) {
    console.log(`Indice ${i}: ${frutas[i]}`);
}

for (e of frutas) {
    console.log(`Elemento ${e}`);
}```
```
* https://www.digitalocean.com/community/tutorials/for-loops-for-of-loops-and-for-in-loops-in-javascript
![](https://static.platzi.com/media/user_upload/Screen%20Shot%202021-06-24%20at%2022.48.54-8ec8f840-48ac-44ff-9efa-e775442e709f.jpg)

## Loops: While

```js
var estudiantes = ["Maria", "Sergio", "Rosa", "Daniel"];

function saludarEstudiante(estudiante) {
    console.log(`Hola ${estudiante}`);
}

var i = 0;

//do-while
do {
    saludarEstudiante(estudiantes[i]);
    i++;
} while (i < estudiantes.length)

//while
while (estudiantes.length > 0) {
    var estudiante = estudiantes.shift();
    saludarEstudiante(estudiante);
}
```
![](https://static.platzi.com/media/user_upload/download%20%2830%29-b72f1c8f-81f1-447a-a314-2c51616a1bb7.jpg)

![](https://static.platzi.com/media/user_upload/carbonWhile-111dab6b-9f44-46f7-9e62-f2ee770d9f63.jpg)

![](https://static.platzi.com/media/user_upload/Loops_apunte-e430fc7e-2a84-4b76-bd0c-4bd2c92fcd3a.jpg)

## Objects
![](https://static.platzi.com/media/user_upload/carbon%20%282%29-93ff2816-ead8-4cd2-acbb-5989138b518b.jpg)
![](https://static.platzi.com/media/user_upload/download%20%2831%29-ec6e3c28-5cd8-4388-a150-3468855f329b.jpg)
![](https://static.platzi.com/media/user_upload/download%20%2832%29-15c69b71-9ff2-4a7b-ba64-4a9d89f3e2a1.jpg)
![](https://i.imgur.com/gEzNZIl.png)

```js
var piedrasPapelTijeras = {
  // Marcador del juego
  puntoMaquina: 0,
  puntoUsuario: 0,

  mostrarMarcador: function () {
    console.log(`Maquina: ${this.puntoMaquina} - Usuario: ${this.puntoUsuario}`)
  },

  // Opciones Validas
  opciones: ["piedra", "papel", "tijeras"],

  // Mostrar opciones validas
  mostrarOpciones: function () {
    for (var opcion of this.opciones) {
      console.log(`"${opcion}"`);
    }
  },

  // --------AQUI COMIENZA EL JUEGO----------//
  // entrada de la maquina
  maquina: "",
  // entrada del usuario
  usuario: "",

  validarMaquina: -1,
  validarUsuario: -1,

  // Funcion principal
  jugar: function () {

    while ((this.puntoMaquina < 10) && (this.puntoUsuario < 10)) {
      console.log("¡A jugar!");
      // Asinga un valor aleatorio a la entrada de maquina
      this.maquina = this.opciones[Math.round(Math.random() * 3)];
      // Asinga un valor aleatorio a la entrada de usuario
      this.usuario = this.opciones[Math.round(Math.random() * 3)];
      // Muestra las entradas
      console.log(`Maquina: ${this.maquina}`);
      console.log(`Usuario: ${this.usuario}`);
      // busca las entradas en las opciones validas
      this.validarMaquina = this.opciones.indexOf(this.maquina);
      this.validarUsuario = this.opciones.indexOf(this.usuario);

      // Revisa si las entradas son opciones validas
      if ((this.validarMaquina >= 0) && (this.validarUsuario >= 0)) {
        switch (true) {

          // valida si hay empate
          case (this.maquina === this.usuario):
            console.log("Hay un empate");
            this.mostrarMarcador();
            this.jugar();
            break;
            //casos donde gana la maquina
          case (((this.maquina === "piedra") && (this.usuario === "tijeras")) ||
            ((this.maquina === "papel") && (this.usuario === "piedra")) ||
            ((this.maquina === "tijeras") && (this.usuario === "papel"))):

            console.log("La maquina ha ganado");
            this.puntoMaquina++;
            this.mostrarMarcador();
            this.jugar();
            break;

          default: //si la maquina no gano, el usuario si

            console.log("El usuario ha ganado");
            this.puntoUsuario++;
            this.mostrarMarcador();
            this.jugar();
        }
      } else {
        console.log(`Opcion no valida ingresa una de las siguientes opciones:`);
        this.mostrarOpciones();
        this.jugar();
      }
    }


  },
  // Resultados
  resultados: function () {
    this.puntoMaquina == 10 ? console.log("Lo siento la Maquina ha ganado :(") : console.log("¡Felicidades eres el campeón del juego!");
  }
}

piedrasPapelTijeras.jugar();
piedrasPapelTijeras.resultados();
```
* https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/this

## Objects: Función constructora
```js
function auto (MARCA, MODELO, ANNIO){
  this.marca = MARCA;
  this.modelo = MODELO;
  this.annio = ANNIO;
}
var autos = [];
for(let i = 0 ; i < 30 ; i++){
  var marca = prompt("Ingresa la marca del auto");
  var modelo = prompt("Ingresa el modelo del auto");
  var annio = prompt("Ingresa el año del auto");
  autos.push(new auto (marca, modelo, annio));
}

for(let i = 0 ; i < autos.length ; i++){
  console.log(autos[i]);
}
```
![](https://static.platzi.com/media/user_upload/ejercicio-1330da3a-fbf9-47ec-9131-07e0c072638d.jpg)

* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new


## Métodos de recorridos de Arrays

```js
// Este ejemplo es imaginando que recibimos una lista de 30 carros diferentes y se nos solicita que se almacene esta información, como estamos aprendiendo a usar js por que es un lenguaje cool y no queremos tipiar todo de manera normal y aburrida, usaremos este lenguaje c: así hacemos un pequeño trabajo de separar todas las marcas, modelos y años respectivamente en distintos arrays para así lograr juntarlos en uno solo usando una función constructiva la cual indicara cada auto ingresado con su marca, modelo y año respectivamente.

var marca = ["Audi", "Subaru", "Lexus", "Porsche", "BMW", "Mazda", "Buick", "Toyota", "Kia", "Honda", "Hyundai", "Volvo", "Mini", "Mercedes-Benz", "Volkswagen", "Ford", "Lincoln", "Scion", "Acura", "Chevrolet", "Nissan", "Infiniti", "GMC", "Cadillac", "Dodge", "Land", "Rover", "Mitsubishi", "Jeep", "Fiat"];
var modelo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30];
var annio = [2020,2019,2018,2020,2020,2020,2018,2018,2020,2020,2020,2018,2018,2020,2020,2019,2020,2020,2019,2019,2020,2020,2019,2019,2019,2020,2019,2019,2018,2020];
var listaAutos = [];
function autoN(marca, modelo, annio){
    this.marca = marca;
    this.modelo = modelo;
    this.annio = annio;
} 
for (var i = 0; i<30; i++){   
    var autoNuevo = new autoN(marca[i],modelo[i],annio[i]);
    listaAutos.push(autoNuevo);
}

// Luego se nos solicito que filtremos los carros por medio del año actual, ya que deseaban saber la cantidad de autos nuevos ingresados. Gracias a nuestro trabajo esto se podía saber de la siguiente manera:

var autosFiltrados = listaAutos.filter(function(auto){
    return auto.annio === 2020;
});
console.log(autosFiltrados);

// Así logramos obtener una lista con todos los autos del año 2020 c:

// Posterior a eso, se necesitaba obtener una lista urgentemente de las marcas de los 30 autos que acababan de ingresar por razones ajenas que no nos interesan c: Obviando que nosotros ya tenemos esta lista creada xD y queremos usar js para esto, esta tarea es tan sencilla como hacer: 

var marcasRecientes = listaAutos.map(function(auto){
    return auto.marca;
});
console.log(marcasRecientes);

// Así obtenemos nuestra lista de marcas recientemente ingresadas c:
```

* https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array

```js
var articulos = [
	{ nombre: '📱', precio: 1000 },
	{ nombre: '💻', precio: 1500 },
	{ nombre: '🖥', precio: 2000 },
	{ nombre: '⌨️', precio: 100 },
	{ nombre: '🖱', precio: 70 },
	{ nombre: '🚗', precio: 30000 },
];

// Método Filter
var articulosFiltrados = articulos.filter(function(articulo) {
	return articulo.precio <= 500;
});

// Método Map
var nombreArticulos = articulos.map(function(articulo) {
	return articulo.nombre;
});

articulosFiltrados;
// (2) [{…}, {…}]
//   0: {nombre: "⌨️", precio: 100}
//   1: {nombre: "🖱", precio: 70}

nombreArticulos; // (5) ["📱", "💻", "🖥", "⌨️", "🚗"]
```
![](https://static.platzi.com/media/user_upload/download%20%2834%29-71d4f38b-9123-4269-a1f4-34ed3de1fba6.jpg)
![](https://static.platzi.com/media/user_upload/download%20%2835%29-1a924a64-19e9-4eea-9f23-fcdabd54f109.jpg)
![](https://static.platzi.com/media/user_upload/Captura%20de%20pantalla%202021-07-13%20091857-ec55eef4-4a89-4b9b-a3f9-82edcdbd0375.jpg)

```js
//             *** Metodos de recorridos de arrays *** 
//-------------------------------------------------------------

var articulos = [
    {nombre:"bicicleta", costo:"3000"},
    {nombre:"tv", costo:"2500"},
    {nombre:"libro", costo:"320"},
    {nombre:"celular", costo:"10000"},
    {nombre:"Laptop", costo:"20000"},
    {nombre:"Teclado", costo:"500"},
    {nombre:"Audifonos", costo:"1700"}
]

//metodo filter va a validar se algo es verdadero o falso

var articulosFilatrados = articulos.filter(function(articulo){
    return articulo.costo <= 500
});
console.log(articulosFilatrados);

// metodo map me va ayudar a mapear columnas de articulos

var nombreArticulos = articulos.map(function(art){
    return art.nombre
});
```
![](https://static.platzi.com/media/user_upload/19-JS-0cdb9aae-196c-404f-b5bf-1a844a8677f6.jpg)

## Recorriendo Arrays con .find(), .forEach() y .some()

El método find () devuelve el primer valor que coincide de la colección. Una vez que coincida con el valor en los resultados, no verificará los valores restantes en la colección de matriz.

El método filter () devuelve los valores coincidentes en una matriz de la colección. Verificará todos los valores de la colección y devolverá los valores coincidentes en una matriz.


```js
var articulos = [
    { nombre: "Bici", costo: 3000 },
    { nombre: "TV", costo: 2500 },
    { nombre: "Libro", costo: 320 },
    { nombre: "Celular", costo: 10000 },
    { nombre: "Laptop", costo: 20000 },
    { nombre: "Teclado", costo: 500 },
    { nombre: "Audifonos", costo: 1700 },
];

//filter Genera un nuevo array
var articulosFiltrados = articulos.filter(function(articulo){
    return articulo.costo <= 500; //articulos con precio menor a 500 pesos
});

//map Ayuda a mapear ciertos elementos de los articulos, es necesario generar nuevo array
var nombreArticulos = articulos.map(function(articulo){
    return articulo.nombre;
});

//find Ayuda a encontrar algo dentro del array articulos
var encuentraArticulo = articulos.find(function(articulo){
    return articulo.nombre === "Laptop";
});

//forEach No es necesario generar nuevo array, se utiliza para realizar un recorrido de un array principal
articulos.forEach(function(articulo){
    console.log(articulo.nombre);
});

//some Se genera nuevo array, regresa un condición en Boolean
var articulosBaratos = articulos.some(function(articulo){
    return articulo.costo <= 700;
});```
```

![](https://static.platzi.com/media/user_upload/download%20%2836%29-7282c92c-63b2-4787-b532-2f8baec30a15.jpg)
![](https://static.platzi.com/media/user_upload/download%20%2837%29-50b88cbd-c0d3-4521-8535-90839b595f4e.jpg)
![](https://static.platzi.com/media/user_upload/download%20%2838%29-52735e7b-4397-42ca-bb3f-103623f40980.jpg)
![](https://static.platzi.com/media/user_upload/20-JS-c994e710-de79-4fbf-82f8-144f90aebd56.jpg)

* https://www.w3schools.com/jsref/jsref_obj_array.asp
* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array 

## Eliminando elementos de un Array
## .push()
El método .push() nos permite agregar uno o más elementos al final de un array.

A continuación veremos un ejemplo aplicado con un array que contiene números:
![](https://static.platzi.com/media/user_upload/Imagen%201-bc72a917-1b18-423d-ad34-d75d26341605.jpg)
Como podemos ver, al momento de ejecutar la función se agregan los números 6 y 7 al array.

Ahora revisemos un ejemplo con strings:
![](https://static.platzi.com/media/user_upload/Imagen%202-f31c19d3-911e-4157-b9ca-a87ec3f50631.jpg)

Como podemos ver, agregamos dos cadenas de strings al ejecutar la función donde tenemos txtArray.push(). Es decir, indico el array al que voy agregar elementos, uso el método .push(), y dentro de .push() indico los elementos que quiero agregar al string. Finalmente, el console.log() lo uso para revisar en la consola si esto sucedió o no.

.shift()
Ahora pasemos a la otra cara de la moneda donde necesitamos eliminar un elemento del array. .shift() eliminar el primer elemento de un array, es decir, elimina el elemento que esté en el índice 0.

![](https://static.platzi.com/media/user_upload/Imagen%203-633de332-2242-4957-a79d-d263bff35c1a.jpg)
Como vemos, luego de aplicar .shift() se eliminó exitosamente el primer elemento del array. ¿Y si quisiéramos eliminar el último elemento? Pasemos al bonus track de esta clase 🙌🏼.

Bonus Track
Si ya entendiste cómo funciona .shift() aplicar .pop() te será pan comido 🍞. El método .pop() eliminará el último elemento de un array. En este sentido, si tenemos un array de 5 elementos, pop() eliminará el elemento en el índice 4. Usemos el mismo ejemplo pero usando este método.
![](https://static.platzi.com/media/user_upload/Imagen%204-f2fc98b7-a80a-4598-a049-1533cbb78404.jpg)

```js
// Array de números

let numArray = [1,2,3,4,5]

function newNum(){
  numArray.push(6,7)
}

newNum()
```

```js
// --- SHIFT ---

//Creamos el array
let array = [1,2,3,4,5]
console.log(array)

// Aplicamos .shift()
let shiftArray = array.shift()

//Revisamos. El output debe de ser [2,3,4,5]
console.log(array)

// --- POP ---

//Creamos el array
let array = [1,2,3,4,5]
console.log(array)

// Aplicamos .shift()
let shiftArray = array.pop()

//Revisamos. El output debe de ser [1,2,3,4]
console.log(array)
```
