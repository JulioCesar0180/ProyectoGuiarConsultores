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

class Tabla_resultados_transporte(models.Model):
    empresa = models.ForeignKey(Tabla_usuario, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=2, default="")
    answer2 = models.CharField(max_length=2, default="")
    answer3 = models.CharField(max_length=2, default="")
    answer4 = models.CharField(max_length=2, default="")
    answer5 = models.CharField(max_length=2, default="")
    answer6 = models.CharField(max_length=2, default="")
    answer7 = models.CharField(max_length=2, default="")
    answer8 = models.CharField(max_length=2, default="")
    answer9 = models.CharField(max_length=2, default="")
    answer10 = models.CharField(max_length=2, default="")

class Tabla_resultados_construccion(models.Model):
    empresa = models.ForeignKey(Tabla_usuario, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=2, default="")
    answer2 = models.CharField(max_length=2, default="")
    answer3 = models.CharField(max_length=2, default="")
    answer4 = models.CharField(max_length=2, default="")
    answer5 = models.CharField(max_length=2, default="")
    answer6 = models.CharField(max_length=2, default="")
    answer7 = models.CharField(max_length=2, default="")

class Tabla_resultados_manufactura(models.Model):
    empresa = models.ForeignKey(Tabla_usuario, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=2, default="")
    answer2 = models.CharField(max_length=2, default="")
    answer3 = models.CharField(max_length=2, default="")
    answer4 = models.CharField(max_length=2, default="")
    answer5 = models.CharField(max_length=2, default="")
    answer6 = models.CharField(max_length=2, default="")

class Tabla_resultados_servicios(models.Model):
    empresa = models.ForeignKey(Tabla_usuario, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=2, default="")
    answer2 = models.CharField(max_length=2, default="")
    answer3 = models.CharField(max_length=2, default="")
    answer4 = models.CharField(max_length=2, default="")
    answer5 = models.CharField(max_length=2, default="")
    answer6 = models.CharField(max_length=2, default="")
    answer7 = models.CharField(max_length=2, default="")
    answer8 = models.CharField(max_length=2, default="")
    answer9 = models.CharField(max_length=2, default="")
    answer10 = models.CharField(max_length=2, default="")
    answer11 = models.CharField(max_length=2, default="")
    answer12 = models.CharField(max_length=2, default="")
    answer13 = models.CharField(max_length=2, default="")
    answer14 = models.CharField(max_length=2, default="")
