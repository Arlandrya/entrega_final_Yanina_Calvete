# entrega_final_Yanina_Calvete

##Pasos Tener instalado

django 5.0.3
python 3.11
vsc 1.87.0
Pillow
Comentario: Se ha creado el archivo mediante django, con startproyect, pararse en la carpeta correspondiente con el cd PE_3 y luego con colocar la App a través de python manage.py startapp Se ha tomato un template de start bootstrap. Para los templates, se a usado el padre para crear herencia para las otras plantillas. Arrastrar la carpeta al vsc y comenzamos:

python manage.py makemigrations para poder crear las tablas de las class en la db
Luego se hace el python manage.py migrate
Instalar un visor de sqlite Viewer
ir a la terminal y correr el python manage.py runserver para ver el server
ctrl+C para cerrar el server

Cuando se ingresa a la pagina por primera vez, se puede ingresar a los botones de about me, descargar, intagram y demas, pero no al resto de los botones.
La unica forma de acceder a todos estos es iniciando sesion. 

URL
inicio: http://127.0.0.1:8000/AGI/
crear usuario: http://127.0.0.1:8000/AGI/crear_usuario
buscar usuarios: http://127.0.0.1:8000/AGI/buscar_usuario
Crear equipo de aventura: http://127.0.0.1:8000/AGI/crear_e_adventure 
Ver/editar/eliminar equipo de aventuras: http://127.0.0.1:8000/AGI/ver_e_aventura
Crear equipo de abismo: http://127.0.0.1:8000/AGI/crear_e_abiss
Ver/editar/eliminar equipo de abismo: http://127.0.0.1:8000/AGI/ver_e_abismo
Crear artefactos: http://127.0.0.1:8000/AGI/crear_artefactos
Ver/editar/eliminar artefactos: http://127.0.0.1:8000/AGI/ver_artefactos
Editar usuario: http://127.0.0.1:8000/AGI/edit
Editar avatar: http://127.0.0.1:8000/AGI/avatar
About me: http://127.0.0.1:8000/AGI/about
