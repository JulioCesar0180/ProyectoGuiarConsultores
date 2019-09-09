from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    nombre_de_empresa = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'nombre_de_empresa', 'last_name', 'email', 'password1', 'password2', )


class FormInicial(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=100)
    razon = forms.CharField(max_length=100)
    rut = forms.CharField(max_length=100)
    experiencia = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)
    comuna = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=100)
    # ventas = forms.BooleanField(required=False)
    message = forms.CharField(widget=forms.Textarea)


class FormDefault(forms.Form):
    placeholder = forms.CharField()


class Form_datosPersonales(forms.Form):
    attrs_nombre = {
        'class': 'form-control',
        'id': 'form-texbox'
    }

    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs=attrs_nombre))

    attrs_email = {
        'class': 'form-control'
    }
    email = forms.EmailField(label='Correo Electronico', widget=forms.EmailInput(attrs=attrs_email))

    attrs_telefono = {
        'class': 'form-control'
    }
    telefono = forms.CharField(label='Teléfono', widget=forms.TextInput(attrs=attrs_telefono))


class Form_datosEmpresa(forms.Form):
    attrs_razon = {
        'class': 'form-control'
    }
    razon = forms.CharField(label='Razón Social', widget=forms.TextInput(attrs=attrs_razon))

    attrs_rut = {
        'class': 'form-control'
    }
    rut = forms.CharField(label='Rut', widget=forms.TextInput(attrs=attrs_rut))

    attrs_experiencia = {
        'class': 'form-control'
    }
    experiencia = forms.IntegerField(label='Antigüedad de la empresa (años)',
            widget=forms.TextInput(attrs=attrs_experiencia))

    attrs_direccion = {
        'class': 'form-control'
    }
    direccion = forms.CharField(label='Dirección', widget=forms.TextInput(attrs=attrs_direccion))

    attrs_comuna = {
        'class': 'form-control'
    }
    comuna = forms.CharField(label='Comuna', widget=forms.TextInput(attrs=attrs_comuna))

    attrs_ciudad = {
        'class': 'form-control'
    }
    ciudad = forms.CharField(label='Ciudad', widget=forms.TextInput(attrs=attrs_ciudad))


class Form_ventasEmpresa(forms.Form):
    CHOICE = [('1', 'De UF 0 a UF 2.400'),
              ('2', 'De UF 2.400 a UF 25.000'),
              ('3', 'De UF 25.000 a UF 100.000'),
              ('4', 'Más de UF 100.000')]
    attrs_ventas = {'class': 'form-check-input'}
    ventas = forms.MultipleChoiceField(choices=CHOICE, widget=forms.CheckboxInput())


class Form_dotacionEmpresa(forms.Form):
    empContratados = forms.CharField(
        label='Cantidad de empleados contratados',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'off'
        })
    )

    empContratistas = forms.CharField(
        label='Cantidad de empleados contratistas',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'off'
        })
    )

    vehLivianos = forms.CharField(
        label='Cantidad de vehículos comerciales livianos de la empresa',
        widget=forms.TextInput(attrs={
            'class': 'form-control',

        })
    )

    vehContratistas = forms.CharField(
        label='Cantidad de vehículos comerciales de contratistas'
    )
    vehPesados = forms.IntegerField(
        label='-'
    )
    vehPesadosContratistas = forms.IntegerField(
        label='-'
    )
    maqEmpresa = forms.IntegerField(
        label='-'
    )
    marContratista = forms.IntegerField(
        label='-'
    )


class Form_rubroEmpresa(forms.Form):
    CHOICE = [('1', 'Contrucción'),
              ('2', 'Manufactura'),
              ('3', 'Transporte terrestre'),
              ('4', 'Servicios Generales'),
              ('5', 'Otro (por favor especifique')]
    rubro = forms.ChoiceField(widget=forms.RadioSelect(choices=CHOICE))

"""

    
    rubro = forms.MultipleChoiceField(choices=CHOICE, widget=forms.RadioSelect())

    attrs_otro = {'class': 'form-control'}
    otro = forms.CharField(widget=forms.TextInput(attrs=attrs_otro))
    """


class Form_elementosRiesgo(forms.Form):
    CHOICE = [('1', 'Ingeniería, contrucción o fabricación de estructuras metálicas'),
              ('2', 'Ingeniería o construcción de edificios, obra gruesa, concreto, carreteras'),
              ('3', 'Ingeniería, construcción o montaje de obras e instalaciones privadas o públicas'),
              ('4', 'Obras menores de construcción, contratistas, albañería, carpintería, climatización'),
              ('5', 'Instalación de tuberías y construcción de alcantarrillado, base de concreto y obras de cimentación, exacavación'),
              ('6', 'Refuerzos, reparación y protección de estructuras de acero, reparación de estanques, impermeabilización, protección catódica'),
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
              ('4', 'Mantención, reparación y montaje de generadores, transformadores eléctricos, alta tensión, líneas'),
              ('5', 'Mantención, reparación y montaje de piezas, repuestos, partes de equipo de extracción minera, industrial'),
              ('6', 'Mantención, reparación y montaje de sistemas hidráulicos, válvulas, compresores, bombas, otros'),
              ('7', 'Mantención, reparación y venta de equipos computacionales, software, adware'),
              ('8', 'Servicio de lavandería industrial y afines'),
              ('9', 'Servicio de movimiento de tierras, perforaciones, mecánicas de rocas'),
              ('10', 'Servicio y arriendo de equipo minero, perforaciones, movimiento de tierras, maquinaria pesada'),
              ('11', 'Servicio de abastecimiento de herramientas, maquinarias menores, ferretería, materiales de construcción'),
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