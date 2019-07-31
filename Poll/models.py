from django.db import models

# Create your models here.


class Tabla_usuario(models.Model):
    user = models.CharField(max_length=200)
    pass_user = models.CharField(max_length=200)
    nombre_empresa = models.CharField(max_length=100, default="")
    rut_empresa = models.CharField(max_length=15, default="")

