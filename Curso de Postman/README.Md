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
