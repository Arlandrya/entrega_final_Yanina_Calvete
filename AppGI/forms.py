from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class Usuarios_formulario (forms.Form):

    usuario = forms.CharField(max_length=15)
    email = forms.EmailField()
    uids = forms.IntegerField()
    server = forms.CharField(max_length=10)


class e_adventure_formulario (forms.Form):

    pj_nombre = forms.CharField(max_length=30)
    pj_elemento = forms.CharField(max_length=30)
    pj_lv = forms.CharField(max_length=15)


class e_abiss_formulario (forms.Form):

    pj_nombre = forms.CharField(max_length=40)
    pj_elemento = forms.CharField(max_length=40)
    pj_lv = forms.CharField(max_length=15)
    fecha_abismo = forms.DateField()
    paso = forms.BooleanField(required=False) 

class artefactos_formulario (forms.Form):

    pj_nombre = forms.CharField(max_length=30)
    pluma = forms.CharField(max_length=40)
    reloj = forms.CharField(max_length=40)
    gorro = forms.CharField(max_length=40)
    copa = forms.CharField(max_length=40)
    flor = forms.CharField(max_length=40)
    lv_general = forms.IntegerField()


class RegistroUsuario(UserCreationForm):

    class Meta:
        model= User
        fields= ["username", "first_name", "last_name","email", "password1", "password2"]


class EditarUsuario(UserCreationForm):

    class Meta:
        model= User
        fields= ["first_name", "last_name","email", "password1", "password2"]


class AvatarForm(forms.Form):
    imagen = forms.ImageField()