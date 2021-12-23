# Notas del curso de postman

* Un protocolo especifica reglas en la comunicacion entre dos entes, en este caso entre dos computudoras.

* HTTP (Hyper Text Transfer Protocol) fue creado especificamente para la web.

Una de las cosas que especifica el protocolo HTTP son los verbos:

* GET: solicitar datos o algun recurso.
* HEAD: traer headers (como una peticion GET pero sin contenidos). Es util cuando vamos a utilizar APIs, para comprobar si lo que vamos a enviar esta correcto y puede ser procesado.
* POST: enviar datos a un recurso para la creación.
* PUT: reemplazar por completo un recurso.
* PATCH: reemplazar parcialmente un recurso.
* DELETE: eliminar un recurso.
Otra de las cosas que especifica el protocolo HTTP son los codigo de estado (status codes). Sirven para describir el estado de la peticion hecha al servidor.

* 1xx: Indican que la peticion fue recibida y el servidor sigue trabajando en el proceso, es decir, no fue exitosa ni fue errónea, sino que esta siendo procesada aun.
* 2xx: Indican que la peticion fue recibida y procesada correctamente.
* 3xx: Indican que hay que tomar acciones adicionales para completar la solicitud. Por lo general estos codigos indican redireccion. Generalmente en los APIs no se usan redirecciones porque no contienen estados, es decir, toda la informacion esta contenida en una solicitud, no se guarda un estado en el servidor con una sesion por ejemplo.
* 4xx: Indican errores del lado del cliente, por ejemplo: se hizo mal la solicitud, faltan datos, headers o cualquier otro error que pueda ocurrir.
* 5xx: Indican errores del servidor. Suelen aparecer cuando existe un fallo en la ejecución en el servidor.
Los codigos mas comunes a la hora de interactuar con un API son:

* 200: Todo esta OK.
* 201: Todo OK cuando se hizo una solicitud POST, el recurso se creo y se guardo correctamente.
* 204: Indica que la solicitud se completo correctamente pero no devolvio informacion. Es muy comun cuando se hacen peticiones con el verbo DELETE.
* 400: Bad Request, algo esta mal en la peticion. Se nos olvido enviar un dato o algo relacionado. Por lo general la respuesta nos especifica cuales fueron los errores a la hora de hacer la peticion.
* 401: Unauthorized, es decir, no estamos autorizados (autenticados) a realizar la peticion.
* 403: Forbidden, yo no tengo acceso a ese recurso aunque este autenticado.
* 404: Not Found, no existe el recurso que se esta intentando acceder.
* 500: Interna Server Error, es un error que retorna el servidor cuando la solicitud no pudo ser procesada. Por lo general, si no tenemos acceso al backend, no tenemos control sobre los errores 500 que retorna un API.

* https://http.cat/

![](https://res.cloudinary.com/dynamic-sourcing-llc/image/upload/f_auto,q_auto,dpr_auto/v1559554843/infografia_c%C3%B3digos-estado-http_v6tgrl.png)

Códigos más usados

1. 200: Todo bien
2. 201: solicitud POST se ejecutó correctamente.
3. 204: Solicitud ejecutada correctamente y no devuelve información. Por ejemplo, al ejecutar el verbo DELETE.
4. 400: bad request, por ejemplo, falta información.
5. 401: No estar autenticado.
6. 403: Forbidden. No tener aceeso a un recurso.
7. 404: No existe el recurso. Not found.
8. 500: La solicitud no pudo ser ejecutada.

Mas errores de cliente
414 URI Too Long
La URI solicitada por el cliente es más larga que el servidor está dispuesto a interpretar.
415 Unsupported Media Type
El formato multimedia de los datos solicitados no está soportada por el servidor, por lo cual el servidor rechaza la solicitud.
416 Requested Range Not Satisfiable
El rango especificado por el campo de encabezado Range en la solicitud no cumple; es posible que el rango está fuera del tamaño de los datos objetivo del URI.
417 Expectation Failed
Significa que la expectativa indicada por el campo de encabezado Expect solicitada no puede ser cumplida por el servidor.
418 I’m a teapot
El servidor se reúsa a intentar hacer café con una tetera.
421 Misdirected Request
La petición fue dirigida a un servidor que no es capaz de producir una respuesta. Esto puede ser enviado por un servidor que no esta configurado para producir respuestas por la combinación del esquema y la autoridad que estan incluidos en la URI solicitada
422 Unprocessable Entity (WebDAV)
La petición estaba bien formada pero no se pudo seguir debido a errores de semántica.
423 Locked (WebDAV)
El recurso que está siendo accedido está bloqueado.
424 Failed Dependency (WebDAV)
La petición falló debido a una falla de una petición previa.
426 Upgrade Required
El servidor se reúsa a aplicar la solicitud usando el protocolo actual pero puede estar dispuesto a hacerlo después que el cliente se actualize a un protocolo diferente. El servidor envía un encabezado Upgrade en una respuesta para indicar los protocolos requeridos.
428 Precondition Required
El servidor origen requiere que la solicitud sea condicional. Tiene la intención de prevenir problemas de ‘actualización perdida’, donde un cliente OBTIENE un estado del recurso, lo modifica, y lo PONE devuelta al servidor, cuando mientras un tercero ha modificado el estado del servidor, llevando a un conflicto.
429 Too Many Requests
El usuario ha enviado demasiadas solicitudes en un periodo de tiempo dado.
431 Request Header Fields Too Large
El servidor no está dispuesto a procesar la solicitud porque los campos de encabezado son demasiado largos. La solicitud PUEDE volver a subirse después de reducir el tamaño de los campos de encabezado solicitados.
451 Unavailable For Legal Reasons
El usuario solicita un recurso ilegal, como alguna página web censurada por algún gobierno.

* https://developer.mozilla.org/es/docs/Web/HTTP/Status
* https://uniwebsidad.com/tutoriales/los-codigos-de-estado-de-http

![](https://static.platzi.com/media/user_upload/htttp-b67b024d-fd31-44d8-95d3-e0b571d3a9c9.jpg)
![](https://static.platzi.com/media/user_upload/http2-7b3b0f04-1732-474a-acb4-4ca3836b3ddd.jpg)

## Estructuras de las URLs
En un API es importante tener bien estructuradas las rutas por las cuales se usarán cada uno de los endpoints que contiene. Antes de entrar de lleno a explicar el API con el que trabajaremos en este curso veamos unos conceptos muy importantes a la hora de trabajar con APIs.

## Recurso
Es la instancia o la representación de un objeto o la representación de algo, tiene datos y operaciones asociadas a él. Por ejemplo: course, material y video son recursos que tenemos disponibles en el API con la que trabajaremos y podemos realizar operaciones sobre ellos: crear, actualizar y eliminar.

## Colecciones
Es un conjunto de recursos, por ejemplo: courses es una colección de course.

## URL
(Uniform Resource Locator) es la ruta en la cual puede ser ubicado un recurso y ejecutar las operaciones sobre él.

## CRUD
Siglas que hacen referencia a las operaciones básicas que se pueden ejecutar sobre un recurso:

* C: Create (crear)
* R: Read (leer)
* U: Update (actualizar)
* D: Delete (eliminar)

## Endpoints
Es el punto final de la comunicación con un ente, en este caso, un endpoint está asociado a una URL y a las operaciones que podemos ejecutar. Este término es muy utilizado en las APIs.

Los endpoint definen operaciones que se quieren ejecutar sobre un recurso. Por ejemplo: si queremos un conjunto de operaciones CRUD sobre Cursos podríamos crear los siguientes endpoints:

* /get-all-courses : para obtener una colección de Cursos.
* /add-new-course: para crear un nuevo recurso de Cursos.
* /delete-all-courses: para eliminar todos los Cursos.

Y así sucesivamente. Pero, esto implicaría un problema. El API puede llenarse de endpoints que ejecutan una sola operación, esto no es escalable, significa que si por ejemplo el recurso Cursos pasa a llamarse Clases habría que actualizar absolutamente todas las URLs y asegurarse de ello puede convertirse en un dolor de cabeza.

Entonces, ¿cuál es la buena práctica en este caso?

Como lo vimos en la clase pasada, el protocolo HTTP especifica una serie de verbos que indican acciones. Lo ideal es que la operación que se ejecute sobre un recurso se obtenga a través del verbo HTTP de la petición y no que esté definido en el endpoint. Por ejemplo:

* /courses: Dependiendo del verbo HTTP se ejecutará una operación en particular. Quedaría así:
    * GET /courses: trae la colección de Cursos.
    * POST /courses: crea un nuevo recurso de Cursos.
    * DELETE /courses: elimina todos los cursos.

De esta manera queda mucho más organizado un API. Pero, qué pasa si queremos traer no una colección de cursos como en los casos anteriores, sino un recurso en específico.

Por lo general cada recurso tiene un identificador único, un ID, es con esto que llamaremos a un endpoint para que nos retorne la información del recurso. Por ejemplo:

* GET /courses/2/: vemos que acá se le está pasando algo que en los endpoints anteriores no veíamos, es el número 2, ese es el identificador único, de esta manera el API sabe que tiene que buscar el curso con ID 2 y retornarlo.

Así sucesivamente con cada uno de los verbos, por ejemplo: casi nunca se hace una eliminación en masa en un API, como el ejemplo que tenemos más arriba donde se eliminan todos los cursos. Lo ideal es que se elimine un recurso individualmente y no una colección, igualmente pasa con la actualización.

## Recursos anidados

Hay veces en las que un recurso depende de otro recurso, por ejemplo, comentarios depende de materiales; usualmente en los APIs las anidaciones se hacen hasta dos niveles, es decir:

* materials/1/comments: estos son dos niveles
* materials/1/comments/2/answers/: son tres niveles, ahí lo ideal sería entonces separar el endpoint de comentarios y ejecutar comments/2/answers/

## Nuestro API

Ya he dado algunos spoilers sobre lo que nuestro API hace, es un clon de lo que Platzi es, una plataforma es donde tenemos Cursos, Materiales, Videos y Comentarios. El API es sencillo y es una prueba que utilizamos en este curso para explorar toda las capacidades que nos ofrece Postman para trabajar con ellos.

Una convención que se usa a la hora de documentar APIs es abstraer el endpoint de la URL del sitio al cual vamos a hacer la petición, puesto que esto al final es redundante de escribir, es decir, usualmente escribimos únicamente /api-token-auth/ en vez de [http://mistioweb.com/api-token-auth/](http://mistioweb.com/api-token-auth/).

## Los endpoints que tenemos:

* /api-token-auth/
* /courses
* /courses/:id/
* /courses/:id/upload_badge/
* /materials/
* /materials/:id/
* /materials/:id/comments/
* /comments/
* /comments/:id/
* /comments/:id/like/
* /comments/:id/dislike/



