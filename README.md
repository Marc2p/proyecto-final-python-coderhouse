# Proyecto final Python Coderhouse
## Datos del proyecto
* Alumno: Marcos Peirone
* Comisión: 34675

## Descripción:
Se trata de una pequeña biblioteca, realizada utilizando el framework Django y plantillas html.
En ella se puede realizar un crud sobre libros, autores, idiomas y géneros, modelos que conforman un catálogo de libros disponibles.
También posee un sistema de inicio de sesión y registro, necesario para acceder al proyecto, así como para algunas páginas que requieren permisos específicos, especialmente para agregar y eliminar datos de los modelos.
Por último, posee un formulario de búsqueda, en el que se pueden buscar libros por título y autor.

### Ejecución del proyecto:
1) Ejecutar el comando python manage.py migrate para crear la base de datos
2) Ejecutar el proyecto en modo de desarrollo con python manage.py runserver
3) Acceder a http://localhost:8000
4) Todas las funcionalidades del proyecto se pueden probar desde su barra de navegación, excepto el formulario de búsqueda, disponible en todas las vistas en la barra lateral
5) Hay algunas vistas a las que solo se puede acceder desde otras vistas, por ejemplo, en la vista de libros, cada título es un enlace que dirige hacia la vista de detalle del mismo, donde se pueden ver más datos, así como modificarlos o eliminarlos