from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserGuiar
from .models import TablaPerfilEmpresa

class LogInForm(forms.Form):
    rut = forms.CharField(label='rut', widget=forms.TextInput(attrs={'placeholder': 'Rut de Empresa'}))
    password = forms.CharField(label='password', max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

    class Meta:
        model = UserGuiar
        fields = ('rut', 'password')


#Arreglarlo
class SignUpForm(UserCreationForm):
    rut = forms.CharField(
        max_length=30, required=False,
        help_text='required', label="Rut Empresa")

    name = forms.CharField(
        max_length=30, required=False,
        help_text='Optional.', label='Nombre Empresa')

    address = forms.CharField(
        max_length=254, label="Dirección")

    nombre_representante = forms.CharField(max_length=254, label="Nombre Representante")

    email_representante = forms.EmailField(max_length=40, label="Email Representante")

    telefono_representante = forms.CharField(max_length=9, label="Telefono Representante")

    class Meta:
        model = UserGuiar
        fields = ('rut', 'name', 'address')

class FormPageOne(forms.Form):
    attrs_nombre = {
        'class': 'form-control'
    }
    nombre = forms.CharField(label='Nombre Empresa', widget=forms.TextInput(attrs=attrs_nombre))

    # Razon Social de la empresa #
    attrs_razon = {
        'class': 'form-control'
    }
    razon = forms.CharField(label='Razón Social', widget=forms.TextInput(attrs=attrs_razon))

    # Rut de la empresa #
    attrs_rut = {
        'class': 'form-control'
    }
    rut = forms.CharField(label='Rut', widget=forms.TextInput(attrs=attrs_rut))

    # Años de Experiencia de la empresa #
    attrs_experiencia = {
        'class': 'form-control'
    }
    experiencia = forms.IntegerField(label='Antigüedad de la empresa (años)',
                                     widget=forms.TextInput(attrs=attrs_experiencia))

    # Direccion de la empresa #
    attrs_direccion = {
        'class': 'form-control'
    }
    direccion = forms.CharField(label='Dirección', widget=forms.TextInput(attrs=attrs_direccion))

    # Comuna de la empresa #
    attrs_comuna = {
        'class': 'form-control'
    }
    comuna = forms.CharField(label='Comuna', widget=forms.TextInput(attrs=attrs_comuna))

    # Ciudad de la empresa #
    attrs_ciudad = {
        'class': 'form-control'
    }
    ciudad = forms.CharField(label='Ciudad', widget=forms.TextInput(attrs=attrs_ciudad))
    representante = forms.CharField(label='Representante', max_length=100)
    email = forms.CharField(label='Correo', max_length=100)
    telefono = forms.CharField(label='Telefono', max_length=100)
    ventas = forms.CharField(label="Ventas", max_length=100)
    empContratados = forms.IntegerField(label="Cantidad de empleados contratados")
    empContratistas = forms.IntegerField(label="Cantidad de empleados contratistas")
    vehLivianos = forms.IntegerField(label="Cantidad de vehiculos livianos")
    vehContratistas = forms.IntegerField(label='Cantidad de vehículos comerciales de contratistas')
    vehPesados = forms.IntegerField(label='Cantidad de vehículos comerciales pesados de la empresa')
    vehPesadosContratistas = forms.IntegerField(label='Cantidad de vehículos comerciales pesados de contratistas')
    maqEmpresa = forms.IntegerField(label='Cantidad de maquinaria pesada de la empresa')
    marContratista = forms.IntegerField(label='Cantidad de maquinaria pesada de contratista')



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

class FormPageTwo(forms.Form):
    campo1 = forms.CharField(label='Placeholder', max_length=100)

class FormPageThree(forms.Form):
    campo1 = forms.CharField(label='Placeholder', max_length=100)

class FormPageFour(forms.Form):
    campo1 = forms.CharField(label='Placeholder', max_length=100)