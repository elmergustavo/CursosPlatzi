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


