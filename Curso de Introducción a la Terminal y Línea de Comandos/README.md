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

Explorando el contenido de nuestro archivos.

    Podemos explorar el contenido de archivos sin la necesidad de abrirlos, desde la terminal 🧐. Esto para archivos de texto.
    head <documento de texto>: Nos muestra las primeras 10 líneas de un archivo de texto. Para especificar el número de líneas head -n <numero de lineas> <archivo>
    tail <documento>: Nos muestra las últimas 10 líneas.
    less <archivo>: Este es muy cool, es muy interactivo, nos permite hacer scroll, y nos permite hacer búsquedas haciendo /<palabra a buscar>. Para salir presionamos q 🔍.
    xdg-open <archivo>: Para abrir un archivo desde la terminal. Usa las aplicaciones predeterminadas. Esto para linux, para mac, es open. Esto crea un proceso en la terminal que no nos dejará hacer nada mas. Para terminar el proceso ctrl+c.
    nautilus nos permite abrir el explorador de archivos en una posición dada (en linux) 📁.


    rm -r dir2 dir3 mi_directorio, para borrar múltiples archivos de manera rápida.

    head archivo, para mostrar las primeras 10 líneas del archivo.
    ○ head archivo -n 15, para modificar el número de líneas a mostrar.

    tail archivo, para mostrar las últimas 10 líneas del archivo.
    ○ tail archivo -n 15, para modificar el número de las últimas líneas a mostrar.

    less archivo, muestra una interfaz con todo el archivo, se puede hacer scroll, moverse con las flechas o con la barra espaciadora. Con el “/” seguido de una palabra que se quiere buscar. Para salir solo se presiona “q”.
    • code archivo/wslview archivo, para abrir el archivo con VS desde la terminal.

    Ctrl + c, para matar procesos que se estén ejecutando en la terminal.

    explorer.exe., (windows) para mostrar donde estamos para en el explorador de archivos.

![](https://static.platzi.com/media/user_upload/5-ab8fbaff-9ef7-45f3-a008-b62fa54344a1.jpg)

## ¿Qué es un comando?
Un comando puede ser 4 cosas:

    Un programa ejecutable: que se compilo en algun lenguaje de programación y se puede ejecutar


    Un comando de utilidad de la shell.

    Una función de shell

    Un alias

Comandos

    type nos permite saber que clase es un comando. Por ejemplo type cd (es una funcion de shell), ls (es un alias)

    Para crear un alias: alias ‘nombreDelAlias’ = ‘comandoQueInvoca’. Por ejemploalias l=”ls -lh”. Temporales, por el momento.

    Con –help o help, puedes tener una ayuda sobre los comandos.

    man ‘comando’ : hace referencia al manual de usuario de un comando, otro similar es informático

    whatis ‘comando’ : nos da una descripcion muy corta de que hace ese comando. Pero no funciona con todos.

## Wildcards
Las wildcards nos sirven para realizar seccionamiento de archivos o directorios, ademas de ls los wildcards tambien pueden usarse con cualquier comando que realize la manipulacion de archivos como mv, cp y rm. En este ejemplo yo movi todos los archivo .py hacia una carpeta

Algo importante a aclarar es que el asterisco * significa cualquier STRING o cadena de texto, entonces si ponemos ls *.txt cualquier archivo .txt se listará.
.
Y el signo de interrogación ? significa que ese último dato puede ser cualquier arbitrario, pero sólo ese último.
.

Entonces en resumen, el * se expande de 0 a más caracteres, mientras que ? expande a uno exactamente.

Wildcard

💡Alternativamente llamado como wild character o wildcard character.
.
Definición

    Son un símbolo usado para remplazar o representar uno más caracteres donde comúnmente se utiliza el * .

.
Tipos de wildcards

    % - Usado en SQL para relacionar más de un caracteres 0 o más veces.
    * - Relaciona cualquier carácter 0 o más veces.
    ? - Para relacionar un caracter una vez.
    [ ] - Realizamos relaciones a través de expresiones regular.

Cabe mencionar que los wildcard, pueden ser utilizar como prefijo o postfijo:
# prefijo
dir *.mp3
# postfijo
dir main.*

![](https://user-images.githubusercontent.com/42653934/152705742-881918f9-f9ee-4bd8-9c34-f386f29b6a24.png)

## Redirecciones: cómo funciona la shell
Independiente del lenguaje, cualquier programa tiene un flujo de entrada de datos “STANDAR INPUT” = “<”, un flujo de salida “STANDAR OUTPUT” = “>” o “1>” y un modo de capturar errores “STANDAR ERROR” = “2>”. En la terminal, podemos tener este mismo flujo de datos gracias a: “<” , “>” y “2>”.
TIP: esto es muy utilizado en los logs para definir los estados: [“ok”, “warning”, “error”].
.
Es muy importante recordar que el uso del redireccionamento “STANDAR OUTPUT” = “>” hacia un archivo hace que se borre todo su contenido y se guarde el actual “STANDAR OUTPUT”, si quieres que no se borre la información actual del archivo, tendrías que agregar un doble “STANDAR OUTPUT” por ejemplo:
echo “hola, mundo!” > día.txt
echo “buenas tardes, mundo!” > día.txt
echo “buenas noches, mundo!” >> día.txt
cat día.txt
buenas tardes, mundo!
Buenas noches, mundo!

* https://www.linuxtotal.com.mx/index.php?cont=redireccionamiento-en-linux

## Redirecciones: pipe operator

¡Los pipe operators de Linux son de lo mejor! En serio puedes hacer cosas muy increíbles con ellos. Por ejemplo, yo llegué a hacer un comando super poderoso que me consultaba todos los archivos que tenía guardados en Amazon S3 y me los ponía en varias líneas ordenaditos (porque Amazon te los devuelve con demasiada información desordenada), es más aquí se los enseño (no te asustes por esto, es algo un poquito avanzado, pero quiero que veas cómo usando pipe operators puedes hacer cosas increíbles):

aws s3 ls s3://$BUCKET --recursive | awk '{print $4}' | awk -F/ '{print $NF}'

Aquí uso el comando awk (uno de los comandos que ya te expliqué en otra clase 👀). Claro, no necesitas llegar a hacer cosas complejas para usar pipe operators, puedes hacer cosas sencillas, por ejemplo, buscar tus paquetes instalados en tu computadora y filtrar por alguno específico:
![](https://user-images.githubusercontent.com/42653934/152706538-9e5f83b5-e3a3-4205-9c68-f355bbe5ff4a.png)

Pipe operator |

💡Los filtros son el procesos de tomar una entrada de flujo y, realizando una conversión, es mandado a la salida de otro stream.
.
Definición

    Un pipeline sirve en la construcción de comandos para generar filtros.

.
Pipeline stdout a stdin

Usamos el operado pipe | entre dos comando para direccionar el stdout del primero con el stdin del segundo. Cualquier comando, entre pipes, puede tener opciones o argumentos para construir filtros complejos.

Una de las ventajas de los pipes, en Linux y UNIX, es de que pueden variar y generar salidas intermedias de diferentes procesos, generando todo un trace de flujo de información.

Redirecciones: pipe operator.

    Es uno de los operadores mas útiles que existen, ya que nos permite poner varios comandos, tales que la salida de uno es la entrada del siguiente 📤.
    echo <texto> genera un stdout con el texto que tenemos.
    cat <archivo1> <archivo2> muestra los dos archivos concatenados 💩.
    El pipe operator | hace que el stdout de un comando sea el stdin de otro comando. Por ejemplo ls -lh | less
    tee hace algo parecido a >, pero dentro de los pipe´s, por ejemplo ls -lh | tee output.txt |less . Se puede poner en medio, pero se ignora porque se sigue pasando.
    cowsay "Texto" es un comando que imprime una vaca que dice algo JAJAJAJAJ 🐮.

## Encadenando comandos: operadores de control



