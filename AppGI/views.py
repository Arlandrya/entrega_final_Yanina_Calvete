from django.shortcuts import render
from django.http import HttpResponse
from AppGI.models import Usuarios, e_abiss, e_adventure, Avatar, artefactos
from AppGI.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request):

    return render(request, "AppGI/inicio.html", {"mensaje": "Bienvenido al registro de equipos para Genshin Impact"})


#iniciar sesion 

def iniciar_sesion(request):
    if request.method == "POST":
    

        info_formulario = AuthenticationForm(request, data = request.POST)

        if info_formulario.is_valid():

            info_dic = info_formulario.cleaned_data

            usuario = authenticate(username = info_dic["username"], password=info_dic["password"])

            if usuario is not None:

                login(request,usuario)

                return render(request, "AppGI/inicio.html", {"mensajes":f"Bienvenido {usuario}"})

        
        else:
         
            return render(request, "AppGI/inicio.html",{"mensajes": "Error al ingresar, por favor intente de nuevo"})
        
    else:

        info_formulario = AuthenticationForm()

    return render(request, "AppGI/registro/inicio_sesion.html", {"formu":info_formulario})


#registrar

def registrarse(request):

    if request.method =="POST":

        info_formulario= RegistroUsuario(request.POST)

        if info_formulario.is_valid():

            info_formulario.save()

            return render(request, "AppGI/inicio.html",{"mensajes": "El usuario se ha creado exitosamente"})
        
    else:
         info_formulario=RegistroUsuario()

    return render(request, "AppGI/registro/registro.html",{"formu":info_formulario})


#editar usuario
@login_required
def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":

        miformulario = EditarUsuario(request.POST)

        if miformulario.is_valid():

            informacion = miformulario.cleaned_data

            usuario.email = informacion ["email"]
           
            usuario.set_password(informacion["password1"])


            usuario.save()

            return render (request, "AppGI/inicio.html")
        
    else:

        miformulario = EditarUsuario(initial= {"email" : usuario.email})  

    return render (request, "AppGI/registro/editar_usuario.html", {"form": miformulario})


#log out

def cerrar_sesion(request):

    logout(request)

    return render(request, "AppGI/inicio.html",{"mensajes": "Ha cerrado sesion exitosamente"})

#Agregar Avatar
@login_required
def agregar_avatar(request):

    if request.method =="POST":

        info_formulario= AvatarForm(request.POST, request.FILES)

        if info_formulario.is_valid():

            info=info_formulario.cleaned_data

            usuario_actual= User.objects.get(username=request.user)        
            nuevo_avatar = Avatar(usuario=usuario_actual, imagen=info["imagen"])

            nuevo_avatar.save()

            return render(request, "AppGI/inicio.html",{"mensajes": "Has creado tu avatar exitosamente"})
        
    else:
         info_formulario=AvatarForm()

    return render(request, "AppGI/registro/nuevo_avatar.html",{"formu":info_formulario})


#CRUD usuario
@login_required
def crear_usuario(request):

    if request.method == "POST":

        info_formulario = Usuarios_formulario(request.POST)

        if info_formulario.is_valid():

            info_dic = info_formulario.cleaned_data

            usuario_nuevo = Usuarios(
                usuario=info_dic["usuario"], 
                email=info_dic["email"],
                uids=info_dic["uids"],
                server=info_dic["server"]
                )
            
            usuario_nuevo.save()

            return render(request, "AppGI/inicio.html")
        
    else:
         
         info_formulario = Usuarios_formulario()

    return render(request, "AppGI/usuario/crear_usuario.html",{"formu": info_formulario})

def busqueda_usuario(request):
    
    return render(request, "AppGI/usuario/buscar_usuario.html")


def resultados_usuario(request):

    usuario = request.GET["usuario"]

    resultado = Usuarios.objects.filter(usuario = usuario)

    return render(request, "AppGI/usuario/resultados.html", {"resultado":resultado})





#CRUD Aventura
@login_required
def crear_e_adventure(request):

    if request.method == "POST":

        info_formulario = e_adventure_formulario(request.POST)

        if info_formulario.is_valid():

            info_dic = info_formulario.cleaned_data

            adventure_nuevo = e_adventure(
                pj_nombre=info_dic["pj_nombre"], 
                pj_elemento=info_dic["pj_elemento"],
                pj_lv=info_dic["pj_lv"]
                )
            
            adventure_nuevo.save()

            return render(request, "AppGI/inicio.html")
        
    else:
         
         info_formulario = e_adventure_formulario()

    return render(request, "AppGI/aventura/crear_e_adventure.html",{"formu": info_formulario})


def ver_e_aventura (request):
    todos_equipos_av = e_adventure.objects.all()

    return render (request, "AppGI/aventura/ver_e_aventura.html", {"v_e_aventura":todos_equipos_av})

@login_required
def actualizar_e_av(request, e_av_id):

    e_av_elegido = e_adventure.objects.get(id=e_av_id) 

    if request.method == "POST":
        info_formulario = e_adventure_formulario(request.POST)

        if info_formulario.is_valid():

            info_dic = info_formulario.cleaned_data

        
            e_av_elegido.pj_nombre=info_dic["pj_nombre"], 
            e_av_elegido.pj_elemento=info_dic["pj_elemento"],
            e_av_elegido.pj_lv=info_dic["pj_lv"]
                
            
            e_av_elegido.save()

            return render(request, "AppGI/inicio.html")
        
    else:
         
         info_formulario = e_adventure_formulario(initial={"pj_nombre":e_av_elegido.pj_nombre, "pj_elemento":e_av_elegido.pj_elemento, "pj_lv":e_av_elegido.pj_lv})

    return render(request, "AppGI/aventura/actualizar_e_av.html",{"formu": info_formulario})

@login_required
def borrar_e_av(request,e_av_id):
    e_av_elegido = e_adventure.objects.get(id=e_av_id)
    e_av_elegido.delete()

    return render(request,"AppGI/inicio.html")

#CRUD Abismo 
@login_required
def crear_e_abiss(request):

    if request.method == "POST":

        info_formulario = e_abiss_formulario(request.POST)

        if info_formulario.is_valid():

            info_dic = info_formulario.cleaned_data

            abiss_nuevo = e_abiss(
                pj_nombre=info_dic["pj_nombre"], 
                pj_elemento=info_dic["pj_elemento"],
                pj_lv=info_dic["pj_lv"],
                fecha_abismo=info_dic["fecha_abismo"],
                paso=info_dic["paso"]
                )
            
            abiss_nuevo.save()

            return render(request, "AppGI/inicio.html")
        
    else:
         
         info_formulario = e_abiss_formulario()

    return render(request, "AppGI/abismo/crear_e_abiss.html",{"formu": info_formulario})


def ver_e_abismo (request):
    todos_equipos_ab = e_abiss.objects.all()

    return render (request, "AppGI/abismo/ver_e_abismo.html", {"v_e_abismo":todos_equipos_ab})

@login_required
def actualizar_e_ab(request, e_ab_id):

    e_ab_elegido = e_abiss.objects.get(id=e_ab_id)

    if request.method == "POST":
        info_formulario = e_abiss_formulario(request.POST)

        if info_formulario.is_valid():

            info_dic = info_formulario.cleaned_data

        
            e_ab_elegido.pj_nombre=info_dic["pj_nombre"], 
            e_ab_elegido.pj_elemento=info_dic["pj_elemento"],
            e_ab_elegido.pj_lv=info_dic["pj_lv"],
            e_ab_elegido.fecha_abismo=info_dic["fecha_abismo"],
            e_ab_elegido.paso=info_dic["paso"]

            
                
            
            e_ab_elegido.save()

            return render(request, "AppGI/inicio.html")
        
    else:
         
         info_formulario = e_abiss_formulario(initial={"pj_nombre":e_ab_elegido.pj_nombre, "pj_elemento":e_ab_elegido.pj_elemento, "pj_lv":e_ab_elegido.pj_lv, "fecha_abismo":e_ab_elegido.fecha_abismo, "paso":e_ab_elegido.paso})

    return render(request, "AppGI/abismo/actualizar_e_ab.html",{"formu": info_formulario})

@login_required
def borrar_e_ab(request,e_ab_id):
    e_ab_elegido = e_abiss.objects.get(id=e_ab_id)
    e_ab_elegido.delete()

    return render(request,"AppGI/inicio.html")

#CRUD Artefactos
@login_required
def crear_artefactos(request):

    if request.method == "POST":

        info_formulario = artefactos_formulario(request.POST)

        if info_formulario.is_valid():

            info_dic = info_formulario.cleaned_data

            artefactos_nuevos = artefactos(
                pj_nombre=info_dic["pj_nombre"],
                pluma=info_dic["pluma"], 
                reloj=info_dic["reloj"],
                gorro=info_dic["gorro"],
                copa=info_dic["copa"],
                flor = info_dic["flor"],
                lv_general = info_dic["lv_general"],
                )
            
            artefactos_nuevos.save()

            return render(request, "AppGI/inicio.html")
        
    else:
         
         info_formulario = artefactos_formulario()

    return render(request, "AppGI/artefactos/crear_artefactos.html",{"formu": info_formulario})


def ver_artefactos (request):
    todos_artefactos = artefactos.objects.all()

    return render (request, "AppGI/artefactos/ver_artefactos.html", {"v_ar":todos_artefactos})

@login_required
def actualizar_artefactos(request, ar_id):

    artefactos_elegidos = artefactos.objects.get(id=ar_id) 

    if request.method == "POST":
        info_formulario = artefactos_formulario(request.POST)

        if info_formulario.is_valid():

            info_dic = info_formulario.cleaned_data

        
            artefactos_elegidos.pj_nombre=info_dic["pj_nombre"],
            artefactos_elegidos.pluma=info_dic["pluma"], 
            artefactos_elegidos.reloj=info_dic["reloj"],
            artefactos_elegidos.gorro=info_dic["gorro"],
            artefactos_elegidos.copa=info_dic["copa"],
            artefactos_elegidos.flor=info_dic["flor"],
            artefactos_elegidos.lv_general=info_dic["lv_general"]

            
            artefactos_elegidos.save()

            return render(request, "AppGI/inicio.html")
        
    else:
         
         info_formulario = artefactos_formulario(initial={"pj_nombre":artefactos_elegidos.pj_nombre,"pluma":artefactos_elegidos.pluma, "reloj":artefactos_elegidos.reloj, "gorro":artefactos_elegidos.gorro, "copa":artefactos_elegidos.copa, "flores":artefactos_elegidos.flor, "lv_general":artefactos_elegidos.lv_general})

    return render(request, "AppGI/artefactos/actualizar_artefactos.html",{"formu": info_formulario})

@login_required
def borrar_artefactos(request,ar_id):
    artefactos_elegidos = artefactos.objects.get(id=ar_id)
    artefactos_elegidos.delete()

    return render(request,"AppGI/inicio.html")


def acerca_de_mi(request):

    return render (request, "AppGI/about.html")