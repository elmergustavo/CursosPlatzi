# Linux NO es difícil

🤔 No sé por que de repente algunas personas piensan que sí lo es. Yo pensaba lo mismo, pero para nada lo es, de hecho es mucho más difícil programar en Windows que programar en Linux (y es por eso que Windows tiene a WSL 👀) esto es porque con Linux tenemos todo a la mano, es un sistema operativo más dev-friendly, Windows está más pensado para el usuario final, es por eso que nos toca virtualizar todo ahí, y que de repente algo no funciona.
.
Otra cosa cursiosa es que de hecho sí puedes invocar demonios en la terminal “literalmente” jaja. En el mundo de la terminal, hay algunos procesos especiales a los que se les conoce como “demonios”, básicamente son procesos que se están ejecutando en el background o en la misma terminal.
.
¿Alguna vez has usado Nodemon mientras trabajabas con Node.js? Bueno, Nodemon es un demonio, su propio nombre lo dice “No… demon”, y es básicamente un demonio porque cuando lo ejecutas se queda aparando la terminal, es decir, se queda corriendo un proceso 👀☝.
.
Of course, no hay que tenerle miendo a la terminal. De hecho, muchos la vemos como “agh, esa cosa con letras raras”, pero la verdad es que una terminal es super comoda! Lo digo porque puedes hacer muuuuuuchas cosas con un solo comando, puedes automatizar tareas y puedes crear mil cosas increíbles.
.
De hecho, como dato cursioso, la terminal y todos los comandos que pones ahí son básicamente un lenguaje de programación llamado “Bash”, sí, puedes programar en Bash usando la terminal 👀. Saber usar la terminal es una de las principales habilidades que debe tener un programador para ser un profesional 😈.

* https://linuxjourney.com/
* https://www.notion.so/Introducci-n-a-la-Terminal-y-L-nea-de-Comandos-5ed377c3c79e4313b0796b679cb1dc73
* https://www.geeksforgeeks.org/linux-file-hierarchy-structure/

![](https://static.platzi.com/media/user_upload/image-2bc4bcc2-3856-4166-acc6-2e21ce152009.jpg)
![](https://static.platzi.com/media/user_upload/C02_jerarquia-estandar-del-sistema-de-archivos-de-linux-2d8855ef-f873-4168-b750-77614b03fd2b.jpg)
![](https://static.platzi.com/media/user_upload/2021-05-12_08h16_36-62619596-b42d-4233-b62c-72f6ca9e4e34.jpg)
![](https://static.platzi.com/media/user_upload/Untitled-1f2ae1ba-d6f6-4a5a-a113-d095d1d2307e.jpg)

## Manipulando archivos y directorios

¿Y para qué me sirve correrlo como interactivo?

Si te preguntaste esto es porque seguramente aún no te has dado cuenta de lo peligroso que es eliminar algo. Cuando tú eliminas algo desde la terminal, este archivo/carpeta se elimina… PARA SIEMPRE *chan, chan chan*.
.
Con esto me refiero a que ese archivo que eliminaste NO se va a mover al basurero, sino que directamente se va a eliminar, y la única forma de recuerarlo podría ser con algún programa que lea sector por sector de tu disco duro.
.
He visto por ahí cuando alguien pregunta por cómo eliminar una carpeta, el comando que más comparten es rm -rf carpeta sin saber exactamente qué es lo que hace, ahora ya saben que poner esa “f” como parámetro es muy peligroso. Con poner “r” basta, esto porque el borrado es recursivo básicamente recorrerá cada subcarperta/archivo y las irá borrando uno por uno.
.
#################################
DANGER ZONE

#################################
.
Ahora quiero explicarte por qué este comando es peligroso, tanto que puedes llegar a eliminar tu sistema operativo, NO CORRAS ESTE COMANDO POR NADA DEL MUNDO.
.
Imagina que quieres eliminar alguna carpeta de tu computadora usando la terminal, y por alguna razón decides usar una ruta absoluta:

rm -rf / home/tuUsuario/carpetaAEliminar/

Todo bien… ¿verdad? Bien, si ejecutaras este comando todo tu sistema operativo desaparecería, ¿por qué? quiero que te fijes cómo entre el / y la palabra home hay un espacio… ¿recuerdas qué significaba esa /? Ya lo vimos 👀… Así es, la carpeta raíz, la carpeta donde vive todo tu sistema operativo, y le estás diciendo que la elimine a la fuerza, ese espacio indica que la a eliminar dos carpetas, primero eliminará / y luego eliminará home/tuUsuario/carpetaAEliminar/.
.
El comando correcto que deberíamos usar es:

rm -rf /home/tuUsuario/carpetaAEliminar/

Aquí ese espacio no existe, por lo que todo iría bien, quiero que te fijes cómo con un pequeño error, puedes eliminar todo. Por esom siempre ten cuidado al usar este comando, y de preferencia… ¡Usa el modo interactivo! 😄


Mostrar información del directorio:
ls :Lista el contenido de los directorios (por defecto ordena la salida alfabéticamente).

Alguna de sus opciones (argumentos) más útiles son:

-a :todos los archivos, incluso los que comienzan con punto (.).

-A :Lista todos los ficheros en los directorios, excepto los que comienzan con punto . (.) y los que comienzan con doble punto (…).

-F :indica tipo: / directorio, * ejecutable, @ enlace simbólico.

-h :indicará el tamaño en KB, MB, etc.

-l :listado en formato largo (o detallado).

-S :clasifica los contenidos de los directorios por tamaños, con los ficheros más grandes en primer lugar.

-r :invierte el orden de la salida.

-R :Lista recursivamente los subdirectorios encontrados.

-t :ordenar por fecha de última modificación.

-u :ordenar por fecha de último acceso.

-x :presenta los ficheros por columnas.

-i :precede la salida con el número de i-node

ejemplos:

ls -lt	:muestra los archivos del mas actual al mas antiguo

ls -ltr	:muestra los archivos del mas antiguo al mas actual

ls -lh	:muestra de forma mas legible el tamaño de los archivos

ls -lhS	:muestra de forma ordenada los archivos por su tamaño

ls -la :muestra los atributos de los archivos y los archivos ocultos

Manipular archivos

    mkdir <nombre_directorio>: crea un directorio también puedes añadir la ruta

    touch: crea un archivo, si no indicas la extension por defecto sera .txt

    cp <archivo> <ruta>: nos permite duplicar archivos, para duplicar directorios con su contenido añadir el modificador -r que indica recursividad

    mv <archivo> <ruta> : mover un archivo hacia un directorio. También se usa para renombrar archivos mv <archivo> <nuevo nombre> no olvidar la extension del archivo
    Para mover directorios añadir el modificador -r

    rm: elimina archivos, con -i indica un mensaje de confirmación en consola para tener mas control sobre la elección de que archivos queremos eliminar. Para eliminar un directorio añadir -r y -ri para usar el mensaje de confirmación



    ls -la muestra TODOS los archivos
    ls -lS ordena los documentos del por tamaño de peso, el más pesado va arriba de todos
    ls -lr ordena de menos pesado a más pesado
    mkdir nombreCarpeta crea una carpeta con su nombre
    touch nombreArchivo crea un archivo
    cp nombreArchivo nombreNuevo copia un archivo y crea otro
    mv archivo directorio mueve un archivo hacía el directorio indicado
    mv nombreArchivo nombreArchivoNuevo reemplaza el nombre de un archivo por otro ``nombre
    rm archivo COMANDO PELIGROSO borra totalmente de la existencia a un archivo
    rm -i archivo Aquí nos hará una pregunta para confirmar si en verdad queremos eliminar un archivo
    rm -ri Elimina directorio con sus archivos internos
    rm -rf COMANDO SUPER PELIGROSO va a borrar TODO sin importar nada, NO SE RECOMIENDA USARLO

## Explorando el contenido de nuestros archivos

## Principios de usabilidad y Heurística:

1. **Visibilidad del estado del sistema:** el usuario debería saber que  está pasando en cada interacción con el producto (cargando, guardando,  errores). Debe recibir un feedback del estado del producto.

   

2.  **Relación producto y mundo real:** El usuario no debería tener dudas al  momento de interactuar con el sistema, se le debe brindar toda la  información para que pueda operar el sistema.

   

3.  **Control y libertad del usuario**: El usuario debe poder cancelar o salir de un proceso, sin finalizarlo y sin compromisos.

   

4. **Consistencia:** En el diseño de los bloques visuales del flujo del  sistema, tratar de llevar un patrón en todos los elementos del sistema.

   

5. **Prevención de errores:** Proveer instrucciones claras de lo que se espera que el usuario realice dentro de nuestro producto.

   

6. **Reconocer antes de recordar:** Entregar información valiosa al usuario y ademas proveer una forma en que el usuario pueda revisarla cuando la  necesite sin acudir a su memoria.

   

7. **Flexibilidad y eficiencia de uso:** Entregar una interfaz capaz de  satisfacer a usuarios avanzados y no avanzados. Permitir el uso del  producto sin necesidad de conocimientos especializados.

8. **Diseño estético y minimalista:** no saturar de contenido al usuario,  mostrar únicamente el contenido relevante para cada vista o cada acción  que el usuario ha decidido acceder. No poner elementos que distraigan al usuario del objetivo de la vista.

   

9. **Ayudar al usuario a reconocer y corregir errores:** Dar información al  usuario de lo que esta generando errores o inconsistencias en el  sistema.

   

10. **Ayuda y documentación:** Detectar las dudas mas comunes de los  usuarios a la hora de usar nuestro producto y proveer información que  pueda resolverlas de manera inmediata.

