from django.db import models

# Create your models here.


class Tabla_usuario(models.Model):
    user = models.CharField(max_length=200)
    pass_user = models.CharField(max_length=200)
