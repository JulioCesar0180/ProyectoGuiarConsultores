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
    experiencia_empresa = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(500)])
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
    Tabla sobre la dotacion de la empresa
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


"""
Tabla sobre los procesos que puede tener una empresa
"""


class TablaProcesos(models.Model):
    nombre_proceso = models.CharField(max_length=100)
    orden = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.nombre_proceso


"""
Tabla sobre los procesos realizados por una empresa
"""


class TablaResultadosProcesos(models.Model):
    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    procesos = models.ManyToManyField(TablaProcesos)
    transporte = models.BooleanField(default=False)
    construccion = models.BooleanField(default=False)
    manufactura = models.BooleanField(default=False)
    servicios = models.BooleanField(default=False)


class TablaPoliza(models.Model):
    nombre_poliza = models.CharField(max_length=100)
    prioridad = models.IntegerField(default=99, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre_poliza


class TablaManejoRiesgos(models.Model):
    manejo_riesgo = models.CharField(max_length=150)
    cr = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    poliza = models.ForeignKey(TablaPoliza, null=True, on_delete=models.CASCADE)
    orden = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.manejo_riesgo


class TablaResultadosManejoRiesgo(models.Model):
    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    opciones_manejo = models.ManyToManyField(TablaManejoRiesgos)


class TablaTiempoPrevencionista(models.Model):
    tiempo_prevensionista = models.CharField(max_length=150)
    cr = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    poliza = models.ForeignKey(TablaPoliza, null=True, on_delete=models.CASCADE)
    orden = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.tiempo_prevensionista


class TablaResultadosTiempoPreven(models.Model):
    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    opciones_prevencionista_t = models.ForeignKey(TablaTiempoPrevencionista, on_delete=models.CASCADE, null=True)
'''
class TablaResultadosTransporte(models.Model):
    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)
    answer6 = models.BooleanField(default=False)
    answer7 = models.BooleanField(default=False)
    answer8 = models.BooleanField(default=False)
    answer9 = models.BooleanField(default=False)
'''


class TablaTransporte(models.Model):
    respuesta_transporte = models.CharField(max_length=200)
    ri = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    poliza = models.ForeignKey(TablaPoliza, null=True, on_delete=models.CASCADE)
    orden = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.respuesta_transporte


class TablaResultadosTransporte(models.Model):
    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    transporte = models.ManyToManyField(TablaTransporte)

'''
class TablaResultadosContruccion(models.Model):
    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)
    answer6 = models.BooleanField(default=False)
'''

class TablaConstruccion(models.Model):
    respuesta_construccion = models.CharField(max_length=200)
    ri = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    poliza = models.ForeignKey(TablaPoliza, null=True, on_delete=models.CASCADE)
    orden = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.respuesta_construccion


class TablaResultadosConstruccion(models.Model):
    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    construccion = models.ManyToManyField(TablaConstruccion)

'''
class TablaResultadosManufactura(models.Model):
    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)
    answer6 = models.BooleanField(default=False)
'''


class TablaManufactura(models.Model):
    respuesta_manufactura = models.CharField(max_length=200)
    ri = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    poliza = models.ForeignKey(TablaPoliza, null=True, on_delete=models.CASCADE)
    orden = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.respuesta_manufactura


class TablaResultadosManufactura(models.Model):
    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    manufactura = models.ManyToManyField(TablaManufactura)

'''
class TablaResultadosServicios(models.Model):
    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
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
'''


class TablaServicios(models.Model):
    respuesta_servicios = models.CharField(max_length=200)
    ri = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    poliza = models.ForeignKey(TablaPoliza, null=True, on_delete=models.CASCADE)
    orden = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.respuesta_servicios


class TablaResultadosServicios(models.Model):

    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    servicios = models.ManyToManyField(TablaServicios)


class TablaManiExplosivos(models.Model):
    tipo_exp = models.CharField(max_length=200)
    ri = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    poliza = models.ForeignKey(TablaPoliza, null=True, on_delete=models.CASCADE)
    orden = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.tipo_exp


class TablaResultadosManiExplosivos(models.Model):
    BOOL_CHOICES = ((True, 'Sí'), (False, 'No'))

    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    is_expo = models.BooleanField(default=False, choices=BOOL_CHOICES)
    tipos_exp = models.ManyToManyField(TablaManiExplosivos, blank=True, null=True)


class TablaElectricidad(models.Model):
    tipo_elec = models.CharField(max_length=200)
    ri = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    poliza = models.ForeignKey(TablaPoliza, null=True, on_delete=models.CASCADE)
    orden = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.tipo_elec


class TablaResultadoElectricidad(models.Model):
    BOOL_CHOICES = ((True, 'Sí'), (False, 'No'))

    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    is_elec = models.BooleanField(default=True, choices=BOOL_CHOICES)
    tipos_elec = models.ManyToManyField(TablaElectricidad, blank=True, null=True)


class TablaSustancias(models.Model):
    tipo_sust = models.CharField(max_length=200)
    ri = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    poliza = models.ForeignKey(TablaPoliza, null=True, on_delete=models.CASCADE)
    orden = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.tipo_sust


class TablaResultadosSustancias(models.Model):
    BOOL_CHOICES = ((True, 'Sí'), (False, 'No'))

    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    is_sust = models.BooleanField(default=False, choices=BOOL_CHOICES)
    tipos_sust = models.ManyToManyField(TablaSustancias, blank=True, null=True)


class TablaTrabajosAltura(models.Model):
    tipo_alt = models.CharField(max_length=200)
    ri = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    poliza = models.ForeignKey(TablaPoliza, null=True, on_delete=models.CASCADE)
    orden = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.tipo_alt


class TablaResultadosAltura(models.Model):
    BOOL_CHOICES = ((True, 'Sí'), (False, 'No'))

    id = models.OneToOneField(UserGuiar, on_delete=models.CASCADE, primary_key=True)
    is_alt = models.BooleanField(default=False, choices=BOOL_CHOICES)
    tipos_alt = models.ManyToManyField(TablaTrabajosAltura, blank=True, null=True)


class TablaDesignacionDotacion(models.Model):
    campo1 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(20)])
    campo2 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(20)])
    campo3 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(20)])
    campo4 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(20)])
    campo5 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(20)])
    campo6 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(20)])
    campo7 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(20)])
    campo8 = models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(20)])
    

class TablaTrabajosEspecificos(models.Model):
    trabajo = models.CharField(max_length=100)
    ri = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.trabajo