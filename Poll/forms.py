from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserGuiar
from .models import TablaPerfilEmpresa

# datos para el drop down
Ciudad_CHOICES = [
    ('antofagasta', 'Antofagasta'),
    ('calama', 'Calama'),
    ('mejillones', 'Mejillones'),
    ('tocopilla', 'Tocopilla'),
]

Comuna_CHOICES = [
    ('antofagasta', 'Antofagasta'),
    ('el loa', 'El Loa'),
    ('mejillones', 'Mejillones'),
    ('tocopilla', 'Tocopilla'),
]


class UpdateForm(forms.Form):
    rut = forms.CharField(
        max_length=30, required=True,
        help_text='Obligatorio', label="Rut Empresa")

    name = forms.CharField(
        max_length=30, required=True,
        help_text='Obligatorio.', label='Nombre Empresa')

    address = forms.CharField(
        max_length=254, label="Dirección")

    nombre_representante = forms.CharField(max_length=254, required=True, label="Nombre Representante")

    email_representante = forms.EmailField(max_length=40, required=True, help_text='Obligatorio.',
                                           label="Email Representante")

    telefono_representante = forms.CharField(max_length=9, required=True, help_text='Obligatorio.',
                                             label="Telefono Representante")

    ciudad_empresa = forms.CharField(label='Ciudad de la Empresa',
                                     widget=forms.Select(choices=Ciudad_CHOICES))

    comuna_empresa = forms.CharField(label='Ciudad de la Empresa',
                                     widget=forms.Select(choices=Ciudad_CHOICES))

    razon_social_empresa = forms.CharField(max_length=254, label="Razón Social de la Empresa")

    ventas_anuales_empresa = forms.CharField(max_length=254, label="Ventas Anuales de la Empresa")

    experiencia_empresa = forms.CharField(max_length=254, label="Experiencia de la Empresa")


class LogInForm(forms.Form):
    rut = forms.CharField(label='Rut Empresa', widget=forms.TextInput(attrs={'placeholder': 'Ingrese Rut de Empresa'}))
    password = forms.CharField(label='Contraseña', max_length=30,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese Contraseña'}))

    class Meta:
        model = UserGuiar
        fields = ('rut', 'password')


# Arreglarlo
class SignUpForm(UserCreationForm):
    rut = forms.CharField(
        max_length=30, required=True,
        help_text='required', label="Rut Empresa")

    name = forms.CharField(
        max_length=30, required=True,
        help_text='Optional.', label='Nombre Empresa')

    address = forms.CharField(
        max_length=254, label="Dirección")

    nombre_representante = forms.CharField(max_length=254, label="Nombre Representante")

    email_representante = forms.EmailField(max_length=40, label="Email Representante")

    telefono_representante = forms.CharField(max_length=9, label="Telefono Representante")

    class Meta:
        model = UserGuiar
        fields = ('rut', 'name', 'address')


""" 
---------------------------------------------------------------------------------------------------
FormPageOne 
-------------------------------------------------------------------------------------------------------
"""
""" Formulario de la primera pagina de la encuesta de la aplicacion """


class FormPageOne(forms.Form):
    """
    Datos de la empresa
    """
    """
    Razon social de la empresa, por ejemplo: GuiarConsultores S.A
    """
    razon_social = forms.CharField(
        # validations
        max_length=50,
        required=True,
        widget=forms.TextInput(
            # attributes HTML
            attrs={
                'id': 'razon_social',
                'class': 'form-control',
            }
        ))
    """
    Rut de la empresa, por ejemplo 12345678-5
    """
    rut = forms.CharField(
        # validations
        max_length=15,
        required=True,
        widget=forms.TextInput(
            # attributes HTML
            attrs={
                'id': 'rut',
                'class': 'form-control',
            }
        )
    )
    """
    Años de experiencia de la empresa, por ejemplo: 10
    """
    experiencia = forms.IntegerField(
        # validations
        max_value=1000,
        min_value=0,
        required=True,
        # attribute HTML
        widget=forms.NumberInput(
            attrs={
                'id': 'experiencia',
                'class': 'form-control',
            }
        )
    )
    """
    Direccion de la empresa, por ejemplo: Avenida Angamos 0610
    """
    direccion = forms.CharField(
        # validations
        max_length=100,
        required=True,
        # attributes HTML
        widget=forms.TextInput(
            attrs={
                'id': 'direccion',
                'class': 'form-control',
            }
        )
    )
    """
    Comuna donde se ubica la empresa, por ejemplo: Providencia
    """
    comuna = forms.CharField(
        # validations
        max_length=50,
        required=True,
        # attributes HTML
        widget=forms.TextInput(
            attrs={
                'id': 'comuna',
                'class': 'form-control',
            }
        )
    )
    """
    Ciudad donde se ubica la empresa, por ejemplo: Santiago
    """
    ciudad = forms.CharField(
        # validations
        max_length=50,
        required=True,
        # attributes HTML
        widget=forms.TextInput(
            attrs={
                'id': 'ciudad',
                'class': 'form-control',
            }
        )
    )

    """
    Datos del representante
    """

    """
    Nombre del representante, por ejemplo: Diego Cuevas
    """
    nombre_representante = forms.CharField(
        # validations
        max_length=50,
        required=True,
        # attributes HTML
        widget=forms.TextInput(
            attrs={
                'id': 'nombre',
                'class': 'form-control',
            }
        )
    )
    """
    Email del representante, por ejemplo: JoanTello@GuiarConsultores.cl
    """
    email_representante = forms.EmailField(
        # validations
        max_length=50,
        required=True,
        # attributes HTML
        widget=forms.EmailInput(
            attrs={
                'id': 'email',
                'class': 'form-control'
            }
        )
    )
    """
    Telefono de contacto con el representante, por ejemplo: 994512290
    """
    telefono_representante = forms.CharField(
        # validations
        max_length=9,
        min_length=9,
        required=True,
        # attributes
        widget=forms.NumberInput(
            attrs={
                'id': 'telefono',
                'class': 'form-control',
            }
        )
    )
    """
    Ventas anuales empresa
    """
    # Radio
    CHOICES_VENTAS_ANUALES = [
        ('minimo', 'De UF 0 a UF 2.400'),
        ('intermedio', 'De UF 2.400 a UF 25.000'),
        ('maximo', 'De UF 25.000 a UF 100.000'),
        ('extra_maximo', 'Más de UF 100.000')
    ]

    ventas_anuales = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES_VENTAS_ANUALES)
    """
    Dotacion Empresa
    """
    """
    Cantidad de empleados contratados, por ejemplo: 10
    """
    empContratados = forms.IntegerField(
        # validations
        min_value=0,
        max_value=10000000,
        required=True,
        # attributes HTML
        widget=forms.NumberInput(
            attrs={
                'id': 'empContratados',
                'class': 'form-control',
            }
        )
    )
    """
    Cantidad de empleados contratistas, por ejemplo: 10
    """
    empContratistas = forms.IntegerField(
        # validations
        min_value=0,
        max_value=10000000,
        required=True,
        # attributes HTML
        widget=forms.NumberInput(
            attrs={
                'id': 'empContratistas',
                'class': 'form-control',
            }
        )
    )
    """
    Cantidad de vehiculos comerciales livianos de la empresa, por ejemplo: 10
    """
    vehLivianos = forms.IntegerField(
        # validations
        min_value=0,
        max_value=10000000,
        required=True,
        # attributes HTML
        widget=forms.NumberInput(
            attrs={
                'id': 'vehLivianos',
                'class': 'form-control',
            }
        )
    )
    """
    Cantidad de vehiculos comerciales de contratistas, por ejemplo: 10
    """
    vehContratistas = forms.IntegerField(
        # validations
        min_value=0,
        max_value=10000000,
        required=True,
        # attributes HTML
        widget=forms.NumberInput(
            attrs={
                'id': 'vehContratistas',
                'class': 'form-control',
            }
        )
    )
    """
    Cantidad de vehiculos comerciales pesados de la empresa, por ejemplo: 10
    """
    vehPesados = forms.IntegerField(
        # validations
        min_value=0,
        max_value=10000000,
        required=True,
        # attributes HTML
        widget=forms.NumberInput(
            attrs={
                'id': 'vehPesados',
                'class': 'form-control',
            }
        )
    )
    """
    Cantidad de vehiculos comerciales pesados de contratistas, por ejemplo: 10
    """
    vehPesadosContratistas = forms.IntegerField(
        # validations
        min_value=0,
        max_value=10000000,
        required=True,
        # attributes HTML
        widget=forms.NumberInput(
            attrs={
                'id': 'vehPesadosContratistas',
                'class': 'form-control',
            }
        )
    )
    """
    Cantidad de maquinaria pesada de la empresa, por ejemplo: 10
    """
    maqEmpresa = forms.IntegerField(
        # validations
        min_value=0,
        max_value=10000000,
        required=True,
        # attributes HTML
        widget=forms.NumberInput(
            attrs={
                'id': 'maqEmpresa',
                'class': 'form-control',
            }
        )
    )
    """
    Cantidad de maquinaria pesada de contratista
    """
    maqContratista = forms.IntegerField(
        # validations
        min_value=0,
        max_value=10000000,
        required=True,
        # attributes HTML
        widget=forms.NumberInput(
            attrs={
                'id': 'maqContratista',
                'class': 'form-control',
            }
        )
    )
    """
    Rubro de la empresa
    """
    # Checkbox (una o mas de una)
    CHOICES_RUBRO = [
        ('construccion', 'contruccion'),
        ('manufactura', 'manufactura'),
        ('transporte terrestre', 'transporte_terrestre'),
        ('servicios generales', 'servicios generales')
    ]

    rubro_empresa = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=CHOICES_RUBRO)


class Form_elementosRiesgo(forms.Form):
    CHOICE = [('1', 'Ingeniería, contrucción o fabricación de estructuras metálicas'),
              ('2', 'Ingeniería o construcción de edificios, obra gruesa, concreto, carreteras'),
              ('3', 'Ingeniería, construcción o montaje de obras e instalaciones privadas o públicas'),
              ('4', 'Obras menores de construcción, contratistas, albañería, carpintería, climatización'),
              ('5',
               'Instalación de tuberías y construcción de alcantarrillado, base de concreto y obras de cimentación, exacavación'),
              ('6',
               'Refuerzos, reparación y protección de estructuras de acero, reparación de estanques, impermeabilización, protección catódica'),
              ('7', 'Otros')]

    attrs_otro = {'class': 'form-control'}
    otro = forms.CharField(widget=forms.TextInput(attrs=attrs_otro))


class Form_actManufaturas(forms.Form):
    CHOICE = [('1', 'Producción, procesamiento y conservación de alimentos, casinos, abastecimientos alimenticios'),
              ('2', 'Confección, fabricación y distribución de prendas de vestir, seguridad, zapatos'),
              ('3', 'Diseño y fabricación de piezas especiales menores, tornerías, otros'),
              ('4', 'Diseño y fabricación de piezas especiales mayores, PVC, acero, otros'),
              ('5', 'Diseño y fabricación de muebles para acondicionamiento de oficinas y faenas'),
              ('6', 'Diseño y fabricación de prototipos industriales y mineros'),
              ('7', 'Otros')]

    attrs_otros = {'class': 'form-control'}
    otro = forms.CharField(widget=forms.TextInput(attrs=attrs_otros))


class Form_tipoCargas(forms.Form):
    CHOICE = [('1', 'Materiales diversos de construcción, repuestos, otros'),
              ('2', 'Personas, trabajadores propios o terceros'),
              ('3', 'Maquinaria pesada, motores, vehículos, equipo minero'),
              ('4', 'Mercadería de alimentos, medicinales'),
              ('5', 'Minerales a granel'),
              ('6', 'Minerales sólidos'),
              ('7', 'Materiales corrosivos, tóxicos, residuos peligrosos'),
              ('8', 'Aceites, lubricantes aditivos'),
              ('9', 'Carga sobredimensionada, estructuras, piezas y/o partes, equipo minero'),
              ('10', 'otro')]

    attrs_otros = {'class': 'form-control'}
    otro = forms.CharField(widget=forms.TextInput(attrs=attrs_otros))


class Form_serviciosGenerales(forms.Form):
    CHOICE = [('1', 'Maestranza de maquinarias, equipos y componentes, repuestos de vehículos con/sin motor'),
              ('2', 'Maestranza, reparación y fabricación de piezas y/o partes mecanicas, industriales y mineras'),
              ('3', 'Mantención y reparación de componentes eléctricos'),
              (
              '4', 'Mantención, reparación y montaje de generadores, transformadores eléctricos, alta tensión, líneas'),
              ('5',
               'Mantención, reparación y montaje de piezas, repuestos, partes de equipo de extracción minera, industrial'),
              ('6', 'Mantención, reparación y montaje de sistemas hidráulicos, válvulas, compresores, bombas, otros'),
              ('7', 'Mantención, reparación y venta de equipos computacionales, software, adware'),
              ('8', 'Servicio de lavandería industrial y afines'),
              ('9', 'Servicio de movimiento de tierras, perforaciones, mecánicas de rocas'),
              ('10', 'Servicio y arriendo de equipo minero, perforaciones, movimiento de tierras, maquinaria pesada'),
              ('11',
               'Servicio de abastecimiento de herramientas, maquinarias menores, ferretería, materiales de construcción'),
              ('12', 'Servicios de fabricación e instalación de señaleticas en carreteras y/o caminos privados'),
              ('13', 'Servicios de izajes, manipulación de cargas y equipos'),
              ('14', 'Servicios de mantención, reparación, garage, desabollada, vehículos, multi-marca')]


class Form_certificacionesEmpresa(forms.Form):
    CHOICE = [('1', 'ISO 9.001'),
              ('2', 'ISO 14.001'),
              ('3', 'OHSAS 18.001'),
              ('4', 'Otro (Por favor especifique')]

    attrs_otros = {'class': 'form-control'}
    otro = forms.CharField(widget=forms.TextInput(attrs=attrs_otros))


class Form_elementosManejoRiesgos(forms.Form):
    CHOICE = [('1', 'Procedimiento de autocuidado, trabajo seguro, medidas preventivas y/o correctivas'),
              ('2', 'Asesoría de mutualidades'),
              ('3', 'Gerencia/Administración de riesgos (ISO 31.000:2009')]


class Form_jornadaPrevencionista(forms.Form):
    CHOICE = [('1', 'Tiempo Completo'),
              ('2', 'Tiempo Parcial o Part-time'),
              ('3', 'Para proyectos específicos'),
              ('4', 'No cuenta con prevencionista de riesgos')]


class FormPageTwo(forms.Form):
    campo1 = forms.CharField(label='Placeholder', max_length=100)


class FormPageThree(forms.Form):
    campo1 = forms.CharField(label='Placeholder', max_length=100)


class FormPageFour(forms.Form):
    campo1 = forms.CharField(label='Placeholder', max_length=100)
