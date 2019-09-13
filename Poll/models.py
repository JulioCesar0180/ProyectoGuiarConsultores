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
    name = models.CharField(max_length=100, verbose_name="Nombre", default="")
    address = models.CharField(max_length=100, verbose_name="Direccion", default="")
    is_admin = models.BooleanField(default=False)
    #password = models.CharField(max_length=10, verbose_name="Contraseña", default="")
    objects = UserGuiarManager()
    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['name']

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
