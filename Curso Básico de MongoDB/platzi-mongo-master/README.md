# Platzi Mongo
Todo el código que escribirás para el proyecto platzi-mongo
estará en el archivo db.py

# Postman
1. Descargar e instalar [Postman](https://www.getpostman.com/downloads/)
2. La URI de las colecciones de Postman usada para el proyecto está en [Postman-platzi-mongo](https://www.getpostman.com/collections/ffcbfb5c8d5cd2dc52d2)
3. Importar colección dentro de Postman [Instrucciones](https://learning.getpostman.com/docs/postman/collections/data_formats/#exporting-and-importing-postman-data)

## Instalar Anaconda 
La forma más simple de ejecutar el proyecto es instalando [Anaconda](https://www.anaconda.com/distribution/).

Con Anaconda instalado de manera correcta, navegar hasta el directorio del proyecto
y ejecutar: 
```
# navegar hasta el directorio del proyecto
cd platzi-mongo
# crear un nuevo ambiente
conda create --name platzi-mongo
# activar el ambiente 
conda activate platzi-mongo
# para desactivar el ambiente
conda deactivate
```
Si usas Python frecuentemente y tienes una versión 3.3+ no es necesario que 
instales Anaconda, crea un ambiente virtual con venv o virtualenv y sigue con 
el paso de instalar las dependencias.
## Instalar dependenias del proyecto
Con el ambiente activado, instalar las dependencias:
```
pip install -r requirements.txt
```
## Variables de entorno necesarias para ejecutar el proyecto
Asegurate de reemplazar el valor de PLATZI_DB_URI por la URI de tu cluster en MongoDB Atlas
```
export FLASK_APP=platzi-api
export FLASK_ENV=development 
export PLATZI_DB_URI="MONGO-URI"
```

## Iniciar el servidor de platzi-mongo
```
flask run
```
