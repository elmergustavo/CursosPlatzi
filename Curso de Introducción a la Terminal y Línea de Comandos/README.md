<div align="center">
    <h1>Introducción a la Terminal y Línea de Comandos</h1>
    <img src="https://static.platzi.com/media/achievements/badge-terminal-5c5518b5-43d0-4387-b39e-3d85db446c5f.png" width="">
</div>

## Introducción al documento

El contenido de este documento son **apuntes teoricos y prácticos** del [Curso de Introducción a la Terminal y Línea de Comandos](https://platzi.com/cursos/terminal/) y busca ser una guía para futuros trabajos personales. El mismo está dictado por [Mauro Chojrin](https://twitter.com/mchojrin), consultor PHP en [Leeway academy](https://academy.leewayweb.com/). El curso es de [Platzi](https://platzi.com).

El curso se explorará la terminal y como esta optimiza la navegación y ejecución de programas en sistemas operativos Unix. Conociendo y dominando la terminal, se podrá invocar y ejecutar programas, crear directorios de los mismos y navegar en ellos de una manera veloz y eficiente.

## Objetivos del documento

- Aprender a usar la terminal desde cero.
- Domina la interfaz de comandos de la terminal.
- Listar archivos y directorios en la terminal.
- Automatizar tareas con la terminal de comandos.
- Comprender los mecanismos de comunicación y administración entre procesos.
- Administra tus archivos desde la terminal.

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



Apuntes del [Curso de Introducción a la Terminal y Línea de Comandos](https://platzi.com/clases/terminal/)

## - Los Comandos

- **Nombre de un programa**

- **Parámetros:** información adicional para la ejecución del programa. También conocidos como argumentos.

- **Modificadores**: alteran lo que el programa va a hacer. También conocidos como _flags_.

  ```bash
  commnad -flag1 -flag2 arg1 arg2
  
  ```

## - Archivos virtuales

- Punteros que apuntan (valga la redundancia) o otros directorios.
  - **..** ➡ Apunta al directorio anterior (Directorio padre).
  - **.** ➡ Apunta al directorio actual.

## - Utilidades batch

Programas que procesan texto y emiten el resultado

```bash
cat filename.txt # Mostrar el contenido completo de un archivo
head -n 5 filename.txt # Mostrar las primeras x líneas de un archivo
tail -n 5 filename.txt # Mostrar las últimas x líneas de un archivo
```

### Utilidades batch avanzadas

- **grep** ➡ Búsqueda por expresiones regulares

  ```bash
  grep hanks filename.txt # Busca la línea que contenga la palabra "hanks"
  grep -i hanks filename.txt # Búsqueda no case sentitive
  ```

- **sed** ➡ (Stream EDitor). Tratamiento de flujos de caracteres. Soporta expresiones regulares. Se usa mucho para reemplazar expresiones. No modifica el archivo si no que crea un nuevo flujo con las modificacones.

  ```bash
  sed 's/hanks/selleck/g' filename.txt # /s ➡ Sustituir hanks por selleck. /g ➡ Aplicar la sustitución a lo largo de todo el archivo
  ```

- **awk** ➡ Tratamiento de texto delimitado. Muy útil para trabajar con archivos estructurados, como archivos separados por comas, tabs, etc. Admite una especie de lenguaje de scripting que aumenta aún mas sus capacidades.

  ```bash
  awk -F ';' '{ print $1 }' filename.csv # -F establece el delimitador. { print $1 } Imprimir la primera columna
  awk -F ';' 'NR > 1 && $3 > 0 { print $1, $3 * $4 }' # NR número de la columna.
  ```

## - Flujos estándar

Son los canales por donde se ingresan y salen datos de un proceso.

- **Entrada**
- **Salida**
- **Error**

### Redirección

Cambiar el flujo estándar(entrada/salida) de un archivo (por default el teclado) a una opción distinta como por ejemplo un archivo.

```bash
command < file.txt # Redirecciona file.txt al comando especificado. (Redireccionar entrada)
ls > output.txt # Redirecciona la salida del comando a un archivo
ls -l >> file.txt # Redireccionar la salida del comando al final de un archivo ya existente.
```

### Pipes

Toman la salida de un proceso y se la pasan como entrada a otro

```bash
ls -lh | more
```

## - Administración de procesos en background y foreground

- ### Correr procesos en segundo plano:

  Permite correr en segundo plano comandos cuya ejecución tarde un tiempo considerable, para poder así seguir usando la terminal minetras ese proceso se ejecuta.

  ```bash
  curl "https://releases.ubuntu.com/20.04.1/ubuntu-20.04.1-desktop-amd64.iso" $ # $ indica que se proceso se ejecute en segundo plano
  ```

  **Ctrl + Z** ➡ Enviar un comando al background

  ```bash
  fg # Recuperar el comando (mandarlo al foreground)
  ```

- ### Ver procesos que se estan ejecutando:

  - **ps:**

    Utilidad Batch para monitorear procesos

    ```bash
    ps # Procesos que YO estoy ejecutando
    ps ax # Procesos que estoy ejecutando YO y el SISTEMA
    ```

    

  - **top:**

    Utilidad interactiva para monitorear procesos y recursos del sistema

- ### Matar procesos:

  - Obtener identificador (PID) usando **ps** 

    ```bash
    kill -9 127 # -9 Indica que el proceso debe finalizar inmediatamente
    
    killall proccess # Hace lo mismo que el anterior sólo que en lugar del PID toma por argumento el nombre del archivo ejecutable que genera el proceso
    ```

## - Permisos sobre archivos:

- **Dueño:** la persona que creo el archivo.
- **Grupo:** usuarios que pueden acceder a ese archivo.
- **Otros:** que puede hacer con el archivo cualquier otro que no sea el dueño ni este en el grupo.

### Permisos:

Se consultan con:

```bash
ls -l
```



- **Lectura** → r

- **Escritura** → w

- **Ejecución** (depende de si el archivo es ejecutable) → x si es un directorio esta letra indica que se puede acceder a ese directorio.

- **d** → Indica que es un directorio

- **l** → Link. Es un puntero a otro archivo.

  Un - en los permisos significa que dicho permiso no esta disponible para dicho usuario, grupo u otros.

  **Ejemplo:**

  ```bash
  ls -l
  -rwxrwxrwx 1 blooping blooping    4390 Dec 15 11:29 README.md # En este caso la d esta excluida por lo que se trata de un archivo. El dueño tiene permisos de lectura, escritura y ejecución, al igual qu el grupo y los otros usuarios.
  
  # El primer conjunto de permisos son los del dueño, los otros son son los del grupo y los últimos son los permisos de cualquier otro usuario
  ```

  ### Modificar permisos:

  - **chmod:** es el más utilizado, se usa para cambiar el modo del archivo. Permite cambiar individualmente los permisos.

  - **chown:** cambia al usuario propietario de ese archivo.

  - **chgrp:** cambia el grupo de usuarios que puede acceder a ese archivo.

    ```bash
    chmod o-w file.txt # o → Indica que el cambio afectara a los otros usuarios que accedan a ese archivo. - → indica que se quiere quitar un permiso. w → es el permiso a quitar
    
    chmod +x backend.php # Al no especificar a quien afectaran los cambios, el permiso se otorga a todos los que tengan acceso al archivo. + → Inidca que se quiere añadir un permiso. x → el permiso que se quiere añadir
    ```

  ### Notación binaria:

  |  r   |  w   |  x   |       |
  | :--: | :--: | :--: | :---: |
  |  1   |  0   |  0   | **4** |
  |  1   |  1   |  0   | **6** |
  |  1   |  1   |  1   | **7** |

  **Aplicado a cada uno de los permisos disponibles:**

  **Dueño**----------**Grupo**----------**Otros**

  |  r   |  w   |  x   |  r   |  w   |  x   |  r   |  w   |  x   |         |
  | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :-----: |
  |  1   |  1   |  0   |  1   |  0   |  0   |  0   |  0   |  0   | **640** |
  |  1   |  0   |  0   |  0   |  0   |  0   |  0   |  0   |  0   | **400** |
  |  1   |  1   |  1   |  1   |  1   |  1   |  1   |  1   |  1   | **777** |

  Esto se usa para hacer un cambio de todos los permisos (dueño, grupo, otros) en una sola operación.

  ```bash
  chmod 760 file.txt # 7 → El dueño tiene todos los permisos. 6 → El grupo no tiene permiso para ejecutar. 0 → Los otros usuarios no tienen ningún permiso sobre el archivo.
  ```

  El usuario **root** tiene permisos para prácticamente leer y escribir cualquier archivo del sistema. El comando **sudo** se usa para tener temporalmente permisos como usuario root.

  ```bash
  sudo chown www-data backend.php # Cambia el dueño del archivo por www-data
  
  sudo chgrp www-data backend.php # Cambia el grupo del archivo por www-data
  ```

  

## - Manejo de Paquetes

**Administradores de paquetes:** simplifican el proceso de instalación de software. Reúnenfuentes para obtener paquetes de software y automatizan la tarea de descargar el software, moverlo a los directorios donde se encuentran los archivos ejecutables y configurar el software (añadir al PATH en las variables de entorno del sistema, instalar dependencias, etc). **Ejemplos de administradores de paquetes:**

- **apt:** Debian y derivadas  como Ubuntu.
- **zypper:** Suse Linux y derivadas.
- **rpm:** Fedora, RHEL y derivadas.
- **pacman:** Arch Linux y derivadas.

### Usando apt

```bash
sudo apt install lynx # sudo → otorga permisos root. apt install → indica que se quiere usar apt para instalar un programa; otras posibles opciones son update para refrescar las bases de datos de los repositorios de softare y remove para desinstalar un paquete. lynx → es el paquete a instalar
```

- **Paquetes binarios:** paquetes con binarios listos para ejecutarse.

- **Paquetes de lenguajes:** librerías y utilidades hechas para trabajar con determinado lenguaje. **Ejemplos:**
  - **pip:** Package Installer for Python. Gestor de paquetes y dependencias para Python.
  - **npm:** Node Package Manger. Gestor de paquetes y dependencias para  NodeJs.
  - **composer:** Gestor de paquetes y dependencias para PHP.

## - Herramientas de compresión y combinación de archivos

- **Comprimir archivos:**

  ```bash
  gzip db.sql # Creará un archivo comprimido con extención .gz
  gzip -d db.spl.gz # -d → indica que se quiere descomprimir el archivo.
  ```

- **Combinar archivos:**

  ```bash
  tar cf backup.tar backup/* # cf → (Create File) Indica que se va a crear un archivo. backup.tar → nombre del archivo donde se van a agrupar los demás. backup/* → Indica donde estan los archivos que se van a combinar
  
  tar tf backup.tar # tf → Visualizar el contenido que esta dentro del .tar
  
  tar xf backup.tar # xf → Desagrupar el archivo .tar
  ```

  **NOTA:** tar agrupa/combina los archivos, *NO* los comprime por defecto. Si se quiere agrupar y comprimir se usa el siguiente comando:

  ```bash
  tar czf backup.tgz backup/* # czf → comprimir el archivo usando gzip¨. backup.tgz → nombre del archivo donde se van a agrupar y comprimir los demás. backup/* → Indica donde estan los archivos que se van a combinar y comprimir
  
  tar xzf backup.tgz # Desagrupar y descomprimir el archivo
  ```

  

## - Herramientas de búsqueda de archivos

Principales herramientas para búsqueda de archivos:

- **locate:** permite buscar el archivo que se le especifique en todo el sistema de archivos. Funciona mediante una base de datos que se tiene que actualizar periódicamente.

  ```bash
  locate file.txt # Buscar el archivo
  sudo upadatedb # actualizar base de datos
  ```

  

- **whereis:** se usa para ubicar archivos binarios (comandos). Retorna el directorio donde esta guardado el ejecutable de un comando.

  ```bash
  whereis echo
  ```

- **find:** es la herramienta de búsqueda más completa y la vez la más compleja. Busca dentro del árbol de directorios que se le especifique usando una serie de criterios. **Ejemplos:**

  ```bash
  find . -user blooping -perm 644 ## . → Busca en el directorio actual. -user → busca los archivos que corresponden a ese usuario. -perm → busca los archivos que tengan esos permisos.
  
  find . -type f -mtime +7 # -type → buscar por tipo. f → establece el tipo para buscar sólo archivos. -mtime → buscar archivos que fueron modificados en cierto intervalo de tiempo. +7 → establece el intervalo de tiempo en más de 7 días.
  
  find . -type f -mtime +7 -exec cp {} ./backup \; # -exec → establece acciones a ejecutar con el(los) archivo(s) encontrado(s). {} → representa el(los) nombre(s) de el(los) archivo(s) encontrado(s). \; → indica el final del comando.
  ```

  

- ## Herramientas para interactuar a través de HTTP

  Dicho intercambio entre el PC y el servidor se puede dar mediante dos comandos:

  - **curl:** se utiliza para hacer *"pedidos crudos"*. Se hace la petición al servidor, se recibe la respuesta en HTTP y se muestra en la pantalla.

    ```bash
    curl https://platzi.com # Descarga el código HTML de la página solicitada.
    
    curl -v https://platzi.com | more # -v → muestra además del HTML la interacción por HTTP con el servidor.
    
    curl -v https://platzi.com > /dev/null # Mostrar sólo los encabezados HTTP
    ```

    

  - **wget:** es una herramienta un poco más compleja que realiza descargas a un servidor HTTP.

    ```bash
    wget https://www.php.net/distributions/php-7.3.10.tar.bz2
    ```

## - Acceso seguro a otras computadoras

Al conectarse de forma segura los comandos no viajan como texto plano, si no que son encriptados para evitar que cualquier agente malicioso interfiera. Para hacer eso se usa el comando **ssh** (Secure Shell)

```bash
ssh leeway-prod # leeway-prod → perfil de ssh predefinido. Dichos perfiles se definen en el archivo ~/.ssh/config. Ejemplo de configuración:
Host leewat-prod
	HostName 45.55.62.127
	User root
```

- **Enviar emails a través de la terminal:**

  ```bash
  echo "Hello World!" | mail -s "Test" human@example.com # -s → Define el asunto del email. 
  ```

  

## - Qué son y cómo se utilizan las variables de entorno

Es una definición global a la que todos los procesos tienen acceso para tener más información sobre el entorno en el que se esta trabajando, esa información puede ser cosas como el **PATH** que es una variable que almacena las rutas de los directorios que contienen archivos binarios que se pueden ejecutar desde la terminal.

Para ver las rutas que almacena esa esa variable se usa el comando:

```bash
echo $PATH # $ → Le indica al interprete de comandos que expanda el contenido de esa variable.
```

- ### Asignar variables de entorno:

  - **Para un comando:** crear una variable para el próximo comando que se va a ejecutar. No es muy común hacer esto puede ser útil para sobrescribir una variable sin que esto afecte a todos los comandos.

    ```bash
    VAR=valor commnad # command → Comando al que va a afectar dicha variable
    ```

     

  - **Para toda la sesión:** crea una asignación global

    ```bash
    export VAR=valor # VAR → Nombre de la variable.
    ```


## - Cómo y para qué escribir scripts en Bash

**Bash** no sólo es un interprete de comandos, también es un leguaje de programación, su extención es **.sh**. Esto permite ejecutar múltiples comandos con sólo correr un script facilitando enormemente la automatización de tareas.

```bash
#!/bin/bash #Indica cuál es el interpete de comandos que va a ejecutar el script.

mkdir /tmp/wordpress
tar czf /tmp/wordpress/wordpress.`date +%F`.tgz /usr/share/nginx/wordpress # `date +%F → Toma la salida del comando date y la agrega al nombre del archivo
mv /tmp/wordpress.`date +%F`.tgz /root/backups/
rmdir /tmp/wordpress
```

- Se pueden ejecutar scripts desde un archivo bash:

```bash
/root/backup_db.sh
/root/backup_core.sh
```

- Sintaxis básica de Bash Scripting.

```bash
#!/bin/bash

NEW_DIR=hello # Crear variables

if [ ! -d "/root/$NEW_DIR" ]; then # Crear condicional. -d → Verifica si existe el directorio
	mkdir /root/$NEW_DIR
fi # fi finaliza el if

cp backup_code.sh /root/$NEW_DIR/
echo "`date`: Todo listo!"
```

- Ejecutar Script:

  ```bash
  chmod u+x platzi.sh # Otorgar permisos de ejecución
  ./platzi.sh # Ejecutar el script
  ```

- Archivos de configuración de interprete de comandos. Se abren cada vez que se inicia sesión:

  - **/etc/environment:** definición de la variable $PATH

  - **.bashrc:** archivo de configuración de bash

    ```bash
    export PATH=$PATH:/home/platzi/ # Agregar directorio al PATH. Esto se pone en el archivo .bashrc
    
    source .bashrc # Refrescar el archivo en el sistema para tomar los cambios
    ```

    

## - Cómo y para qué dejar tareas programadas

Para programar tareas hay dos opciones:

- **at:** permite programar comandos tomando como referencia la fecha y hora actual.

  ```bash
  at now +2 minutes # Las tareas se ejectaran en 2 minutos contando desde ahora. Al ejecutar el comando se abre otro prompt donde se pueden poner todos los comandos que se quieren programar. Ctrl + d → Finalizar la programación de tareas
  ```

  Si el comando no funciona y arroja el error: *Can’t open /var/run/atd.pid to signal atd. No atd running?* Hay que iniciar los servicios de at y cron. Par ello hay que ejecutar lo siguiente:

  ```bash
  service --status # Revisar si los servicios estan activos
  sudo service atd start # Activar at
  sudo service cron atd # Activar cron
  ```

  

- **cron:** permite dejar comandos programados para que se ejecuten de forma periódica. Utiliza un archivo llamando **crontab**

  ```bash
  crontab -e # Permite ver la tareas que estan programadas y programar nuevas tareas.
  
  45 12 * * * echo "hola" > hola.txt # Primer valor → Minuto. Segundo Valor → Hora. Tercer valor → Día del mes. Cuarto valor → Mes. Quinto valor → Día de la semana. Sexto valor → Comando a ejecutar
  ```
# Terminal and Command Line Course

## Terminal
- **Terminal**: window that shows us the promp, this hosts the shell.
- **Command line**: program that takes commands and passes them to the operating system to do something.

## Learning the terminal
| Command | Description |
| --------- | --------- |
| ls | List the files and folders from the directory |
| ls -l | List the diles and folders with all the info of each |
| ls -lh | List the diles and folders with all the info of each for human reading |
| cd | Moves the terminal to the home directory of the user |
| cd {folder} | Moves terminal to directory |
| clear | Cleans terminal (ctrl + l) |
| pwd | Print Working Directory. |
| file {name_file} | Describe the file's type |

## Manipulating files and directories

| Command | Description |
| --------- | --------- |
| ls -la | List all elements of directory, including hidden ones |
| ls -lS | Lists elements from highest to lowest size |
| ls -lr | Lists elements inversely |
| tree | Show all directories in tree form |
| tree -L {#} | Show all directories to the specified level |
| mkdir {folder} | Creates a new directory |
| touch {file} | Creates a new file |
| cp {original} {copia} | Copy file |
| mv {file} {path} | Move file to path |
| mv {name} {new_name} | Renames file or directory |
| rm {file} | Delete file |
| rm -i {file} | Delete file interactively (pide confirmación) |
| rm -r {folder} | Delete folder recursively |

## File content

| Command | Description |
| --------- | --------- |
| head {file} | Show the first 10 lines of file |
| head {file} -n {#} | Show the first n lines of file |
| tail {file} | Show the last 10 lines of file |
| tail {file} -n {#} | Show the last n lines of file |
| less {file} | Shows the file's content |
| xdg-open | Open file |
| nautilus | Open file system |


## What is a command

| Command | Description |
| --------- | --------- |
| type {command} | Show the command's category |
| alias {alias_name}="{command}" | Creates a termporal alias for a command |
| help {command} | Show info of how to use a command |
| man {command} | Show command's manual |
| info {command} | Show command's manual |
| whatis {command} | Show a short description of command |

## Wildcards

| Command | Description |
| --------- | --------- |
| ls *{.ext} | Filter files that end with extension |
| ls {word}* | Filter files that contain specific word |
| ls {word}? | Filter files that contain 1 character after word |
| ls [[:upper:]]* | Filter files and directories that start with uppercase on all the tree |
| ls -d [[:upper:]]* | Filter files and directories that start with uppercase on current directory |
| ls [[:lower:]]* | Filter files and directories that start with lowercase on all the tree |
| ls -d [[:lower:]]* | Filter files and directories that start with lowercase on current directory |
| ls [ad]* | Show files that start with `a` or `d` |

## Redirections

| Command | Description |
| --------- | --------- |
| ls {folder} > {name}.txt | Save list of files in directory in file.txt |
| ls {folder} >> {name}.txt | If files exist, concatenates list on file.txt |
| ls {folder} 2> {name}.txt | Redirect a stderr to file.txt |
| ls {folder} 2>&1 {name}.txt |Redirect stdout y stderr to file.txt |
| ls -lh \| less | Pipe operator allows a command's stdout to become the stdin of another command |
| echo "{text}" | Print text on terminal |
| cat {file} | Show a file's content |
| ls -ls \| sort | Order command's output |
| cowsay {text} | Print a cow saying the text |
| {command} \| lolcat | Colors output of command |


## Concatenating commands

| Command | Description |
| --------- | --------- |
| ls; mkdir NewFolder; cal | ; chains command to run synchronously |
| ls & date & cal | Commans are executed asynchronously |
| mkdir test && cd test | AND, if a command executes correctly then run the other command |
| cd test || touch file.txt | OR, executes only first command that runs correctly |

## Modify permissions on terminal
| Command | Description |
| --------- | --------- |
| chmod 755 {file_name} | Modifies permissions using octal mode |
| chmod u-r {file_name} | Removes permissions using symbolic mode |
| chmod u+r {file_name} | Gives permissions using symbolic mode |
| whoami | Returns the name of actual user |
| id | Groups the user belong to |
| su root | Changes to root user |
| sudo {command} | Gives root permissions to run command |
| passwd | Change password of current user |

## Environment variables

| Command | Description |
| --------- | --------- |
| printenv | List environment variables |
| echo $variable | Print the content of variable |

## Search commands

| Command | Description |
| --------- | --------- |
| which {bin} | Show path of binary |
| find {path} -name {name} | Search file on path |
| find {path} -type d -name {name} | Search directory on path that matches type and name |
| find {path} -type f -name {name} | Search file on path that matches type and name |
| find {path} -size 20M | Search on path a file with size |
| grep {expReg} {file} | Search all coincidences inside file (case sensitive) |
| grep -i {expReg} {file} | Search all coincidences inside file (not case sensitive)  |
| grep -c {expReg} {file} | Count number of occurrences |
| grep -v {expReg} {file} | Sind all non coincidences |
| wc {file} | Count number of lines, words and bits of file |
| wc -l {file} | Count only number of lines |
| wc -w {file} | Count only number of words |
| wc -c {file} | Count only number of bits |

## Network utilities

| Command | Description |
| --------- | --------- |
| ifconfig | Info of our network |
| ping {website} | Allows detection is a site is active or not |
| curl {website} | Return site's HTML |
| wget {website} | Downloads site's HTML on our computer |
| traceroute {website} | Trace route of all conexions to reach site |
| netstat -i | Show all network devices |

## Compressing files

| Command | Description |
| --------- | --------- |
| tar -cvf {name}.tar {folder} | Compress directory or file with .tar format |
| tar -cvzf {name}.tar.gz {folder} | Compress element with gzip |
| tar -xvf {name} | Decompress .tar |
| tar -xzvf {name} | Decompress gzip |
| zip -r {name}.zip {folder} | Compress element on .zip |
| unzip {name} | Decompress .zip |

## Process management

| Command | Description |
| --------- | --------- |
| ps | Show all processes running on terminal |
| kill {PID} | Stops process excecution |
| top | Show the processes using resources |

<!-- ## ¿Qué es la terminal?
- **Terminal**: es la ventanita que nos muestra el prompt. Este aloja la shell.
- **Línea de comandos**: programa que toma comandos y los pasa al sistema operativo para hacer algo.

## Aprendiendo a caminar en la terminal
| Comando | Descripción |
| --------- | --------- |
| ls | Lista los archivos y carpetas del directorio |
| ls -l | Lista los archivos y carpetas con toda la información de cada uno |
| ls -lh | Lista los archivos y carpetas con información para lectura humana |
| cd | Mueve la terminal al directorio home del usuario |
| cd {folder} | Mueve la terminal al directorio |
| clear | Limpia la pantalla de la terminal (ctrl + l) |
| pwd | Print Working Directory. Imprime la ruta del directorio actual |
| file {name_file} | Describe el tipo de archivo |

## Manipulando archivos y directorios

| Comando | Descripción |
| --------- | --------- |
| ls -la | Lista todos los elementos del directorio, incluyendo los ocultos |
| ls -lS | Listo los elementos ordenados por mayor a menor peso |
| ls -lr | Lista los elementos de manera inversa |
| tree | Despliega todos los directorios en forma de árbol |
| tree -L {#} | Despliega los elementos hasta el nivel ingresado |
| mkdir {folder} | Crea un nuevo directorio |
| touch {file} | crea un nuevo archivo |
| cp {original} {copia} | Copia un archivo |
| mv {file} {path} | Mueve el archivo a la ubicación ingresada |
| mv {name} {new_name} | Renombra el archivo o directorio |
| rm {file} | Elimina el archivo |
| rm -i {file} | Elimina de manera interactiva (pide confirmación) |
| rm -r {folder} | Elimina el directorio de manera recursiva |

## Explorando el contenido de nuestros archivos

| Comando | Descripción |
| --------- | --------- |
| head {file} | Muestra las primeras 10 líneas de un archivo |
| head {file} -n {#} | Muestra las primeras n líneas de un archivo |
| tail {file} | Muestra las últimas 10 líneas de un archivo |
| tail {file} -n {#} | Muestra las últimas n lineas de un archivo |
| less {file} | Muestra el contenido del archivo |
| xdg-open | Abre un archivo |
| nautilus | Abrir el sistema de archivos |


## ¿Qué es un comando?

| Comando | Descripción |
| --------- | --------- |
| type {command} | Muestra la categoria a la pertenece un comando |
| alias {alias_name}="{command}" | Crea un alias temporal para un comando |
| help {command} | Muestra información de cómo usar el comando |
| man {command} | Muestra el manual del comando |
| info {command} | Muestra el manual del comando |
| whatis {command} | Muestra una descripción corta del comando |

## Wildcards

| Comando | Descripción |
| --------- | --------- |
| ls *{.ext} | Filtra archivos que terminen con la extensión |
| ls {word}* | Filtra archivos que contengan una palabra especifica |
| ls {word}? | Filtra archivos que contengan 1 caracter despues de la palabra |
| ls [[:upper:]]* | Filtra archivos y directorios que inicen con mayuscula en todo el arbol |
| ls -d [[:upper:]]* | Filtra archivos y directorios que inicen con mayuscula en el directorio actual |
| ls [[:lower:]]* | Filtra archivos y directorios que inicen con minuscula en todo el arbol |
| ls -d [[:lower:]]* | Filtra archivos y directorios que inicen con minuscula en el directorio actual |
| ls [ad]* | Muestra los archivos que comiencen con a o d |

## Redirecciones

| Comando | Descripción |
| --------- | --------- |
| ls {folder} > {name}.txt | La lista de archivos del directorio se guarda en el archivo .txt |
| ls {folder} >> {name}.txt | Si el archivo ya existe, el listado se concatena al contenido del archivo .txt |
| ls {folder} 2> {name}.txt | Redirige un stderr a una salida por archivo |
| ls {folder} 2>&1 {name}.txt | Redirige el stdout y stderr a una salida por archivo |
| ls -lh \| less | El pipe operator permite que el stdout de un comando se contierta en el stdin de otro |
| echo "{text}" | Imprime en consola el text |
| cat {file} | Muestra el contenido de un archivo |
| ls -ls \| sort | Ordena la salida del comando |
| cowsay {text} | Imprime una vaca diciendo el texto |
| {command} \| lolcat | Colorea la saida del comando |


## Encatenando comandos

| Comando | Descripción |
| --------- | --------- |
| ls; mkdir NewFolder; cal | ; encadena comandos para que se ejecuten de forma síncrona |
| ls & date & cal | Se ejecutan de manera asíncrona |
| mkdir test && cd test | AND, si se cumple cun comando entonces se ejecuta el siguiente |
| cd test || touch file.txt | OR, se ejecuta solo el primer comando que cumpla |

## Modificando permisos en la terminal

| Comando | Descripción |
| --------- | --------- |
| chmod 755 {file_name} | Modifica permisos con el modo octal |
| chmod u-r {file_name} | Quita permisos con el modo simbólico |
| chmod u+r {file_name} | Modifica permisos con el modo simbólico |
| whoami | Devuelve el nombre del usuario actual |
| id | Grupos a los que pertenece el usuario |
| su root | Cambia al usuario root |
| sudo {command} | Da permisos de root para ejecutar el comando |
| passwd | Cambia la contraseña del usuario actual |

## Variables de entorno

| Comando | Descripción |
| --------- | --------- |
| printenv | Lista las variables de entorno |
| echo $variable | Imprime el contenido de la variable |

## Comandos de búsqueda

| Comando | Descripción |
| --------- | --------- |
| which {bin} | Muestra la ruta del binario |
| find {path} -name {name} | Busca en la ruta el archivo |
| find {path} -type d -name {name} | Busca en la ruta un directorio que coincida con el tipo y nombre |
| find {path} -type f -name {name} | Busca en la ruta un archivo que coincida con el tipo y nombre |
| find {path} -size 20M | Busca en la ruta un archivo con el peso |
| grep {expReg} {file} | Busca todas las coincidencias dentro del archivo (case sensitive) |
| grep -i {expReg} {file} | Busca todas las coincidencias dentro del archivo (no case sensitive)  |
| grep -c {expReg} {file} | Cuenta el número de ocurrencias |
| grep -v {expReg} {file} | Encontrar todas las no coincidencias |
| wc {file} | Cuenta la cantidad de líneas, palabras y bits de un archivo |
| wc -l {file} | Cuenta solo el número de líneas |
| wc -w {file} | Cuenta solo el número de palabras |
| wc -c {file} | Cuenta solo el número de bits |

## Utilidades de red

| Comando | Descripción |
| --------- | --------- |
| ifconfig | Información de nuestra red |
| ping {website} | Permite detectar si una página está activa o no |
| curl {website} | Devuelve el HTML del sitio |
| wget {website} | Descarga el HTML directamente a nuestra computadora |
| traceroute {website} | Traza la ruta de todas las conexiones realizadas para llegar al sitio |
| netstat -i | Nos muestra los dispositivos de red |

## Comprimiendo archivos

| Comando | Descripción |
| --------- | --------- |
| tar -cvf {name}.tar {folder} | Comprime el directorio o archivo al formato .tar |
| tar -cvzf {name}.tar.gz {folder} | Comprime el elemento con formato gzip |
| tar -xvf {name} | Descomprime .tar |
| tar -xzvf {name} | Descomprime gzip |
| zip -r {name}.zip {folder} | Comprime el elemento con formato .zip |
| unzip {name} | Descomprime .zip |

## Manejo de procesos

| Comando | Descripción |
| --------- | --------- |
| ps | Muestra los procesos corriendo en la terminal |
| kill {PID} | Detiene la ejecución de un proceso |
| top | Muestra los procesos que están usando más recursos | -->

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
