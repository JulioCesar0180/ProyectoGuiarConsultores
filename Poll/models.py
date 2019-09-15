from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.


#Manager
class UserGuiarManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, rut, password, **extra_fields):
        if not rut:
            raise ValueError('Error')
        user = self.model(rut=rut, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, password, **extrafields):
        user = self.model(rut=rut, **extrafields)
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


#Auth
class UserGuiar(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField(max_length=12, verbose_name="Rut Empresa", unique=True, default="")
    name = models.CharField(max_length=100, verbose_name="Nombre Empresa", default="")
    address = models.CharField(max_length=100, verbose_name="Direccion", default="")
    is_admin = models.BooleanField(default=False)
    #password = models.CharField(max_length=10, verbose_name="Contraseña", default="")
    objects = UserGuiarManager()
    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['name', 'address']

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class TablaResultadosTransporte(models.Model):
    rut_empresa = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)
    answer6 = models.BooleanField(default=False)
    answer7 = models.BooleanField(default=False)
    answer8 = models.BooleanField(default=False)
    answer9 = models.BooleanField(default=False)


class TablaResultadosContruccion(models.Model):
    rut_empresa = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)
    answer6 = models.BooleanField(default=False)


class TablaResultadosManufactura(models.Model):
    rut_empresa = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)
    answer6 = models.BooleanField(default=False)


class TablaResultadosServicios(models.Model):
    rut_empresa = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)
    answer6 = models.BooleanField(default=False)
    answer7 = models.BooleanField(default=False)
    answer8 = models.BooleanField(default=False)
    answer9 = models.BooleanField(default=False)
    answer10 = models.BooleanField(default=False)
    answer11 = models.BooleanField(default=False)
    answer12 = models.BooleanField(default=False)
    answer13 = models.BooleanField(default=False)
    answer14 = models.BooleanField(default=False)


class TablaResultadosDotacion(models.Model):
    rut_empresa = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.CharField(max_length=10, default="")
    answer2 = models.CharField(max_length=10, default="")
    answer3 = models.CharField(max_length=10, default="")
    answer4 = models.CharField(max_length=10, default="")
    answer5 = models.CharField(max_length=10, default="")
    answer6 = models.CharField(max_length=10, default="")
    answer7 = models.CharField(max_length=10, default="")
    answer8 = models.CharField(max_length=10, default="")


class TablaResultadosGestion(models.Model):
    rut_empresa = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)
    answer6 = models.BooleanField(default=False)
    answer7 = models.BooleanField(default=False)
    answer8 = models.BooleanField(default=False)
    answer9 = models.BooleanField(default=False)
    answer10 = models.BooleanField(default=False)


class TablaResultadosProcesos(models.Model):
    rut_empresa = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)


class TablaResultadosExplosivos(models.Model):
    rut_empresa = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)
    answer6 = models.BooleanField(default=False)


class TablaResultadosElectricidad(models.Model):
    rut_empresa = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)


class TablaResultadosSustanciasPeligrosas(models.Model):
    rut_empresa = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)
    answer6 = models.BooleanField(default=False)
    answer7 = models.BooleanField(default=False)
    answer8 = models.BooleanField(default=False)
    answer9 = models.BooleanField(default=False)


class TablaResultadosRiesgoAltura(models.Model):
    rut_empresa = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)


class TablaResultadosFinales(models.Model):
    rut_empresa = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    riesgo_transporte = models.CharField(max_length=3, default="")
    riesgo_construccion = models.CharField(max_length=3, default="")
    riesgo_manufactura = models.CharField(max_length=3, default="")
    riesgo_servicios = models.CharField(max_length=3, default="")
    riesgo_dotacion = models.CharField(max_length=3, default="")
    riesgo_gestion = models.CharField(max_length=3, default="")
    riesgo_procesos = models.CharField(max_length=3, default="")
    riesgo_explosivos = models.CharField(max_length=3, default="")
    riesgo_electricidad = models.CharField(max_length=3, default="")
    riesgo_sustancias_peligrosas = models.CharField(max_length=3, default="")
    riesgo_altura = models.CharField(max_length=3, default="")

"""
class TablaPriorizacionRiesgos(models.Model):
    rut_empresa = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    resultados = models.ForeignKey(TablaResultadosFinales, on_delete=models.CASCADE)
    responsabilidad_civil_empresa = models.BooleanField(default=False)
    equipos_moviles = models.BooleanField(default=False)
    transporte_terrestre = models.BooleanField(default=False)
    vehiculos_comerciales_livianos = models.BooleanField(default=False)
    vehiculos_comerciales_pesados = models.BooleanField(default=False)
    accidentes_personales = models.BooleanField(default=False)
"""