# ¿Qué es MongoDB Sharding y las mejores prácticas?

## Necesidad
En el momento que tenemos nuestra base de datos en producción, se empiezan a generar más trafico de datos y el almacenamiento se llena. Por eso llega un momento donde nuestro cluster no rinde adecuadamente, ya sea por CPU, RAM o Disco Duro.

##  Solución
La solución más usada en MongoDB es el escalamiento horizontal de las bases de datos o fragmentación (sharding en inglés). Esto nos permite agregar nuevos clusters, es decir más máquinas, en nuestro ecosistema de modo que podemos hacer crecer nuestra capacidad de procesado y almacenamiento. Esto resulta más efectivo que el escalamiento vertical, que se basaria en aumentar la capacidad del hardware de esa única máquina. Aún así, actualmente, los mejores servidores en la actualidad no tienen más de 256 GB de RAM o 16 TB de disco duro, por lo que el escalamiento vertical es una opción limitada por hardware.

## Principios de fragmentación
Al fragmentar, la base de datos se “divide” en fragmentos separados que residen en diferentes máquinas. Un ejemplo simple podría ser: suponga que una empresa tiene máquinas que pueden almacenar hasta 2 millones de elementos de datos de clientes. Ahora, el negocio está llegando a ese punto de quiebre y probablemente superará los 2,5 millones de usuarios pronto. Entonces, deciden dividir su base de datos en dos, de modo que doblan su capacidad sin necesidad de aumentar la de la maquina.

![Fragmentacion de bases de datos](https://geekflare.com/wp-content/uploads/2018/11/simple-sharding.png)


## Problemas durante la fragmentación
### Llaves primarias y externas
Al dividir la base de datos en dos o más, las llaves primarias dejan de tener sentido. Sobre todo si se han configurado un autoincremento.
Es entonces cuando la misma llave primaria puede dar diferentes resultados dependiendo a que base de datos se consulta.
MongoDB no soporta llaves externas, por lo que no sirven como solución al problema de las llaves primarias.

### Errores de datos externos y transferencias entre clusters
Es posible que usemos datos del cluster A y del B simultaneamente. En el caso de que uno de ellos se encuentre fuera de servicio, se generaría un error que detendría la consulta.
También pueden darse errores debido a consultas + actualizaciones simultaneas de las bases de datos entre diferentes clusters. De modo que pueden producirse pérdidas de información o corrupccion de los datos. Por ejemplo, durante la transferencia de dinero entre las cuentas de varios clientes que pertenecen a diferentes clústers.

## Gestión automatica de fragmentaciones
La mejor parte de la fragmentación de MongoDB es que incluso el equilibrio de fragmentos es automático. Es decir, si tiene cinco fragmentos y dos de ellos están casi vacíos, puede decirle a MongoDB que reequilibre las cosas de manera que todos los fragmentos estén igualmente llenos.

Como desarrollador o administrador, no necesita preocuparse mucho, ya que MongoDB entre bastidores hace la mayor parte del trabajo pesado. Lo mismo ocurre con la falla parcial de los nodos. Si tiene conjuntos de réplicas configurados correctamente y ejecutándose en su clúster, las interrupciones parciales no afectarán el tiempo de actividad del sistema.

Un esquema ejemplo de una app sería el siguiente:
![Ejemplo de app con mongoDB](https://geekflare.com/wp-content/uploads/2018/11/mongodb-sharded-cluster.png)

## Buenas practicas

### Llaves de fragmentación con alta cardinalidad
A la hora de decidir si un dato entrante se almacena en un cluster u otro, podemos asignar un criterio de elección (llave de fragmentación).
Por ejemplo, dividir los datos según la inicial de el nombre de pila del usuario. A veces esto no termina de funcionar del todo bien, porque no podemos asegurar que la distribución de iniciales sea uniforme; de modo que puede que uno de los clusters se llene mas que otro.
![Llaves fragmentacion](https://geekflare.com/wp-content/uploads/2018/11/naive-sharding.png)

Una buena practica es usar **llaves de fragmentación de alta cardinalidad** que permitan una distribución uniforme de los datos.
* Email
* Mes de nacimiento
* Llave compuesta (combinación de varios campos mediante operaciones)


### Cambiando monótonamente

Un error común en la fragmentación de MongoDB es utilizar claves de aumento monotónico (aumento incremental automático) como clave de fragmentación.

Generalmente, se utiliza la clave principal del documento. La idea aquí es bien intencionada, es decir, a medida que se sigan creando nuevos documentos, caerán uniformemente en uno de los fragmentos disponibles. Desafortunadamente, tal configuración es un error clásico. Esto es así porque si la clave del fragmento siempre aumenta, después de un punto, los datos comenzarán a acumularse en el lado de alto valor de los fragmentos, lo que provocará un desequilibrio en el sistema.

![Error de acumulación] (https://geekflare.com/wp-content/uploads/2018/11/shard-keys-increasing-540x270.png)

La solución es optar por un esquema de clave de fragmentación con hash, que crea una clave de fragmentación mediante el hash de uno de los campos proporcionados y usándolo para determinar el fragmento.

![Hasheado de llaves](https://geekflare.com/wp-content/uploads/2018/11/harshed-sharding.png)

Una clave de fragmento hash se ve así:
```
 {
    "_id": "6b85117af532da651cc912cd"
}
```
Se puede crear en el shell del cliente de Mongo usando:
```
 db.collection.createIndex ({_id: hashedValue})
```

### Fragmento temprano
Uno de los consejos más útiles directamente desde las trincheras es fragmentar temprano, incluso si termina con un grupo pequeño de dos partes. Una vez que los datos han superado los 500 GB o algo así, la fragmentación se convierte en un proceso complicado en MongoDB.

### Cuándo ejecutar equilibradores
Otra buena idea es monitorear sus patrones de tráfico y ejecutar el equilibrador fragmento sólo en momentos de poco tráfico. El reequilibrio en sí toma un ancho de banda considerable. Conviene activar el equilibrador en momentos de poco tráfico.  He aquí cómo usted puede lograr esto (suponiendo que tiene poco tráfico 03 a.m.-05 a.m.):
```
 uso config 
db.settings.update ( 
   {_ID: "equilibrador"}, 
   {$ Conjunto: {ActiveWindow: {start: "03:00", parada: "05:00"}}}, 
   {Upsert: true} 
)```

