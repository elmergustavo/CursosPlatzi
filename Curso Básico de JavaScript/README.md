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





