from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tabla_perfil_usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
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
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=2, default="")
    answer2 = models.CharField(max_length=2, default="")
    answer3 = models.CharField(max_length=2, default="")
    answer4 = models.CharField(max_length=2, default="")
    answer5 = models.CharField(max_length=2, default="")
    answer6 = models.CharField(max_length=2, default="")
    answer7 = models.CharField(max_length=2, default="")

class Tabla_resultados_manufactura(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=2, default="")
    answer2 = models.CharField(max_length=2, default="")
    answer3 = models.CharField(max_length=2, default="")
    answer4 = models.CharField(max_length=2, default="")
    answer5 = models.CharField(max_length=2, default="")
    answer6 = models.CharField(max_length=2, default="")

class Tabla_resultados_servicios(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
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

class Tabla_resultados_dotacion(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=2, default="")
    answer2 = models.CharField(max_length=2, default="")
    answer3 = models.CharField(max_length=2, default="")
    answer4 = models.CharField(max_length=2, default="")
    answer5 = models.CharField(max_length=2, default="")
    answer6 = models.CharField(max_length=2, default="")
    answer7 = models.CharField(max_length=2, default="")
    answer8 = models.CharField(max_length=2, default="")

class Tabla_resultados_gestion(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
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

class Tabla_resultados_procesos(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=2, default="")
    answer2 = models.CharField(max_length=2, default="")
    answer3 = models.CharField(max_length=2, default="")
    answer4 = models.CharField(max_length=2, default="")
    answer5 = models.CharField(max_length=2, default="")

class Tabla_resultados_explosivos(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=2, default="")
    answer2 = models.CharField(max_length=2, default="")
    answer3 = models.CharField(max_length=2, default="")
    answer4 = models.CharField(max_length=2, default="")
    answer5 = models.CharField(max_length=2, default="")

class Tabla_resultados_electricidad(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=2, default="")
    answer2 = models.CharField(max_length=2, default="")
    answer3 = models.CharField(max_length=2, default="")
    answer4 = models.CharField(max_length=2, default="")
    answer5 = models.CharField(max_length=2, default="")

class Tabla_resultados_sustancias_peligrosas(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=2, default="")
    answer2 = models.CharField(max_length=2, default="")
    answer3 = models.CharField(max_length=2, default="")
    answer4 = models.CharField(max_length=2, default="")
    answer5 = models.CharField(max_length=2, default="")
    answer6 = models.CharField(max_length=2, default="")

class Tabla_resultados_altura(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=2, default="")
    answer2 = models.CharField(max_length=2, default="")
    answer3 = models.CharField(max_length=2, default="")
    answer4 = models.CharField(max_length=2, default="")

class Tabla_resultados_finales(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    riesgo_transporte = models.CharField(max_length=2, default="")
    riesgo_construccion = models.CharField(max_length=2, default="")
    riesgo_manufactura = models.CharField(max_length=2, default="")
    riesgo_servicios = models.CharField(max_length=2, default="")
    riesgo_dotacion = models.CharField(max_length=2, default="")
    riesgo_gestion = models.CharField(max_length=2, default="")
    riesgo_procesos = models.CharField(max_length=2, default="")
    riesgo_explosivos = models.CharField(max_length=2, default="")
    riesgo_electricidad = models.CharField(max_length=2, default="")
    riesgo_sustancias_peligrosas = models.CharField(max_length=2, default="")
    riesgo_altura = models.CharField(max_length=2, default="")

class Tabla_priorizacion_riesgos(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    resultados = models.ForeignKey(Tabla_resultados_finales, on_delete=models.CASCADE)
    responsabilidad_civil_empresa = models.CharField(max_length=2, default="")
    equipos_moviles = models.CharField(max_length=2, default="")
    transporte_terrestre = models.CharField(max_length=2, default="")
    vehiculos_comerciales_livianos = models.CharField(max_length=2, default="")
    vehiculos_comerciales_pesados = models.CharField(max_length=2, default="")
    accidentes_personales = models.CharField(max_length=2, default="")
