# MongoDB
Curso de mongodb de platzi.

## Base de datos no relacionales (NoSQL)

Las bases de datos NoSQL tienen 4 grandes familias: Key Value Stores, basadas en grafos, columnares y basadas en documentos.

* **Key Value Stores**: Guardan la información en formato de llaves y valores. Las usamos para guardar cache, información de sesión de los usuarios o cosas muy sencillas. Son muy rápidas de consultar pero no podemos usarlas en casos más complejos donde necesitamos estructuras más especiales. El mejor ejemplo de estas bases de datos es Redis.

* **Graph Databases**: Bases de datos basadas en Grafos. Nos permiten establecer conexiones entre nuestras entidades para realizar consultas de una forma más eficiente que en bases de datos relacionales (así como Twitter o Medium donde cada publicación tiene diferentes relaciones entre sus usuarios, likes, etc). Por ejemplo: Neo4j o JanusGraph.

* **Wide-column** Stores: Bases de datos columnares. Tienen una llave de fila y otra de columnas para hacer consultas muy rápidas y guardar grandes cantidades de información pero modelar los datos se puede volver un poco complicado. Las usamos en Big Data, IoT, sistemas de recomendaciones, entre otras. Por ejemplo: Cassandra o HBase.

* **Document Databases**: Bases de datos basadas en documentos. Nos permiten guardar documentos dentro de colecciones, tiene muy buena performance y flexibilidad que nos permite modelar casos de la vida real de forma sencilla y efectiva. Por ejemplo: MongoDB o CouchBase.

## Funcionamiento de MongoDB
### Base de datos:
* Contenedor físico de colecciones.
* Cada base de datos tiene su archivo propio en el sistema de archivos.
* Un cluster puede tener múltiples bases de datos.

### Colecciones:
* Agrupación de documentos.
* Equivalente a una tabla en las bases de datos relacionales.
* No impone un esquema, por lo que los documentos pueden tener diferentes campos.

### Documentos:
* Un registro dentro de una colección.
* Es análogo a un objeto JSON (BSON).Es su codificación en binario y admite otros datos como fechas.
* La unidad básica dentro de MongoDB.
* Se identifican por un campo oculto ```_id: 123456789``` que es obligatorio y único. Si no se introduce en la creación del documento, se asigna automaticamente.
* Máximo de 16MB.

![comparacion entre conceptos SQL y MongoDB](https://i.pinimg.com/originals/b2/17/79/b21779c78f9474ae2adf947ac6cca20d.png)

Ejemplo de un documento en formato JSON.
```
{   _id:"123456789", 
    item: "canvas",
    qty: 100, 
    tags: ["cotton"], 
    size: { 
        h: 28, 
        w: 35.5, 
        uom: "cm"
        } 
}
````

### Tipos de datos:

#### Strings
Nos sirven para guardar textos.

#### Boolean
Información cierta o falsa (true y false).

#### ObjectId: 
Utilizan el tiempo exacto en el que generamos la consulta para siempre generan IDs únicos. Existen en BSON pero no en JSON.

#### Date 
Nos sirven para guardar fechas y hacer operaciones de rangos entre ellas.

#### Números
Doubles, Integers, Integers 64 bits y Decimals.

#### Documentos Embebidos
Documentos dentro de otros documentos ({}).

#### Arrays []
Arreglos o listas de cualquier otro tipo de datos, incluso, de otras listas.

Más tipos en https://docs.mongodb.com/manual/reference/bson-types/

### Esquemas y relaciones:
Los **esquemas** son la forma en que organizamos nuestros documentos en nuestras colecciones. MongoDB no impone ningún esquema pero podemos seguir buenas prácticas y estructurar nuestros documentos de forma parecida (no igual) para aprovechar la flexibilidad y escalabilidad de la base de datos sin aumentar la complejidad de nuestras aplicaciones.

Las **relaciones** son la forma en que nuestras entidades o documentos sen encuentran enlazados unos con otros. Por ejemplo: Una carrera tiene multiples cursos y cada curso tiene multiples clases.

#### Relaciones 1 a 1
Los **documentos embebidos** nos ayudan a guardar la información en un solo documento y nos ahorra el tiempo que tardamos en consultar diferentes documentos a partir de referencias a colecciones separadas.

```
Colección: inventario

{   _id:"123456789", 
    item: "canvas",
    qty: 100, 
    tags: ["cotton"], 
    size: { 
        h: 28, 
        w: 35.5, 
        uom: "cm"
        } 
}

```

#### Relaciones 1 a muchos
**Documentos embebidos** cuando la información no va a cambiar muy frecuentemente y **referencias** cuando si. 

```
Colección: inventario
{   _id:123456789, 
    item: "canvas",
    tags: ["cotton"], 
    size: { 
        h: 28, 
        w: 35.5, 
        uom: "cm"
        } 
}


Colección: stock
{
    _id:00000001,
    inventory_id: 123456789
    quantity: 100
}
```


#### Tipos de esquemas
La arquitectura de la base de datos supone la principal decisión del desarrollo. Tenemos que tener en cuenta varios puntos antes de empezar a realizar el código:

* Qué datos serán consultados con mayor y menor frecuencia. (_El nombre de un articulo se muestra mas frecuentemente que su proveedor._)

* Qué datps serám actualizados con mayor y menor fecuencia. (_El stock de un articulo se actualiza mas frecuentemente que su marca._)

* Que tipo de consultas serán las más y menos frecuentes (y cuál será su coste de procesamiento). (_Se más frecuentemente antes las listas de varios articulos que modificar detalles individuales de uno de ellos. La lista deberia tener una mayor optimización._)


* Por dónde se expande la BD a medida que escala y si llegara al tamaño maximo de 16MB por documento.
(_Los almacenes o contenedores tienen una capacidad de articulos limitada. Pero a medida que se escala se pueden ir añadiendo (lenamente) almacenes con nuevos articulos. El numero de articulos crece mucho más rápido que el de almacenes o contenedores._)

* Que tipo de nuevos datos se prevee incluir a medida que se añaden funciones. (_Podemos requerir de una colección de "usuarios" para acceder al sistema (con contraseña,nombre,apellidos,telefono,email...)._)


##### Modo MongoDB con Documentos Embebidos
Fácil de implementar y acceso a todos los datos de golpe. A medida que crezca la BD los documentos serán más pesados. Esto dificulta actualizar datos de manera frecuente como el stock.
```
{
    "_id": "ALM0201",
    "ubicación": "Calle Ejemplo 23",
    "responsable": "Cristina Aguado",
    "telefono": "999888777",
    "contenedores":[
        {
        "_id": "CNT05123",
                "tamaño":"40ft",
                "color": "verde",
                "articulos": [
                    {
                    "_id": "ART661234",
                    "nombre": "Laptop",
                    "marca":"superPC",
                    "proveedor":"UAMZ Inc",
                    "peligroso": false,
                    "stock": 240
                    },                
                    {
                    "_id": "ART903452",
                    "nombre": "BateríaLaptop",
                    "marca":"superPC",
                    "proveedor":"UAMZ Inc",
                    "peligroso": true,
                    "stock": 350
                    }

                ]
                    
        },
        {
            "_id": "CNT02012",
                    "tamaño":"20ft",
                    "color": "rojo",
                    "articulos": [                                      
                        {
                        "_id": "ART523642",
                        "nombre": "Cable HDMI",
                        "marca":"superCable",
                        "proveedor":"ExIo SL",
                        "peligroso": false,
                        "stock": 1032
                        }    
                    ]
        }
    ]   
},
{
    "_id": "ALM0111",
    "ubicación": "Calle Recuerdo 12",
    "responsable": "Pepe Villuela",
    "telefono": "666111666",
    "contenedores":[]
}
```


##### Modo “SQL” con Referencias
Las consultas directas por id son muy eficientes. Si se quieren mostrar conjuntos de documentos (como una lista de articulos con su stock) se deben realizar uniones que aumentan el costo de procesado.
```
//colección: almacenes
{
    "_id": "ALM0201",
    "ubicación": "Calle Ejemplo 23",
    "responsable": "Cristina Aguado",
    "telefono": "999888777",
    "contenedores":["CNT05123","CNT02012"]
},
{
    "_id": "ALM0111",
    "ubicación": "Calle Recuerdo 12",
    "responsable": "Pepe Villuela",
    "telefono": "666111666",
    "contenedores":[]
}

// colección: contenedores
{
    "_id": "CNT05123",
    "tamaño":"40ft",
    "color": "verde",
    "articulos": ["ART661234","ART903452"]
},
{
    "_id": "CNT02012",
    "tamaño":"20ft",
    "color": "rojo",
    "articulos": ["ART523642"]
},

//colección: artículos
{
    "_id": "ART661234",
    "nombre": "Laptop",
    "marca":"superPC",
    "proveedor":"UAMZ Inc",
    "peligroso": false,
    "stock": 240
},                
{
    "_id": "ART903452",
    "nombre": "BateríaLaptop",
    "marca":"superPC",
    "proveedor":"UAMZ Inc",
    "peligroso": true,
    "stock": 350
},
{
    "_id": "ART523642",
    "nombre": "Cable HDMI",
    "marca":"superCable",
    "proveedor":"ExIo SL",
    "peligroso": false,
    "stock": 1032
}
```

##### Combinación de documento embedido y referencias:
Mejor opción si tenemos datos con consulta (nombre) update frecuente (stock), y datos con consulta puntual (marca, proveedor…). Nos quiamos todo el costo de cargar los detalles cuando no son necesarios.
```
//colección: almacenes
{
    "_id": "ALM0201",
    "ubicación": "Calle Ejemplo 23",
    "responsable": "Cristina Aguado",
    "telefono": "999888777",
    "contenedores":[
        {
        "_id": "CNT05123",
                "tamaño":"40ft",
                "color": "verde",
                "articulos": [
                    {
                    "_id": "ART661234",
                    "nombre": "Laptop",
                    "stock": 240
                    },                
                    {
                    "_id": "ART903452",
                    "nombre": "BateríaLaptop",
                    "stock": 350
                    }

                ]
                    
        },
        {
            "_id": "CNT02012",
                    "tamaño":"20ft",
                    "color": "rojo",
                    "articulos": [                                      
                        {
                        "_id": "ART523642",
                        "nombre": "Cable HDMI",
                        "stock": 1032
                        }    
                    ]
        }
    ]   
},
{
    "_id": "ALM0111",
    "ubicación": "Calle Recuerdo 12",
    "responsable": "Pepe Villuela",
    "telefono": "666111666",
    "contenedores":[]
}

//colección: artículos
{
    "_id": "ART661234",
    "nombre": "Laptop",
    "marca":"superPC",
    "proveedor":"UAMZ Inc",
    "peligroso": false,
},                
{
    "_id": "ART903452",
    "nombre": "BateríaLaptop",
    "marca":"superPC",
    "proveedor":"UAMZ Inc",
    "peligroso": true,
},
{
    "_id": "ART523642",
    "nombre": "Cable HDMI",
    "marca":"superCable",
    "proveedor":"ExIo SL",
    "peligroso": false,
}
```


## Ecosistema de MongoDB
MongoDB es una base de datos gratis y de código abierto No Relacional basada en documentos que nos permite guardar una gran cantidad de documentos de forma distribuida. Mongo también es el nombre de la compañía que desarrolla el código de esta base de datos.

Una de sus principales características es que nos permite guardar nuestras estructuras o documentos en formato **JSON** (no exactamente JSON, pero si algo muy parecido, lo veremos más adelante) para tener una gran flexibilidad a la hora de modelar situaciones de la vida real.

Por ser una base de datos distribuida podemos hablar no de uno sino de varios servidores, lo que conocemos como el Cluster de MongoDB. Gracias a esto obtenemos una gran escalabilidad de forma horizontal (escalabilidad en cantidad de servidores).

![Escalabilidad vertical de servidores](https://www.oscarblancarteblog.com/wp-content/uploads/2017/03/escalamiento-vertical.png)
![Escalabilidad horizontal de servidores](https://www.oscarblancarteblog.com/wp-content/uploads/2017/03/escalamiento-horizontal.png)

MongoDB es **“Schema Less”** lo que permite que nuestros documentos tengan estructuras diferentes sin afectar su funcionamiento, algo que no podemos hacer con las tablas de las bases de datos relacionales. Su lenguaje para realizar queries, índices y agregaciones es muy expresivo.

## MongoDB Atlas (cloud)
Tenemos varios proveedores que nos permiten utilizar o alquilar MongoDB como servicio y en este caso vamos a usar MongoDB Atlas por ser desarrollado por las mismas personas que desarrollan MongoDB.
https://www.mongodb.com/cloud/atlas

MongoDB Atlas tiene las siguientes características:
* Aprovisionamiento automático de clusters con MongoDB
* Alta disponibilidad
* Altamente escalable
* Seguro
* Disponible en AWS, GCP y Microsoft Azure
* Fácil monitoreo y optimización

## Divers de MongoDB para otros lenguajes
Los drivers las librerías que utilizamos para comunicar nuestra aplicación con nuestra base de datos.
Sin nuestros drivers no podemos trabajar con nuestros cluster de base de datos.
Para agregallos, usamos un gestor de dependencias. 
* Python: 
```bash 
python -m pip install pymongo
```
* Node.js: 
```bash 
npm install mongodb --save
```
* Ruby: 
```bash 
gem install mongoid
```
* GO: 
```bash 
dep ensure -add go.mongodb.org/mongo-driver/mongo
```

# Recomendaciones de arquitectura de BD en MongoDB

* Usar proveedores cloud con alta disponibilidad: AWS, Google Cloud o Azure son muy buenas opciones.
* No te compliques pensando en administración de servidores con MongoDB, servicios como MongoDB Atlas o mlab son muy buenas opciones.
* Guardar las credenciales en variables de entorno (```export VARIABLE = valor```) o archivos de configuración fuera del proyecto.
* Asegura que tu cluster se encuentra en la misma región del proveedor que tu aplicación.
* Haz VPC peering entre la VPC de tu aplicación y la VPC de tu cluster.
* Cuida la lista de IPs blancas.
* Puedes habilitar la autenticación en dos pasos.
* Actualiza constantemente tu versión de MongoDB.
* Separa los ambientes de desarrollo, test y producción.
* Habilita la opción de almacenamiento encriptado.

**Lecturas recomendadas:**
* 14 Things I Wish I’d Known When Starting with MongoDB 
https://www.infoq.com/articles/Starting-With-MongoDB/
* Time Series Data and MongoDB: Part 2 – Schema Design Best Practices
https://www.mongodb.com/blog/post/time-series-data-and-mongodb-part-2-schema-design-best-practices

* Performance Best Practices: MongoDB Data Modeling and Memory Sizing
https://www.mongodb.com/blog/post/performance-best-practices-mongodb-data-modeling-and-memory-sizing

* What is MongoDB Sharding and the Best Practices?
https://geekflare.com/mongodb-sharding-best-practices/


# Instalación y ejecución
## Instalación en macOS
Para realizar la instalación directamente desde bash es necesario tener instalado el paquete brew. 
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

NOTA: en este caso se usa la versión de mongodb comunity 4.4. La versión se indica tras el símbolo @, de modo que se puede usar otra versió modificando este valor.

```bash
brew tap mongodb/brew
brew install mongodb-community@4.4

```
## Ejecución en macOS

Puede ejecutar MongoDB como un servicio de macOS usando brew, o puede ejecutar MongoDB manualmente como un proceso en segundo plano. Se recomienda ejecutar MongoDB como un servicio macOS, ya que al hacerlo se configuran los valores ulimit correctos del sistema automáticamente (consulte la configuración ulimit para obtener más información).

Para ejecutar MongoDB (es decir, el proceso mongod) como un servicio macOS, emita lo siguiente:
```bash
brew services start mongodb-community@4.4
```

Para detener la ejecución de un mongod como servicio macOS, utilice el siguiente comando según sea necesario:

```bash
brew services stop mongodb-community@4.4
```

Para ejecutar MongoDB (es decir, el proceso mongod) manualmente como un proceso en segundo plano, emita lo siguiente:

```bash
mongod --config /usr/local/etc/mongod.conf --fork
```

Para inicializar el shell de MongoDB, emita lo siguiente:
```bash
mongod
```

## Configuración de un cluster en MongoDB Atlas
1. Iniciar sesión en Atlas.
2. Crear nuevo cluster (Build a Cluster).
    1. Seleccionar proveedor y region más próxima a los usuarios.
    2. Escojer el tipo de máquiuna (tier) en función de las necesidades.
    3. Escojer la version de Atlas.
    4. Nombrar el cluster.
    5. Esperar a que se despliegue el cluster (varios minutos).
3. En la pestaña Security, click en Añadir Nuevo Usuario.
    1. Nombre y contraseña seguros (guardar credenciales).
    2. Permisos de usuario (admin/lectura/escritura).
4. En la pestaña Security, click en Añadir IP en WhiteList.
    1. Escribir la ip desde la que nos conectamos para que permita la conecxión.
5. Click en Connect.
    1. Click en Connect via Mongo Shell.
    2. Verificar que Mongo Shell está instalado.
    3. Usar el comando: ```mongo "mongodb+srv://cluster0.wujbs.mongodb.net/<nombredelabasedatos>" --username <nombredelusuarioadmin>```.
    4. Autentificarse con la contraseña del usuario.
    
## Interfaz gráfica MongoDB Compass
  1. Instalar MongoDB Compass desde https://www.mongodb.com/download-center/compass
  2. Crear nueva conexión.
      1. Introducir la url de la base de datos.
      2. Activar SRV record (conexion segura).
      3. Autenticarse con el usuario creado en Atlas.
  
# Creando una base de datos
## Comandos básicos de MongoDB
* Conexión con el cluster de MongoDB Atlas (recuerda añadir tu IP a la lista de IPs permitidas): ```mongo "URL DE NUESTRO CLUSTER",```
* Mostrar las bases de datos exitentes:```show dbs```
* Mostra la base de datos en la nos encontramos: ```db```
* Usar una nueva base de datos (o crearla si no existe):  ```use basedatos-db```
* Listar todos los posibles comandos que podemos ejecutar: ```db.NOMBRE_COLECCIÓN.help()```

## Operaciones CRUD (Create, Read, Update, Delete)
**Version de MongoDB: 4.4**
Para más información sobre otras versiones: https://docs.mongodb.com/manual/crud/


### Crear (insert)
Las operaciones de creación o inserción agregan nuevos documentos a una colección. Si la colección no existe actualmente, las operaciones de inserción crearán la colección.

MongoDB proporciona los siguientes métodos para insertar documentos en una colección:
```
db.collection.insertOne () Nuevo en la versión 3.2
db.collection.insertMany () Nuevo en la versión 3.2
```
En MongoDB, las operaciones de inserción tienen como objetivo una sola colección. Todas las operaciones de escritura en MongoDB son atómicas al nivel de un solo documento.

* Crear una colección (opcional) y añadir un elemento en formato JSON. La base de datos responde true si la operación fue exitosa y crea el campo irrepetible de _id si nosotros no lo especificamos: ```db.NOMBRE_COLECCIÓN.insertOne({ ... }) ```

* Crear una colección (opcional) y añadir algunos elementos en formato JSON. Recibe un array de elementos y devuelve todos los IDs de los elementos que se crearon correctamente.
```db.NOMBRE_COLECCIÓN.insertMany([{ ... }, { ... }])```

![InsertOne](https://docs.mongodb.com/manual/_images/crud-annotated-mongodb-insertOne.bakedsvg.svg)

### Leer (find)

Las operaciones de lectura recuperan documentos de una colección; es decir, consultar una colección de documentos. MongoDB proporciona los siguientes métodos para leer documentos de una colección. Puede especificar filtros de consulta o criterios que identifiquen los documentos a devolver.

```
db.collection.find ()
```

* Encontrar elementos en una colección: 
```db.NOMBRE_COLECCIÓN.find()``` 
* Podemos aplicar filtros y mostrar todos los elementos: 
```db.NOMBRE_COLECCIÓN.find({filtroA:"valor1", filtroB:"valor2"})```
* Podemos aplicar filtros y mostrar uno de los elementos:
```db.NOMBRE_COLECCIÓN.find({filtroA:"valor1",filtroB:"valor2"}).limit(1)```
* Leer solo ciertos campos del elemento (se escribe un 1): 
```db.NOMBRE_COLECCIÓN.find({filtro:valorfiltro}, {campoA: 1, campoC: 1)```
* Leer todos los campos de un elemento excluyendo (se escribe un 0): 
```db.NOMBRE_COLECCIÓN.find({filtro:valorfiltro}, {campoB: 0)```

* Si queremos encontrar un **elemento por su id** es importante aplicar una transformación de tipo de variable de "string" a ObjectId("string").
 ```db.NOMBRE_COLECCIÓN.find{'_id': ObjectId(curso['_id'])}```
* Para limitar el numero de resultados de la busqueda se usa el métodod .limit(n) 

![FindOne](https://docs.mongodb.com/manual/_images/crud-annotated-mongodb-find.bakedsvg.svg)


### Actualizar (set)
Las operaciones de actualización modifican los documentos existentes en una colección. MongoDB proporciona los siguientes métodos para actualizar documentos de una colección:
```
db.collection.updateOne () Nuevo en la versión 3.2
db.collection.updateMany () Nuevo en la versión 3.2
db.collection.replaceOne () Nuevo en la versión 3.2
```
En MongoDB, las operaciones de actualización tienen como objetivo una sola colección. Todas las operaciones de escritura en MongoDB son atómicas al nivel de un solo documento.

Puede especificar criterios o filtros que identifiquen los documentos a actualizar. Estos filtros utilizan la misma sintaxis que las operaciones de lectura.

Esquema: 
```db.cursos.updateOne({filtros}, {$set: {campo:valor}}).modified_count```
```db.cursos.updateMany({filtros}, {$set: {campo:valor}}).modified_count```

Ejemplo:
```db.cursos.updateOne({'_id': ObjectId(curso['_id'])}, {'$set': {'nombre': curso['nombre'], 'descripcion': curso['descripcion'], 'clases': curso['clases']}}).modified_count```

![UpdateMany](https://docs.mongodb.com/manual/_images/crud-annotated-mongodb-updateMany.bakedsvg.svg)


### Eliminar
Las operaciones de eliminación eliminan documentos de una colección. MongoDB proporciona los siguientes métodos para eliminar documentos de una colección:
```
db.collection.deleteOne () Nuevo en la versión 3.2
db.collection.deleteMany () Nuevo en la versión 3.2
```
En MongoDB, las operaciones de eliminación tienen como objetivo una sola colección. Todas las operaciones de escritura en MongoDB son atómicas al nivel de un solo documento.

Puede especificar criterios o filtros que identifiquen los documentos que se eliminarán. Estos filtros utilizan la misma sintaxis que las operaciones de lectura.

![DeleteMany](https://docs.mongodb.com/manual/_images/crud-annotated-mongodb-deleteMany.bakedsvg.svg)

## Operadores de consulta

### Operadores de comparació
* **$eq** : Operador igual =.
* **$gt** : Operador mayor que >.
* **$gte** : Operador mayor o igual que >=.
* **$lt** : Operador menor que >.
* **$lte** : Operador manor o igual que >=.
* **$ne** : Operador distinto de.
* **$in** : Valores dentro de un arreglo.
* **$nin** : Valores que no están dentro de un arreglo.
### Operadores lógicos
* **$and** : Une queries con un and lógico (similar al uso de una coma en un filtro).
* **$not** : Invierte el efecto de una query.
* **$nor** : Une queries con un nor lógico.
* **$or** : Une queries con un or lógico (si una condición se cumple nos trae el documento) ```db.inventory.find( { $or: [ { status: “A” }, { qty: { $lt: 30 } } ] } )```.
### Operadores por elemento
* **$exist** : Documentos que cuentan con un campo específico (Ejemplo: campo edad).
* **$type** : Documentos que cuentan con un campo de un tipo específico (Ejemplo: tipo datetime).
### Operadores para arreglos
* **$all** : Arreglos que contengan todos los elementos de la query ```db.articles.find( { tags: { $all: [ [ “ssl”, “security” ] ] } } )```.
* **$elemMatch** : Documentos que cumplen la condición del $elemMatch en uno de sus documentos (condiciones dentro de subdocumentos) ```db.inventory.find( { “instock”: { $elemMatch: { qty: 5, warehouse: “A” } } } )```
* **$size** : Documentos que contienen un campo tipo arreglo de un tamaño específico.

https://docs.mongodb.com/manual/tutorial/query-documents/



# Querys complejas

```
# -----------------Carreras-------------------------


def crear_carrera(json):
    return str(db.carreras.insert_one(json).inserted_id)


def consultar_carrera_por_id(carrera_id):
    return dumps(db.carreras.find_one({'_id': ObjectId(carrera_id)}))


def actualizar_carrera(carrera):
    # Esta funcion solamente actualiza nombre y descripcion de la carrera
    return str(db.carreras.update_one({'_id': ObjectId(carrera['_id'])},
                           {'$set': {'nombre': carrera['nombre'], 'descripcion': carrera['descripcion']}})
               .modified_count)


def borrar_carrera_por_id(carrera_id):
    return str(db.carreras.delete_one({'_id': ObjectId(carrera_id)}).deleted_count)


# Clase de operadores
def consultar_carreras(skip, limit):
    return dumps(db.carreras.find({}).skip(int(skip)).limit(int(limit)))


def agregar_curso(json):
    curso = consultar_curso_por_id_proyeccion(json['id_curso'], proyeccion={'nombre': 1})
    return str(db.carreras.update_one({'_id': ObjectId(json['id_carrera'])}, {'$addToSet': {'cursos': curso}}).modified_count)


def borrar_curso_de_carrera(json):
    return str(db.carreras.update_one({'_id': ObjectId(json['id_carrera'])}, {'$pull': {'cursos': {'_id': ObjectId(json['id_curso'])}}}).modified_count)

# -----------------Cursos-------------------------


def crear_curso(json):
    return str(db.cursos.insert_one(json).inserted_id)


def consultar_curso_por_id(id_curso):
    return dumps(db.cursos.find_one({'_id': ObjectId(id_curso)}))


def actualizar_curso(curso):
    # Esta funcion solamente actualiza nombre, descripcion y clases del curso
    return str(db.cursos.update_one({'_id': ObjectId(curso['_id'])},  {'$set': {'nombre': curso['nombre'],'descripcion': curso['descripcion'],'clases': curso['clases']}}).modified_count)


def borrar_curso_por_id(curso_id):
    return str(db.cursos.delete_one({'_id': ObjectId(curso_id)}).deleted_count)


def consultar_curso_por_id_proyeccion(id_curso, proyeccion=None):
    return db.cursos.find_one({'_id': ObjectId(id_curso)}, proyeccion)

```
    


## Usando operadores para realizar Updates en arreglos

En este enlace se encuentran la referencia a todos los operadores que se encuentran en MongoDb, antes de emplear lógica adicional para realizar una operación vale la pena echar una ojeada a la lista de operadores que en algunos casos pueden facilitar mucho las cosas.

Para realizar las relaciones entre carreras y cursos empleamos los operadores $addToSet y $pull estos operadores sirven para agregar $addToSet o retirar $pulldocumentos de un arreglo dependiendo del filtro que aplicamos.

Así cuando ejecutamos ```db.carreras.update_one({'_id': ObjectId(json['id_carrera'])}, {'$addToSet': {'cursos': curso}}) ``` $addToSet lo que hace es agregar el objeto curso al arreglo cursos, si el arreglo cursos no existe lo crea.

Para retirar un curso de una carrera usamos $pull de la siguiente manera ```db.carreras.update_one({'_id': ObjectId(json['id_carrera'])}, {'$pull': {'cursos': {'_id': ObjectId(json['id_curso'])}}})``` aquí $pull recibe un filtro y todos los elementos del arreglo cursos que cumplan con ese filtro serán borrados.

skip() y limit()

Si tenemos una consulta que retorna 100 documentos pero solamente necesitamos los documentos del número 20 al 30, la manera de hacerlo es usando skip() y limit().

Si tenemos 100 carreras y solamente queremos las primeras 10 podemos ejecutar ```db.carreras.find({}).limit(10)``` esta nos traerá las primeras 10 carreras.

Ahora si queremos las carreras ubicadas en los puestos 40 y 50 lo que debemos hacer es ```db.carreras.find({}).skip(40).limit(10)```

Como vemos skip() y limit() son muy útiles para realizar paginaciones, cuando tenemos consultas que retornan muchos documentos y que en algunos casos la totalidad de los documentos no es utilizada es buena práctica limitar el número de documentos que hacemos viajar entre nuestro cluster de base de datos y el código de nuestra aplicación. Esto puede ayudar a mejorar la velocidad con que las consultas son procesadas por la aplicación.

Ejercicios de práctica usando operadores
```
// Arreglo de ejemplo
use test
db.inventory.insertMany(

[{ _id: 1, item: { name: "ab", code: "123" }, qty: 15, tags: [ "A", "B", "C" ] },
{ _id: 2, item: { name: "cd", code: "123" }, qty: 20, tags: [ "B" ] },
{ _id: 3, item: { name: "ij", code: "456" }, qty: 25, tags: [ "A", "B" ] },
{ _id: 4, item: { name: "xy", code: "456" }, qty: 30, tags: [ "B", "A" ] },
{ _id: 5, item: { name: "mn", code: "000" }, qty: 20, tags: [ [ "A", "B" ], "C" ] }]

)

// $or
db.inventory.find({$or: [{qty: {$gt: 25}}, {qty: {$lte: 15}}]})

// $gte
db.inventory.find({qty: {$gte: 25}})

// $size
db.inventory.find({tags: {$size: 2}})

// Insertemos estos documentos de ejemplo en la colección survey
db.survey.insertMany([
{ _id: 1, results: [ { product: "abc", score: 10 }, { product: "xyz", score: 5 } ] }
{ _id: 2, results: [ { product: "abc", score: 8 }, { product: "xyz", score: 7 } ] }
{ _id: 3, results: [ { product: "abc", score: 7 }, { product: "xyz", score: 8 } ] }
])

// $elemMatch
db.survey.find(
   { results: { $elemMatch: { product: "xyz", score: { $gte: 8 } } } }
)

db.survey.find(
   { results: { $elemMatch: { product: "xyz" } } }```

```



# Pipelines de agregaciones
Las agregaciones son operaciones avanzadas que podemos realizar sobre nuestra base de datos con un poco más de flexibilidad en nuestros documentos.

* **Pipeline de Agregaciones:** Es un grupo de multiples etapas que ejecutan agregaciones en diferentes momentos. Debemos tener muy en cuenta el performance de nuestras agregaciones porque las agregaciones corren en todo el cluster.
https://docs.mongodb.com/manual/core/aggregation-pipeline/

![Pipeline ejemplo](https://imgs.developpaper.com/imgs/2280896570-5da47e5a388ce_articlex.png)

* **Map-Reduce:** Nos permite definir funciones de JavaScript para ejecutar operaciones avanzadas. La función de map nos permite definir o “mappear” los campos que queremos usar y la función reduce nos permite ejecutar operaciones y devolver resultados especiales. Por ejemplo: podemos mappear algunos campos y calcular la cantidad de elementos que cumplen ciertas condiciones.
https://docs.mongodb.com/manual/core/map-reduce/

![Map reduce ejemplo](https://docs.mongodb.com/manual/_images/map-reduce.bakedsvg.svg)

* **Agregaciones de propósito único:** Funciones ya definidas que nos ayudan a calcular un resultado especial pero debemos tener cuidado porque pueden mejorar o afectar el performance de la base de datos. Por ejemplo: count(), estimatedDocumentCount y distinct.

```bash
db.inventory.count()
db.inventory.estimatedDocumentCount()
db.inventory.disctinct()
```

![SPA reduce ejemplo](https://docs.mongodb.com/manual/_images/distinct.bakedsvg.svg)



# Indices para consultas rápidas
Para comparar la diferencia entre el rendimiento puedes utilizar el comando ```explain('executionStats')```

por ejemplo, en una colección de ejemplo students (la puedes obtener acá e importar a atlas de acuerdo a esta guía). Vamos a buscar los estudiantes cuyo nombre sea ‘Tandra Meadows’
```
db.students.find({name: 'Tandra Meadows'}).explain('executionStats')
```

en los resultados vas a encontrar executionTimeMillis y totalDocsExamined, en nuestro ejemplo los valores son 0 y 200 respectivamente. Este es un conjunto muy pequeño, por ello el tiempo de ejecución es irrelevante, pero el número de documentos examinados es el total de elementos en la colección (imagina 1 billón de registros).

ahora vamos a agregar un índice de tipo texto a nuestro campo y comparar los resultados haciendo una consulta que utilice este índice
```
db.students.createIndex({name: 'text'})
db.students.find({$text: {$search: 'Tandra Meadows'}}).explain('executionStats')
```
o dado que agregamos el índice de texto podemos utilizar solo un nombre y sin importar mayúsculas o minúsculas

```
db.students.find({$text: {$search: 'tandra'}}).explain('executionStats')
ahora el número de documentos examinados es de 2 solamente.
```
bonus

Para hacer una consulta ‘parcial’, es decir, que incluya solo una parte del nombre -como en la clase cuando se busca mongo y no arroja resultados hasta que se utiliza mongodb- podemos utilizar expresiones regulares (el operador $regex) sin importar las mayúsculas y minúsculas, case insensitive (/i), de la siguiente manera.

```
db.cursos.find({nombre: {$regex: /mongo/i}})
el detalle es que en la búsqueda de expresiones regulares no se utiliza el índice que creamos ☹️
```

además el problema con los índices de texto es que si indexas varios campos los resultados de la búsqueda incluirán todos ellos, es decir, no puedes especificar el campo sobre el que se hará la búsqueda. En nuestro ejemplo, si agregamos un campo tutor con el nombre del tutor y creamos un índice de texto para este nuevo campo, al buscar los estudiantes nos incluirá también aquellos que tengan como tutor alguien llamado ‘Tandra’. Esto se puede resolver agregando un segundo filtro de tipo regex.
