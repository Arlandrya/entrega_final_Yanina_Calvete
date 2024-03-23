from django.urls import path
from AppGI.views import *


urlpatterns = [
    #url de inicio
    path("", inicio, name="inicio"),
    #url de Login
    path("login", iniciar_sesion, name= "iniciar_sesion"),
    #url para registrarse
    path("signup", registrarse, name= "registrarse"),
    #editar perfil
    path("edit", editar_usuario, name= "editar_usuario"),
    #Agregar Acatar
    path("avatar", agregar_avatar, name= "agregar_avatar"),
    #url para desloguearse
    path("logout", cerrar_sesion, name= "cerrar_sesion"),
    #url de usuarios
    path("crear_usuario", crear_usuario, name="crear_usuario"),
    path("buscar_usuario", busqueda_usuario, name="buscar usuario"),
    path("resultados", resultados_usuario),
    #url de aventura
    path("crear_e_adventure", crear_e_adventure, name="crear_e_adventure"),
    path("ver_e_aventura", ver_e_aventura, name= "Ver equipos_av"),
    path("actualizar_e_aventura/<e_av_id>", actualizar_e_av, name="Editar Equipo Aventura"),
    path("borrar_e_aventura/<e_av_id>", borrar_e_av, name="Eliminar Equipo Aventura"),
    #url de abismo
    path("crear_e_abiss", crear_e_abiss, name="crear_e_abiss"),
    path("ver_e_abismo", ver_e_abismo, name= "Ver equipos_ab"),
    path("actualizar_e_abismo/<e_ab_id>", actualizar_e_ab, name="Editar Equipo Abismo"),
    path("borrar_e_abismo/<e_ab_id>", borrar_e_ab, name="Eliminar Equipo Abismo"),
    #url de artefactos
    path("crear_artefactos", crear_artefactos, name="crear_artefactos"),
    path("ver_artefactos", ver_artefactos, name="Ver artefactos"),
    path("actualizar_artefactos/<ar_id>", actualizar_artefactos, name="Editar Artefactos"),
    path("borrar_artefactos/<ar_id>", borrar_artefactos, name="Eliminar Artefactos"),
    #url de inicio
    path("about", acerca_de_mi, name="about"),

]