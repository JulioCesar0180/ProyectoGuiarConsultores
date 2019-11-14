from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import MinValueValidator, MaxValueValidator
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
    rut = models.CharField(max_length=12, verbose_name="Rut Empresa", primary_key=True, default="")
    name = models.CharField(max_length=100, verbose_name="Nombre Empresa", default="")
    address = models.CharField(max_length=100, verbose_name="Direccion", default="")
    is_admin = models.BooleanField(default=False)
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


"""
    Tabla de ventas Anuales de la empresa
"""


class TablaVentasAnuales(models.Model):
    ventas = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.ventas


"""
    Tabla del perfil de la empresa y su representante
"""


class TablaPerfilEmpresa(models.Model):
    # id generada por Django
    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)

    # Datos complementarios a la empresa
    experiencia_empresa = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    ciudad_empresa = models.CharField(max_length=20, default="")
    comuna_empresa = models.CharField(max_length=20, default="")
    razon_social_empresa = models.CharField(max_length=100, default="")
    ventas_anuales_empresa = models.ForeignKey(TablaVentasAnuales, on_delete=models.CASCADE, null=True, blank=True)

    # Datos del representante
    nombre_representante = models.CharField(max_length=50, default="")
    rut_representante = models.CharField(max_length=12)
    email_representante = models.EmailField(max_length=50, default="")
    telefono_representante = models.CharField(max_length=15, default="")


"""
    Tabla del perfil de la empresa y su representante
"""


class TablaResultadosDotacion(models.Model):
    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    cant_emp_contratados = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    cant_emp_contratista = models.IntegerField( default=0, validators=[MinValueValidator(0)])
    cant_veh_empresa = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    cant_veh_contratista = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    cant_veh_empresa_pesado = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    cant_veh_contratista_pesado = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    cant_maq_pesada_empresa = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    cant_maq_pesada_contratista = models.IntegerField(default=0, validators=[MinValueValidator(0)])