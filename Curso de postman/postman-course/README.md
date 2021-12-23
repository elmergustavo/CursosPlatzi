
# This is the API for Postman Course

It is a simple version of an API builded with Django and Django Rest Framework
using Docker.


# You can learn how to build APIs here:

- [Curso de API REST](https://platzi.com/clases/api-rest/)
- [Curso de Django](https://platzi.com/clases/django/)
- [Curso Avanzado de Django](https://platzi.com/clases/django-avanzado/)
- [Curso de Fundamentos de Docker](https://platzi.com/clases/docker/)

# How to run this project
- Install Docker and Docker Compose
- Execute `docker-compose up -d`: This command starts a local server with the API running over 8000 port.
- Get inside the docker container executing `docker exec -it postman-course_web_1 bash`
- Inside the docker container execute `source admin_info.sh`
- Run the migrations `python manage.py runscript migrations.admin_migration`
