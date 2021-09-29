# Curso de Fundamentos de AWS Cloud

![Logo](https://static.platzi.com/media/achievements/1323-b1cdbbea-6d17-4d0d-a3d1-ec8b5700dae6.png)

**Instructor**: Mauro Parra Miranda

---

# Archivos

1. [Slides](/files/aws.pdf).

# Indice

1. [Introducción al cómputo en la nube](#introducción-al-cómputo-en-la-nube)
    * [¿Qué es el cómputo en la nube?](#qué-es-el-cómputo-en-la-nube)
    * [¿Cómo puedo empezar a usar AWS?](#cómo-puedo-empezar-a-usar-aws)
    * [Introducción a la oferta de servicios de AWS y sus aplicaciones](#introducción-a-la-oferta-de-servicios-de-aws-y-sus-aplicaciones)
2. [Introducción a la oferta de AWS y sus interacciones](#introducción-a-la-oferta-de-aws-y-sus-interacciones)
    * [Ejemplo de arquitectura con Elastic Beanstalk](#ejemplo-de-arquitectura-con-elastic-beanstalk)
    * [¿Qué es EC2?](#qué-es-ec2)
    * [Creando una instancia de EC2](#creando-una-instancia-de-ec2)
    * [Conectándonos a nuestra instancia desde Windows](#conectándonos-a-nuestra-instancia-desde-windows)
    * [Conectándonos a nuestra instancia desde Linux](#conectándonos-a-nuestra-instancia-desde-linux)
    * [Conectándonos a nuestra instancia desde OSX](#conectándonos-a-nuestra-instancia-desde-osx)
    * [Subiendo un proyecto: Clonando un repositorio de GitHub a nuestra Instancia de EC2](#subiendo-un-proyecto-clonando-un-repositorio-de-github-a-nuestra-instancia-de-ec2)
    * [Subiendo un proyecto a nuestra instancia de EC2: Ejecutar nuestro proyecto](#subiendo-un-proyecto-a-nuestra-instancia-de-ec2-ejecutar-nuestro-proyecto)
    * [¿Qué es Lambda y Serverless?](#qué-es-lambda-y-serverless)
    * [Creando una función Lambda con Python](#creando-una-función-lambda-con-python)
3. [Elastic Beanstalk](#elastic-beanstalk)
    * [Conociendo Elastic Beanstalk](#conociendo-elastic-beanstalk)
    * [Creando un ambiente en Elastic Beanstalk](#creando-un-ambiente-en-elastic-beanstalk)
    * [Almacenamiento - S3](#almacenamiento---S3)
    * [Almacenamiento con S3: Contenido Estatico](#almacenamiento-con-s3-contenido-estatico)
    * [Almacenamiento con Glacier: Contenido duradero](#almacenamiento-con-glacier-contenido-duradero)
4. [Bases de Datos](#bases-de-datos)
    * [Bases de Datos - RDS Aurora PG](#bases-de-datos---rds-aurora-pg)
    * [Conociendo RDS PG](#conociendo-rds-pg)
    * [Creando una base de datos Platzi DB](#creando-una-base-de-datos-platzi-db)
    * [Conociendo Aurora PG (Postgress)](#conociendo-aurora-pg-postgress)
    * [Haciendo una migración a Aurora DB](#haciendo-una-migración-a-aurora-db)
    * [Mejores prácticas de Bases de Datos y RDS](#mejores-prácticas-de-bases-de-datos-y-rds)
5. [Redes](#redes) 
    * [Route53](#route53)
6. [Herramientas de administración](#herramientas-de-administración)
    * [Herramientas de administración - IAM](#herramientas-de-administración---iam)
    * [Utilizando IAM](#utilizando-iam)
    * [CloudWatch](#cloudwatch)
    * [CloudTrail](#cloudtrail)
7. [Seguridad](#seguridad)
    * [Certificate manager](#certificate-manager)
    * [GuardDuty](#guardduty)
8. [Bonus](#bonus)
    * [AWS Rekognition](#aws-rekognition)
    * [Creando nuestro servicio de Postgres](#creando-nuestro-servicio-de-postgres)
    * [Accediendo a nuestra base de datos Postgres](#accediendo-a-nuestra-base-de-datos-postgres)

---

# Introducción al cómputo en la nube

## ¿Qué es el cómputo en la nube?

**En AWS el cómputo en la nube trata de los siguiente:**

1. **Sitios web**: Principalmente, lo clásico, sitios web, que pueden ser desde una sola computadora con una arquitectura básica LAMP (Linux, Apache, MySQL & PHP) a construir grandes infraestructuras, soportar muchísimos usuarios sin ningún tipo de dificultad.
1. **Respaldos y recuperación**: AWS brinda la posibilidad de que en cualquier momento se pueda hacer respaldos y recuperar información, como puede ser recuperar una máquina completa, o tener respaldos de varias etapas del desarrollo de un proyecto.
1. **Archivos permanentes**: AWS permite almacenar archivos estáticos, como pueden ser imágenes o archivos de cualquier tipo o extensión.
1. **DevOps**: En este área, no solamente se cuenta con automatización en el release de los nuevos proyectos, sino también con una alta disponibilidad o respaldos automatizados en diversos lugares del mundo, que pueden ser diarios y pueden ser escalables, como por ejemplo, desde 5 usuarios hasta 3000 en dos minutos.
1. **Análisis masivos**: AWS permite la realización de cálculos de analíticos de forma masiva; es decir, no sólo el procesamiento de los analíticos típicos y populares que implementan en los sitios web, sino también se pueden hacer mediciones de diversos datos y tipos de información. Por ejemplo, el análisis de la CPU y/o memoria RAM consumida por una aplicación en diversos servidores.
1. **Cómputo Serverless**: Con este servicio, no es necesaria la preocupación por la cantidad de computadoras o cómo y cuándo se va a escalar el servicio. AWS permite realizar una partición del software; no a nivel de componentes, sino casi que a nivel de funciones; las cuales son expuestas a través de microservicios, los cuales pueden interactuar entre ellos. Amazon no cobra por el tamaño de estos microservicios, sino por la utilización o llamadas hacia éstos; y en caso de que dichas llamadas sean muy frecuentes, serán escalados los microservicios.
1. **Cómputo de alto rendimiento**: Levanta los servidores necesarios para computar a un alto rendimiento sólo las veces que la aplicación lo requiera.
1. **IOT**: En este área, AWS no sólo brinda la parte del hardware, que sería tener acceso a hardware de una manera relativamente rápida y fácil, sino también todo lo que incluye interactuar con dichos dispositivos, el gateway para permitir el ingreso de la información, y además, puede escalar de manera automática cuando se necesite.
1. **Aplicaciones empresariales**: AWS tiene aplicaciones empresariales tradicionales, como por ejemplo, correos empresariales, que, al igual que otros servicios, escala de manera automática y profesional.
1. **Distribución de media**: Con este servicio, AWS te brinda mecanismos de transcoding. Por ejemplo, si se desea realizar un streaming, este servicio brinda todo lo necesario para poder llegar a la cantidad de personas que se quiera.
1. **Servicios móviles**: Estos servicios son esenciales para lograr una correcta interacción entre una aplicación móviles con otros servicios, como con una base de datos, el backend, etc.
1. **Cómputo científico**: AWS tiene máquinas especializadas (más memoria RAM, más CPU, más cores trabajando al mismo tiempo, etc.) para el cómputo enfocado a la parte científica, como pueden ser, simulaciones físicas, simulaciones financieras, etc.
1. **E-commerce**: Este servicio incluye todos los componentes necesarios para hacer una página de ventas virtual. Entre esos componentes, están la parte de seguridad, comunicación con la base de datos de manera segura, tantos servidores como sean necesarios; del lado de la base de datos incluye respaldos, optimizaciones para expandir o disminuir la base de datos de acuerdo al uso, etc.
1. **Ambientes híbridos**: Este área de AWS brinda la posibilidad de poder trabajar con información en la nube, y al mismo tiempo con datos de manera local hosteados en un servidor propio.
1. **Blockchain**: Este sistema permite realizar acciones, como por ejemplo, minar, hacer análisis de la información para verificar que no esté siendo modificada o alterada en el camino, entre otras.

AWS ha crecido a un ritmo de más del 50% por año, tanto en clientes como en servicios.

**Ventajas de AWS:**

1. Usa lo que necesites, apaga lo que no: AWS brinda la posibilidad de encender los servicios cuando se vaya a hacer uso de ellos y de apagarlos cuando no se vayan a utilizar. De esta manera, AWS sólo cobra por el tiempo en el que utilicemos dichos servicios.
1. Crece tanto como sueñes: AWS permite una escalabilidad a alta velocidad. Esto facilita la posibilidad de crecer o decrecer tanto como se necesite.
1. Velocidad cuando la necesitas: AWS no sólo brinda la posibilidad de administrar y de escalar a nivel de hardware, también se puede hacer con la velocidad de cómputo los servidores.
1. Cobertura mundial: Amazon tiene diversos datacenters en distintos lugares del mundo, y no sólo en distintos lugares del mundo, sino que, por ejemplo, Amazon tiene un datacenter en Brasil, pero no es únicamente un datacenter; son tres o cuatro edificios llamados “zonas”, es decir, cuatro zonas en ese datacenter, cada una con electricidad autónoma, con datos autónomos, etc. de tal manera que se puede tener la confianza de que aunque fallase algún datacenter, hay otros dos o tres que van a responder por el que esté fallando. En ciertos lugares hay limitaciones, como por ejemplo, en los datacenters de China no se pueden almacenar cierto tipos de datos o de información. También es bueno tener en cuenta la ubicación de los datacenters; por ejemplo, en Latinoamérica, el más cercano es el de Brasil, por lo que ese datacenter va a ser mejor en términos de latencia y en temas por el estilo.


Una instancia de AWS EC2 es gratis todo tu primer año.

### Regiones de AWS

![Regiones](/images/regiones.png)

[Programas de AWS para investigación y educación](https://aws.amazon.com/es/grants/).

## ¿Cómo puedo empezar a usar AWS?

Para crear tu cuenta de AWS debes entrar a [aws.amazon.com](aws.amazon.com), recuerda que para crear tu contraseña puedes usar [passwordsgenerator.net](passwordsgenerator.net).

AWS dispone de dos programas que permiten a los clientes trasladar sus enseñanzas y esfuerzos de investigación a la nube y de este modo innovar más rápidamente y con un menor costo. Para aplicar a las becas de AWS entra a [aws.amazon.com/es/grants](aws.amazon.com/es/grants).

Cuando tengas tu cuenta registrada, entra a [console.aws.amazon.com](console.aws.amazon.com) y tendrás acceso a la consola de amazon con todos los servicios disponibles.

## Introducción a la oferta de servicios de AWS y sus aplicaciones

En la siguiente lista se encuentra la oferta de servicios con algunas de sus aplicaciones más importantes o que nos pueden servir:

* Computo: Máquinas virtuales, serverless, infraestructura, etc.
* Storage: Administrar archivos.
* Bases de Datos: Opciones como Postgrade, MySQL, etc.
* Migración de Servicios: Si ya tienes datos en una data center, te ayuda a poder migrarlos.
* Networking & Content Delivery: Registrar dominios, administrar certificados SSL y más.
* Herramientas de Desarrollador: Para facilitar la colaboración entre desarrolladores como xcode, commits, etc.
* Herramientas de Administración: (CloudWatch: Permite ver que está sucediendo en tu infraestructura o en tus servidores. CloudTrail: Permite llevar una auditoria accesos y permisos y saber qué es lo que hacen).
* Media Services: Como Elastic Transcoder que sirve si por ejemplo estás haciendo streaming de un partido podrías subir el dato que estas generando como vídeo y ellos generaran todas las versiones que necesitas para diferentes tipos de dispositivos ya sean celulares, computadoras, etc.
* Machine Learning: Como Rekognition que puedes ir enviando imágenes y te puede reconocer que estás viendo.
* Analytics: Cuanta RAM está usando cada visitante, cuanto CPU, que actividad está teniendo ese visitante en tu sitio.
* Seguridad: Como IAM que sirve para manejar a que tienen acceso la cuenta de los colaboradores.
* GuardDuty: Te permite hacer un recuento de los diferentes accesos de red que ha habido, entonces si hubiese un ataque a un servidor te va a permitir saber de dónde viene el ataque y te va dar opciones].
* Servicios Móviles: Te permite generar tus propios servicios móviles de forma más sencilla.
* AR & VR: Ya viene con el software instalado y puedes empezar a hacer identificación de algún patrón para empezar a enseñar alguna cosa en tu aplicación.
* Integración de Aplicaciones: Como Simple Notification Service: Se puede hacer llamado a diferentes servicios, ejemplo: Enviar notificaciones a través de correo electrónico, SMS.
* Customer Engagement: Sirve más para uso empresarial, como correo electrónico, cuentas de Amazon, etc.
* Bussiness Productivity: Permite usar Alexa para negocios, cargar documentos al correo empresarial, etc.
* Desktop & App Streaming: Como WorkSpaces que sirve si en algún momento necesitas compartirle a alguien alguna máquina virtual de cierta manera, que tenga un escritorio como Windows y que esa máquina tenga un navegador y que solo se pueda conectar al sitio de la empresa, escuela, etc.
* Internet of Things: Puede proveer de hardware y te permite crear servicios para que fácilmente puedas administrarlos, como conectarlos con datos o aplicaciones web.
* Game Development: (Motor de juegos) Puedes generar un juego con el software que te proporcionan. Crear escenas, interacción.

# Introducción a la oferta de AWS y sus interacciones

## Ejemplo de arquitectura con Elastic Beanstalk

Hay muchas formas de desarrollar un sistema en AWS, una de ellas es la arquitectura Elastic Beanstalk.

Esta arquitectura tiene como ventaja la alta disponibilidad y la eficiencia para atender una gran cantidad de usuarios.

* AWS Elastic Beanstalk: es un servicio de ASW que se utiliza para implementar y escalar servicios y aplicaciones web desarrolladas en JAVA, .NET, PHP, Node.js, Python, Go, entre otros, en servidores familiares como Apache y Nginx. Además se encargará de administar de manera automática la implementación, el aprovisionamiento de la capacidad, el equilibrio de la carga y el escalado de nuestra aplicación.
* CloudWatch: es un servicio de monitorieo y administración creado para desarrolladores, operadores de sistemas, entre otros. El servicio ofrece datos e información procesable para monitorear las aplicaciones, comprender cambios de rendimiento que afectan al sistema, optimizar recursos y lograr una vida unificada del estado de las operaciones.

![Elastic Beanstalk](https://github.com/elmergustavo/CursosPlatzi/blob/master/Curso%20de%20Fundamentos%20de%20AWS%20Cloud/images/elastic-beanstalk.png)

[Youtube: Introduction to AWS Elastic Beanstalk](https://www.youtube.com/watch?v=SrwxAScdyT0)

## ¿Qué es EC2?

"EC2 son un conjunto de maquinas virtuales en línea que puedes utilizar para desarrollo, calidad o producción. Estas son algunas de sus características:

* **Instancias**: Máquinas virtuales con diversas opciones de Sistema Operativo, vCPU, RAM, Disco Duro, etc.
* **Seguridad**: Generación de llaves únicas para poder conectarse a tu máquina Linux o Windows de forma segura.
* **Espacio**: Diversas opciones de espacio en disco duro, virtualmente infinito.
* **Redundancia**: Puedes tener diversas copas de la misma máquina en diversas regiones geográficas.
* **Firewall**:Puedes controlar de manera muy fina desde donde te puedes conectar a la máquina y por qué puertos.
* **Direcciones IP estáticas**: Puedes optar por comprar una IP pública estática para que siempre puedas poner la última versión o la última máquina en esa IP.
* **Respaldos**: Puedes respaldar toda la máquina (Ambiente, Sistema operativo, todo) cada que quieras.
* **Escalable**: En caso necesario, puedes incrementar o decrementar los recursos de la máquina: más vCPUs, más RAM, etc.
* **Migración de snapshot**: Puedes copiar un snapshot a otras regiones, en caso de que cualquier cosa suceda en la que estas.

Recuerda que puedes ver la documentación oficial de EC2 [Aquí](https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/concepts.html).

## Creando una instancia de EC2

Logueados en la [consola de amazon](https://console.aws.amazon.com) seguimos los siguientes pasos.
1. Desplegamos servicios de Amazon.
2. Desplegamos Informática.
3. Clic en EC2.
![Panel EC2](/images/panel-ec2.png)
4. Clic a 'Launch Instance'.
5. Se selecciona la Amazon Machine Image (AMI). Cuidado, no todas sirven para lo mismo, hay algunas que son gratuitas de propósito general, como hay de pago tanto de propósito general como específico, por ejemplo, ML, DL.
![AMI](/images/ami.png)
6. Se selecciona la instancia. La instancia son las propiedades de la máquina, procesador, ram, almacenamiento, capacidad de la red, compatibilidad IPV6.
![Instancia](/images/instancia.png)
7. Se configuran detalles de la instancia. Por lo general no es necesario editar nada acá.
![Detalles](/images/instance-details.png)
8. Se configuran los detalles del almacenamiento. Como estamos en la capa gratuita, no es recomendable mover nada acá. Este espacio es configurable, dependiendo de nuestras necesidades.
![Almacenamiento](/images/storage-details.png)
9. Se configuran las etiquetas. En este caso, se le asignó la llave: 'Name'; y el valor: 'Platzi Lab'.
![Tags](/images/tags.png)
10. Se configura el grupo de seguridad. Para propósitos de la clase, se le colocó el nombre del grupo: "platzi-solo-ssh". Tipo: SSH. Source: Anywhere.
![Security](/images/security.png)
11. Se verifica la información, si es correcta, clic en 'Launch'.
![Review](/images/review.png)
12. Nos aparece una pantalla en la que nos pide seleccionar el SSH, como no tenemos le damos a crear un nuevo par, se le coloca un nombre, se descarga y por último, se lanza la instancia. Importante, la llave descargada debemos reservarla con absoluto recelo, ya que es nuestro único método para poder acceder a la instancia.
![SSH](/images/platzi-ssh.png)

Nos muestra una pantalla de confirmación que la instancia se está iniciando.
![Iniciando](/images/instance-launching.png)

Si le damos clic al id nos mostrará la información general de la instancia que acabamos de crear.
![Instancia](/images/instance-created.png)

## Conectándonos a nuestra instancia desde Windows

Sistemas UNIX como Mac y Linux traen por defecto una terminal predeterminada que funciona perfecto para conectarte por SSH (secure shell) a nuestras instancias en AWS. Sin embargo, en Windows no hay alternativas nativas que funcionen tan bien, así que puedes usar [MobaXterm](https://mobaxterm.mobatek.net/), un software que te ayudara a conectarnos a nuestras instancias, ademas de muchos otros beneficios.

Recuerda que tienes las siguientes responsabilidades:

* Updates: Con las instancias, nosotros somos totalmente responsables de la actualización de OS
* Respaldos: Nuestra instancia no se respaldará sola, tendremos que hacerlo nosotros.
* Restauración snapshot: Podemos hacer respaldos antes de hacer grandes cambios para poder hacer rollback del Sistema en caso necesario.

## Conectándonos a nuestra instancia desde Linux

Abrimos una nueva terminal, nos ubicamos en el directorio donde se almaceno el archivo pem y ejecutamos el siguiente comando.
```bash
chmod 6000 'nombre-llave'.pem
ssh -i platzi-prueba.pem ec2-user@3.85.231.75

load pubkey "platzi-prueba.pem": invalid format
The authenticity of host '3.85.231.75 (3.85.231.75)' can't be established.
ECDSA key fingerprint is SHA256:QQQcNsV1z508bC+hFyFMuR2sGNlz7RjRWt3/TaXXFaA.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '3.85.231.75' (ECDSA) to the list of known hosts.

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
```
Con esto ya quedamos logueados en la terminal del servicio de Amazon.

## Conectándonos a nuestra instancia desde OSX

Aplica el mismo procedimiento para Linux.

Si muestra que hay un error con el archivo pem, que tiene demasiados permisos, se soluciona utilizando el comando:
```bash
chmod 600 'llave'.pem
```
Y se vuelve a ejecutar el comando.

## Subiendo un proyecto: Clonando un repositorio de GitHub a nuestra Instancia de EC2

Para clonar repositorios desde tu instancia de AWS necesitas instalar git:
```bash
# Permisos de super usuario
sudo su
# Instalación de git
yum install git
```
Teniendo git instalado ya podemos clonar el repositorio que necesitemos:
```bash
git clone [URL_DEL_PROYECTO]
```
En el siguiente [link](https://github.com/mauropm/aws-platzi-python) vas a encontrar el repositorio con el que vamos a trabajar en la clase. Para que el clonado salga bien, no se debe utilizar por medio de llave SSH, sino por medio de HTTPS.

## Subiendo un proyecto a nuestra instancia de EC2: Ejecutar nuestro proyecto

Ahora que clonamos nuestro repositorio, vamos a instalar las dependencias necesarias para que funcione. El proyecto que trabajamos en clase sólo necesita una dependencia:
```bash
# Permisos de super usuario
sudo su
# Instalación de flask
pip install flask
```
En mi caso no tenía instalado pip, sino una versión antigua de Python 2, lo solucioné instalando python3 y luego ejecutando con pip3.
```bash
yum install python3

pip3 install flask
```
Con las dependencias instaladas podemos correr nuestro servidor, en el caso de nuestro proyecto es con el siguiente comando:
```bash
python3 app.py
```
Para acceder por internet a nuestro servidor tenemos que buscar nuestra instancia de EC2 y copiar la IP pública, pero no es suficiente. Debemos entrar a Security Groups, Inbound y añadir una regla Custom TCP Rule, escribe el puerto en el que corre tu servidor (que para nuestro proyecto es el 5000) y en la opción Source elije Anywhere.

![Inbound Rules](/images/inbound-rules.png)

Recuerda que para encontrar tu IP pública puedes entrar a [whatismyip.com](whatismyip.com).

![Proyecto corriendo](/images/proyecto-corriendo.png)

## ¿Qué es Lambda y Serverless?

Lambda es un proyecto de AWS muy relacionado con el concepto de Serverless, dejar la administración de tus servidores en manos de Amazon para solo encargarte de las funciones de código que ejecutara tu aplicación.

**¿Qué son?**

Imagina lambda como un lugar donde puedes ejecutar funciones de tu código.

**Serverless**

No existe un servidor como vimos en EC2, es decir, solo está el código en lamba y AWS se encarga de ejecutarlo cuando necesites.

**Lenguajes soportados**

Puedes programar funciones lamba en Nodejs (JavaScript), Python, Java (8), C# (.Net Core) y Go.

**Recuerda tener en cuenta los siguientes puntos:**

* **Memoria**: Mínima de 128MB, máxima 3000MB con incrementos de 64MB.
* **Límites de ejecución y espacio**: Puedes correr tu aplicación hasta 300 segundos y tienes un /tmp limitado a 512MB.
* **Ejecución paralela**: Esta limitada a 1000 ejecuciones concurrentes (a un mismo tiempo), no tiene límite en ejecuciones secuenciales (una detrás de otra).

**Ventajas de Lambda:**

* **Seguridad**: Al ser una infraestructura compartida, no tienes que preocuparte de seguridad: AWS maneja todo.
* **Performance**: AWS está monitoreando constantemente la ejecución de tus funciones y se encarga de que siempre tenga el mejor performance.
* **Código aislado**: Tu código, aún estando en una infraestructura compartida, corre en un ambiente virtual exclusivo, aislado de las demás ejecuciones lamba.

Recuerda que AWS te regala 1 millón de peticiones lamba gratis el primer año.

## Creando una función Lambda con Python

Abrimos la consola de AWS. Desplegamos los servicios, en compute, le damos clic a Lambda.

![Lambda](/images/lambda.png)

Seguimos los siguientes pasos:
1. Le damos nombre:  platzifunc.
2. Seleccionamos el lenguaje: Python 3.8.
3. Seleccionamos el rol.

![Lambda Config](/images/lambda-config.png)

Nos muestra el siguiente dashboard.

![Labda Dashboard](/images/platzifunc-dashboard.png)

Escribimos el siguiente código en la función lambda `lambda_function.py`, guardamos y damos clic en deploy.
```py
import os

def lambda_handler(event, context):
    what_to_print = os.environ.get("what_to_print")
    how_many_times = int(os.environ.get("how_many_times"))

    # make sure what_to_print and how_many_times values exist
    if what_to_print and how_many_times > 0:
        for i in range(0, how_many_times):
            # formatted string literals are new in Python 3.6
            print(f"what_to_print: {what_to_print}.")
        return what_to_print
    return None
```
En el dashboard hay un apartado de las variables de ambiente. Creamos nuestras variables cómo aparecen en nuestro código y le asignamos valores.

![Environment variables](/images/environment.png)

Ahora, se crea un evento de prueba, en el dashboard, en la parte de arriba dice Test, dar clic ahí y crear el test que viene por defecto. Dar nombre cualquiera. Una vez creado dar clic en Test y saldrá el siguiente resultado.

![Test](/images/lamda-test.png)

# Elastic Beanstalk
## Conociendo Elastic Beanstalk

Elastic Beanstalk es una plataforma donde en pocos pasos, obtienes un balanceador de cargas y tantas instancias EC2 como tu quieras.

Este ambiente puede escalar de manera dinámica de acuerdo al tiempo de respuesta a los usuarios, uso de CPU, uso de RAM, etc.

Esta herramienta soporta los siguientes ambientes:
* Docker Image
* Go
* Java SE
* Java con Tomcat
* .NET + Windows Server + IIS
* Nodejs
* PHP
* Python
* Ruby

![Arquitectura Elastic Beanstalk](/images/elastic-beanstalk.png)

[Youtube: Introduction to AWS Elastic Beanstalk](https://www.youtube.com/watch?v=uiM1xzOX8Qg)

## Creando un ambiente en Elastic Beanstalk

Ingresamos a la plataforma de Elastic Beanstalk, en la página principal de la consola de Amazon.

![Plataforma](/images/aws-elastic-beanstalk-platform.png)

Seguimos los siguientes pasos:

1. Clic a 'Create Application'.
2. Registramos la información:
    * Nombre: platzi
    * Platform: Python
    * En esta ocasión seleccionamos la opción de crear aplicación de muestra.
    * Clic a 'Create Application'.
![Data platform](/images/beanstalk-creation.png)

Va a empezar a crear el elastic load balancer, luego una máquina o una instancia con Python para poder instalar lo que se desee, etc.

Nos dirigimos al repositorio usado para la instancia de EC2, pero esta vez seleccionamos la rama "elastic-beanstalk".

Amazon requiere cierta configuración especial para poder poner a funcionar el código, entre ellos está la creación de un directorio `.ebextensions` en el que irán algunas configuraciones de flask, y el archivo `app.py` no puede tener este nombre, sino `application.py`, y la variable `app` dentro de este archivo se llame `application`. Si esto no se cumple, amazon nos dirá que no se cumple con el standar WSGI.

Una vez cargada la instancia de Beanstalk, comprimimos la carpeta en la que está el repositorio [específico para elastic beans](/code/aws-platzi-python-elastic-beanstalk.zip). Y en la pantalla de la plataforma se le da clic a 'Upload and deploy', y seleccionar el archivo comprimido.

![Beanstalk](/images/beanstalk.png)

No me funcionó el archivo generado en el repositorio, viendo los comentarios, es porque no es necesario el directorio `.ebextensions`, y hay que crear el archivo requirements.txt con flask como requisito. **¡Funciona!**.

Si por algún error se hace un mal deploy, se puede cambiar la versión, se le da clic a 'Upload and Deploy', y se le da clic a 'Application Versions page'.

![Deploy](/images/deploy.png)

Luego se selecciona la versión deseada.

![Versiones](/images/versions.png)

Se pueden almacenar hasta 1000 versiones diferentes de una aplicación. Igualmente, en el dashboard de la aplicación podemos ver la salud del servicio, las configuraciones, eventos, etc.

Dentro de las configuraciones podemos configurar cómo se va a comportar el servicio cuando empiece a recibir más carga de trabajo, cuántos servidores se añadirán, de a cuántos se decaerá, cómo se comportará si el servidor se cae, si se mata y se crea uno nuevo, etc.

## Almacenamiento - S3

AWS te permite guardar archivos en su plataforma, de tal forma tus instancias EC2, Lambda u otras son efímeras y puedes borrarlas sin preocupación alguna.

Existen dos grandes opciones para almacenamiento en AWS:

* S3: Es un repositorio de archivos rápido y perfecto para uso de una aplicación a la hora de crear, manipular y almacenar datos.
* Glacier: Es un servicio de almacenamiento en la nube para archivar datos y realizar copias de seguridad a largo plazo.

Con S3, AWS te permite guardar archivos en su plataforma, de tal forma, tus instancias EC2, Lamba u otras son efímeras y puedes borrarlas sin preocupación alguna. Tambien te permite hacer respaldos en tiempo prácticamente real en otras regiones de AWS.

## Almacenamiento con S3: Contenido Estatico

En la pantalla principal de la consola de AWS, nos dirigimos al apartado de Storage y seleccionamos S3.

1. Seleccionamos crear bucket.
![Bucket](/images/s3-bucket.png)
2. Llenamos la información:
    * Nombre: platzi-oscar1.
    * Se selecciona la región.
    * Se selecciona la configuración de otro bucket (opcional).
    * Se permite el acceso público del bucket.
![Bucket config](/images/bucket-config.png)

Una vez el bucket ha sido creado, lo abrimos y subimos [1 archivo](/code/aws-estatico/index.html).

Una vez el archivo ha sido subido, lo seleccionamos con el checkbox, a la parte superior izquierda hay una lista desplegable llamada "Actions", se selecciona "Make public" y se confirma esta decisión.

Ahora, queremos que este archivo sea parte de un hosting estático, para eso, se selecciona propiedades del bucket, y nos dirigimos al apartado "Static website hosting", editamos, habilitamos y seleccionamos el archivo index.html como el indice.

![hosting s3](/images/hosting-s3.png)

Creamos una regla de replicación. Esta regla necesita el versionado de los archivos, se habilitan. Se coloca el nombre de la regla de replicación, se selecciona la regla a todos los objetos en el bucket, se selecciona un bucket donde se hará la replicación, se selecciona un rol y se guarda la información.

![Replicación](/images/replicacion-s3.png)

Volvemos a los permisos y verificamos la url creada para el archivo estático.

![Estático](/images/s3-estatico.png)

## Almacenamiento con Glacier: Contenido duradero

AWS tiene un tipo de almacenamiento más económico, pero también más lento que S3 llamado Glacier. Es una muy buena opción si tienes que guardar algún tipo de archivo histórico, como documentos de transacciones de años pasados.

Glacier podrá entregarte tus datos y/o archivos con tiempos de entre 2 y 15 minutos por archivo.

# Bases de Datos

## Bases de Datos - RDS Aurora PG

AWS creó un producto llamado RDS que optimiza el funcionamiento de un motor de bases de datos. Este servicio incluye mantenimiento a tu base de datos, respaldos diarios, optimización para tu tipo de uso, etc.

RDS tiene varias opciones de motores de bases de datos, como: Aurora PG, Aurora MySQL, MySQL, MariaDB, PostgreSQL, Oracle y Microsoft SQL Server.

Recuerda que AWS te da 750 horas de servicio gratis de RDS, incluyendo cualquiera de los motores de bases de datos.

**Nota**: Los motores de bases de datos como Oracle y Microsoft SQL Server, han sido considerados por mucho tiempo como motores empresariales o tipo Enterprise debido a que ofrecen unas prestaciones interesantes como Backups fáciles, redundancia, tolerancia a fallos, etc. AWS a través de RDS, ofrece estas prestaciones y más; por lo que ya no es necesario tener estos factores en cuenta a la hora de escoger el motor de base de datos para un nuevo proyecto.

## Conociendo RDS PG

AWS implementa el motor de PostgreSQL (RDS PG) en una instancia optimizada para correr con la máxima eficacia.

RDS PG incluye, por omisión, tareas de optimización como vacuum, recuperación de espacio en el disco duro y planificación de queries. Tambien te permite hacer respaldos diarios (o incluso más seguido) de tu base de datos.

Otras ventajas de RDS PG son:

* **Cifrado** a tu elección, tu base de datos puede estar cifrada en disco duro

    [Cifrado de recursos de Amazon RDS](https://docs.aws.amazon.com/es_es/AmazonRDS/latest/UserGuide/Overview.Encryption.html).

* **Migración asistida**: RDS PG tiene mecanismos que te ayudan a migrar tu información en caso de que tu ya cuentes con una base de datos con otro proveedor.
* **Alta disponibilidad**: RDS PG te permite fácilmente configurar un ambiente de alta disponibilidad al ofrecerte diversas zonas para tu base de datos.

Recuerda que Amazon RDS provee de seguridad por omisión tan alta que no podrás conectarte a tu DB hasta que explícitamente lo permitas.

## Creando una base de datos Platzi DB

**¡Precaución!** Le sucedió a una estudiante de Platzi.

> MUCHO CUIDADO! hermanos ya se que es obvio pero deben tener mucho cuidado con que seleccionan y ASEGURARSE de que es gratuito, porque sino lo es amazon no te va a notificar( estar en la tier gratuita no te asegura que amazon no te va a cobrar, solo hace que no te cobren algunas cosas ) y no se vera inmediatamente reflejado en la facturacion, yo accidentalmente seleccione una base de datos mucho mas grande (la cual viene como la opción por defecto en la nueva versión del formulario) y en 20 dias me cobraron #500 USD#!!!, no les vaya a pasar lo mismo

Para crear nuestra DB seguimos los siguientes pasos:
1. En la consola de AWS, buscamos 'Database' y le damos clic a RDS.
![RDS](/images/rds-main.png)
2. Clic a 'Create Database'.
3. Llenamos la información necesaria para crear la DB. Importante, como es una práctica se selecciona free tier.

    El update en la sección de Maintenance se deshabilita, pues podría ocurrir que una actualización tumbe toda la DB.
![RDS Creation](/images/rds-creation.png)
4. Clic en Create database.

## Haciendo una migración a RDS PG

Recuerda que puedes tomar el [Curso de PostgreSQL](https://platzi.com/cursos/postgresql) y también el [Curso de Introducción a Terminal y Línea de Comandos](https://platzi.com/cursos/terminal/) en [Platzi](https://platzi.com).

Seguimos los siguientes pasos conectados al servicio de EC2 creado en el principio del curso:
1. Como superusuario instalamos la misma versión de postgres que creamos en la DB.
```bash
yum install postgresql-server
```
2. en el repositorio [master](/code/aws-platzi-python-master) existe un archivo que se llama [sample-uk-zipcodes.sql](/code/aws-platzi-python-master/sample-uk-zipcodes.sql). Vamos a montarlo a la DB.

    Usamos el siguiente comando para descargarlo a la DB.
    ```bash
    wget https://raw.githubusercontent.com/mauropm/aws-platzi-python/master/sample-uk-zipcodes.sql
    ```
3. Nos conectamos a la DB usando:
```bash
psql -h platzidb.cs996twzbtux.us-east-1.rds.amazonaws.com -U postgres

# En la consola de postgres
CREATE DATABASE platzidb;

# salimos de la consola
\q

# Ejecutamos el comando para cargar la DB
psql -h platzidb.cs996twzbtux.us-east-1.rds.amazonaws.com -U postgres platzidb < sample-uk-zipcodes.sql
```
4. Ingresamos a la DB
```bash
psql -h platzidb.cs996twzbtux.us-east-1.rds.amazonaws.com -U postgres platzidb
```
5. Verificamos las tablas creadas en la DB.
```bash
\dt
               Listado de relaciones
 Esquema |        Nombre        | Tipo  |  Dueño   
---------+----------------------+-------+----------
 public  | ccgs                 | tabla | postgres
 public  | constituencies       | tabla | postgres
 public  | counties             | tabla | postgres
 public  | districts            | tabla | postgres
 public  | nuts                 | tabla | postgres
 public  | outcodes             | tabla | postgres
 public  | parishes             | tabla | postgres
 public  | places               | tabla | postgres
 public  | places_archived      | tabla | postgres
 public  | postcodes            | tabla | postgres
 public  | spatial_ref_sys      | tabla | rdsadmin
 public  | terminated_postcodes | tabla | postgres
 public  | wards                | tabla | postgres
(13 filas)
```

## Conociendo Aurora PG (Postgress)

Aurora PG es una nueva propuesta en bases de datos, AWS toma el motor de Postgres, instancias de nueva generación, optimizaciones varias en el kernel/código y obtiene un Postgres 3x más rápido.

Aurora PG es compatible con Postgres 9.6.x.

Antes de migrar a Aurora PG debes considerar los siguientes puntos:

* Usar Aurora RDS PG no es gratis en ningún momento.
* AWS RDS PG es eficiente por varias razones:
    * Modificaciones al código mismo del motos de bases de datos.
    * Instancias de última generación.
* Aurora PG estará por omisión en una configuración de alta disponibilidad con distintas zonas, es decir, en 3 centros de datos a un mismo tiempo.

La implementación de RDS Aurora PG y la de RDS PG es muy diferente en términos internos, pero a nivel de usuario, es la misma experiencia.

En el caso de RDS Aurora PG, lo que hace AWS es modificar el código de PostgreSQL sin romper compatibilidad, con el fin de optimizar las instancias en donde va a estar viviendo la base de datos de PostgreSQL, también modificando a qué discos duros provee estas instancias logra que RDS Aurora PG sea tres veces más rápido que RDS PG.

**Nota**: PostgreSQL es una de los motores de bases de datos más utilizados empresarialmente que sea software libre, y es por esta razón que se han estado haciendo tanta modificaciones. PostgreSQL normalmente es mucho más rápido y más estable que por ejemplo MySQL. MySQL es un buen motor de bases de datos, sin embargo, es utilizado para otro tipo de proyectos con menos calidad de trabajo, etc.

## Haciendo una migración a Aurora DB

Amazon Aurora no se encuentra dentro de la capa gratuita, así que para efectos del aprendizaje, veremos cómo se crea y el procedimiento de cómo configurar y migrarla será con la pantalla del instructor.

1. Creamos la DB de aurora.
![Aurora creation](/images/aurora-creation.png)
2. El dashboard nos indica cuándo la DB está lista y disponible para su uso.
![Dashboard](/images/aurora-dbs.png)
3. ingresamos a la instancia de EC2 y ejecutamos el siguiente comando.
```bash
psql -h platzi-aurora-instance-1.cs996twzbtux.us-east-1.rds.amazonaws.com -U postgres platzidb2

\dt
No se encontraron relaciones.
```
4. salimos de la DB, y ahora importamos la DB.
```bash
psql -h platzi-aurora-instance-1.cs996twzbtux.us-east-1.rds.amazonaws.com -U postgres platzidb2 < sample-uk-zipcodes.sql
Contraseña para usuario postgres: 
SET
SET
SET
SET
SET
 set_config 
------------
 
(1 fila)

SET
SET
SET
CREATE EXTENSION
ERROR:  must be owner of extension plpgsql
CREATE EXTENSION
ERROR:  must be owner of extension postgis
CREATE EXTENSION
ERROR:  must be owner of extension unaccent
SET
SET
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE SEQUENCE
ALTER SEQUENCE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE SEQUENCE
ALTER SEQUENCE
CREATE SEQUENCE
ALTER SEQUENCE
CREATE TABLE
CREATE SEQUENCE
ALTER SEQUENCE
CREATE TABLE
CREATE SEQUENCE
ALTER SEQUENCE
CREATE TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX

psql -h platzi-aurora-instance-1.cs996twzbtux.us-east-1.rds.amazonaws.com -U postgres platzidb2
Contraseña para usuario postgres: 
psql (9.2.24, servidor 11.7)
ADVERTENCIA: psql versión 9.2, servidor versión 11.0.
          Algunas características de psql pueden no funcionar.
conexión SSL (cifrado: ECDHE-RSA-AES256-GCM-SHA384, bits: 256)
Digite «help» para obtener ayuda.

platzidb2=> \dt
               Listado de relaciones
 Esquema |        Nombre        | Tipo  |  Dueño   
---------+----------------------+-------+----------
 public  | ccgs                 | tabla | postgres
 public  | constituencies       | tabla | postgres
 public  | counties             | tabla | postgres
 public  | districts            | tabla | postgres
 public  | nuts                 | tabla | postgres
 public  | outcodes             | tabla | postgres
 public  | parishes             | tabla | postgres
 public  | places               | tabla | postgres
 public  | places_archived      | tabla | postgres
 public  | postcodes            | tabla | postgres
 public  | spatial_ref_sys      | tabla | rdsadmin
 public  | terminated_postcodes | tabla | postgres
 public  | wards                | tabla | postgres
(13 filas)
```
En terminos de interfaz de usuario no hay diferencia entre la DB postgres que se creo previamente y Aurora PG. Entonces podemos hacer el salto entre DB si postgres se queda corto y tener 3 veces más velocidad, 3 veces más redundancia con diferentes servidores, y si alguna eventualidad sucede en algún data center, el servicio va a perdurar sin hacer modificaciones al código o forma de trabajo, pues en terminos de motor de postgres es exactamente el mismo.

## Mejores prácticas de Bases de Datos y RDS

* **Respaldos diarios**.
    
    Por omisión puedes tener respaldos automatizados.
* **Replicar la base de datos**.

    Es fácil poder replicar la información de tu base de datos en un data center distinto de Amazon.

# Redes 

## Route53

Existen muchos servicios de redes en AWS, uno de los más interesantes es Route 53.

AWS te permite tener un DNS muy avanzado a tu disposición, con el podrás hacer subdominios asignados a instancias y verlos reflejados en segundos.

Route 53 está disponible en todas las regiones de AWS, por lo que funcionará excelente aún en caso de que alguna de las regiones se pierda.

Para poder ejecutar esta instancia nos dirigimos a la consola y corremos '*Route 53*'.

![Route 53](/images/route53.png)

Podemos crear un dominio y comprarlo con facilidad en AWS, así mismo, Amazon te indica si el dominio está disponible y te muestra otras sugerencias, así como el precio por un año.

![Dominio](/images/domain-r53.png)

Los siguientes pasos serán capturas de pantalla del curso.

Una vez comprado el dominio podemos ver diferentes opciones, como el listado del name server asociado. También un Record Set para hacer el dominio más agradable.

![Name server](/images/r53-datos.png)

# Herramientas de administración

## Herramientas de administración - IAM

Existen muchas herramientas de administración en AWS muy útiles, las siguientes tres son las más importantes:

* **IAM** te permite administrar todos los permisos de acceso de usuarios y máquinas sobre máquinas.
* **CloudWatch** te mostrará diversos eventos relacionados con tu infraestructura o servidores, para tener un lugar centralizado de logs e información.
* **Cloudtrail** es una herramienta de auditoria que permite ver quién o qué hizo que actividad en tu cuenta de AWS.

Cada uno de los productos de AWS tienen diversas alternativas para acceder a más logs, estas opciones cuentan con almacenamiento histórico y hacen un gran trabajo al tratar la información para auditar actividades y deshabilitar usuario.

## Utilizando IAM

* AWS Identity and Access Management (IAM) le permite administrar el acceso a los servicios y recursos de AWS de manera segura. Con IAM, puede crear y administrar usuarios y grupos de AWS, así como utilizar permisos para conceder o denegar el acceso de estos a los recursos de AWS.
* Existen
    * Usuarios
    * Grupos: agrupaciones de usuarios.
    * Roles: Similar a un usuario solo que no puede hacer lo mismo, es solamente una identidad que tiene una serie de permisos a ser utilizada desde un programa.
    * Políticas: En estas se especifican los permisos.
        * Amazon Resource Name (ARN)
        * arn:aws:service:region:account:resource
* Se definen los permisos explícitos de acceso a ciertos servicios.

Para utilizar este servicio nos dirigimos a la página principal de la consola de aws, nos dirigimos al apartado de '*Security, Identity, & Compliance*', y le damos clic a *IAM*.
![IAM Dashboard](/images/iam-dashboard.png)

En el dashboard podemos ver usuarios, grupos, roles, etc. Le damos clic a usuarios para crear uno.

![Users](/images/add-users.png)

Le damos clic a '*add user*' y llenamos la información.
![Details](/images/user-details.png)

Habilitamos permisos, creamos un grupo cuyos permisos sean los de S3, que puedan escribir.
![permisos](/images/s3-permisos.png)

![Grupos](/images/s3-grupos.png)

Se añaden etiquetas, si se desea, es totalmente opcional.

Se verifica la información.
![Review](/images/iam-review.png)

Una vez verificada la información se da clic a crear usuario.

Nos muestra una opción que los usuarios pueden iniciar sesión en una url específica. `https://044968212970.signin.aws.amazon.com/console`.

![Success](/images/user-success.png)
```bash
Access Key: AKIAQU6CQPHVBYQZNGKP

Secret Access Key: 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
```

Para iniciar sesión necesitamos de software especializado, en el curso muestra el software [Cyberduck](https://duck.sh/).

Personalmente, creo que es mejor Filezilla, aunque estoy probando uno que parece ser más atractivo, [sFTP Client](https://www.sftpapp.com/), utilicé [snapcraft](https://snapcraft.io/sftpclient) para instalarlo. Visualmente, es hermoso, pero cuesta $25USD... Quizás en un futuro.

## CloudWatch

[¿Qué es Amazon CloudWatch Logs?](https://docs.aws.amazon.com/es_es/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)

## CloudTrail

Herramienta que te permite saber qué o quién hizo alguna actividad dentro de tu cuenta de AWS.

[AWS CloudTrail Documentation](https://docs.aws.amazon.com/cloudtrail/index.html)

# Seguridad

Es muy importante aclarar que los certificados que genera ACM (AWS Certificate Manager) son gratuitos solo bajo ciertas condiciones. NO es cierto que son gratuitos.

## Certificate manager

Certificate Manager: AWS te permite crear nuevos certificados cuando necesites (o importar alguno que ya tengas) y te sera fácil usarlos en balanceadores de cargas.


Con AWS Certificate Manager, no se aplican cargos adicionales por el aprovisionamiento de los certificados SSL/TLS públicos o privados que utiliza con los servicios integrados con ACM, como Elastic Load Balancing y API Gateway.

Y cuales son estos servicios integrados:
* Elastic Load Balancing
* Amazon CloudFront
* AWS Elastic Beanstalk
* Amazon API Gateway
* AWS CloudFormation

Si el certificado no se le asocia a alguno de esos servicios, entonces el certificado tiene costo.

## GuardDuty

GuardDuty: AWS permite que hagas una auditoria constante de todos los intentos de conexiones que tienen tus equipos de computo.

Amazon GuardDuty es un servicio de monitorización continua de la seguridad que analiza y procesa los siguientes orígenes de datos: logs de flujo de VPC, logs de eventos de AWS CloudTrail y logs de DNS. Utiliza fuentes de información de amenazas, como listas de direcciones IP y dominios maliciosos, y aprendizaje automático para identificar la actividad inesperada y potencialmente no permitida, así como la actividad malintencionada en su entorno de AWS. Esto puede incluir problemas como escalado de privilegios, uso de credenciales expuestas o la comunicación con direcciones IP, URL o dominios malintencionados.

En guardduty también se pueden generar resultados de muestra, para ello se selecciona settings o configuración dependiendo del idioma usado y se da click en el botón generar resultados de muestra.

# Bonus

## AWS Rekognition

AWS Rekognition facilita la adición de análisis de imagen y video a sus aplicaciones con tecnología probada, altamente escalable y de aprendizaje profundo que no requiere experiencia en aprendizaje automático para su uso. Con Amazon Rekognition puede identificar objectos, personas, texto, escenas y actividades en imágenes y videos, además de detectar cualquier contenido inapropiado.

**Precios de Amazon Rekognition Image**

Con Amazon Rekognition Image, hay dos tipos de costos.

Amazon Rekognition Image cobra cada vez que analiza una imagen con nuestras API. Ejecutar múltiples API contra una única imagen cuenta como procesamiento múltiple de imágenes.

Almacenamiento de metadatos de rostros: Para habilitar la búsqueda de rostros, deberá almacenar un repositorio de metadatos de rostros en el que Amazon Rekognition pueda buscar coincidencias. Los cargos de almacenamiento se aplican mensualmente y se prorratean en el caso de meses parciales.

**Capa gratuita**

Como parte de la capa gratuita de AWS, puede comenzar a utilizar Amazon Rekognition Image de manera gratuita. La capa gratuita dura 12 meses y permite que analice 5000 imágenes por mes y almacena 1000 piezas de metadatos de rostros por mes.

## Creando nuestro servicio de Postgres

Esta es una clase actualizada de cómo crear una DB en postgres. No hay mucha diferencia de cómo lo realicé en el curso.

## Accediendo a nuestra base de datos Postgres

En esta clase se conecta con PGAdmin3. Yo ya he podido conectar la DB de amazon a PGAdmin4.
