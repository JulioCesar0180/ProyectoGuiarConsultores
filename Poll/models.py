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
    REQUIRED_FIELDS = ['name', 'address', 'is_admin']

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
    