from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuarios (models.Model):

    usuario = models.CharField(max_length=15)
    email = models.EmailField()
    uids = models.IntegerField()
    server = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.usuario} --- {self.uids} --- {self.server}"
    
class e_adventure (models.Model):

    pj_nombre = models.CharField(max_length=40)
    pj_elemento = models.CharField(max_length=40)
    pj_lv = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.pj_nombre} --- {self.pj_elemento} --- {self.pj_lv}"

    

class e_abiss (models.Model):

    pj_nombre = models.CharField(max_length=40)
    pj_elemento = models.CharField(max_length=40)
    pj_lv = models.CharField(max_length=15)
    fecha_abismo = models.DateField()
    paso = models.BooleanField()

    def __str__(self):
        return f"{self.pj_nombre} --- {self.pj_lv} --- {self.paso}"
    
class artefactos (models.Model):

    pj_nombre = models.CharField(max_length=30)
    pluma = models.CharField(max_length=40)
    reloj = models.CharField(max_length=40)
    gorro = models.CharField(max_length=40)
    copa = models.CharField(max_length=40)
    flor = models.CharField(max_length=40)
    lv_general = models.IntegerField()

    def __str__(self):
        return f"{self.pj_nombre} --- {self.pj_lv} --- {self.paso}"
    

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    imagen = models.ImageField(upload_to="avatares", null= True, blank=True)
