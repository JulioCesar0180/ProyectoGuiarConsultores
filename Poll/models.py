from django.db import models

# Create your models here.


class Tabla_usuario(models.Model):
    user = models.CharField(max_length=200)
    pass_user = models.CharField(max_length=200)
    nombre_empresa = models.CharField(max_length=100, default="")
    rut_empresa = models.CharField(max_length=15, default="")
    direccion_empresa = models.CharField(max_length=100, default="")
    experiencia_empresa = models.CharField(max_length=10, default="")
    ciudad_empresa = models.CharField(max_length=20, default="")
    comuna_empresa = models.CharField(max_length=20, default="")
    nombre_contacto_empresa = models.CharField(max_length=100, default="")
    telefono_empresa = models.CharField(max_length=20, default="")
    email_empresa = models.CharField(max_length=100, default="")
    ventas_anuales_empresa = models.CharField(max_length=50, default="")
