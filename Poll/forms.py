from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import *

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
FormUserGuiar
-------------------------------------------------------------------------------------------------------
"""
""" Formulario relacionado con UserGuiar """


class FormUserGuiar(ModelForm):
    class Meta:
        model = UserGuiar
        fields = [
            'rut',  # Rut de la empresa
            'name',  # Nombre de la empresa
            'address'  # Direccion de la empresa
        ]

        labels = {
            'rut': 'Rut de la empresa',
            'name': 'Nombre',
            'address': 'Dirección'
        }

        exclude = [
            'name',
            'password',
            'is_admin',
            'is_superuser',
            'groups',
            'last_login',
            'user_permissions'
        ]

        widgets = {
            'rut': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }


""" 
---------------------------------------------------------------------------------------------------
FormTablaPerfilEmpresa
-------------------------------------------------------------------------------------------------------
"""
""" Formulario relacionado con la TablaPerfilEmpresa """


class FormTablaPerfilEmpresa(ModelForm):

    # Como ventas anuales puede ser null, mediante el formulario se fuerza a tener un valor
    def __init__(self, *args, **kwargs):
        super(FormTablaPerfilEmpresa, self).__init__(*args, **kwargs)
        self.fields['ventas_anuales_empresa'].required = True

    class Meta:
        model = TablaPerfilEmpresa
        fields = (
            'experiencia_empresa',
            'ciudad_empresa',
            'comuna_empresa',
            'razon_social_empresa',
            'ventas_anuales_empresa',
            'nombre_representante',
            'rut_representante',
            'email_representante',
            'telefono_representante',
        )

        labels = {
            'experiencia_empresa': 'Antigüedad de la empresa',
            'ciudad_empresa': 'Ciudad',
            'comuna_empresa': 'Comuna',
            'razon_social_empresa': 'Razon Social',
            'ventas_anuales_empresa': 'Ventas Anuales de la Empresa',
            'nombre_representante': 'Nombre',
            'rut_representante': 'Rut',
            'email_representante': 'Correo Electronico',
            'telefono_representante': 'Teléfono'
        }

        exclude = [
            'id'
        ]

        widgets = {
            'experiencia_empresa': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'ciudad_empresa': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'comuna_empresa': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'razon_social_empresa': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'ventas_anuales_empresa': forms.RadioSelect,
            'nombre_representante': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'rut_representante': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email_representante': forms.EmailInput(attrs={
                'class': 'form-control',
            }),
            'telefono_representante': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }


class FormTablaResultadosDotacion(ModelForm):

    class Meta:
        model = TablaResultadosDotacion
        fields = [
            'cant_emp_contratados',
            'cant_emp_contratista',
            'cant_veh_empresa',
            'cant_veh_contratista',
            'cant_veh_empresa_pesado',
            'cant_veh_contratista_pesado',
            'cant_maq_pesada_empresa',
            'cant_maq_pesada_contratista',
        ]
        labels = {
            'cant_emp_contratados': 'Cantidad de empleados contratados',
            'cant_emp_contratista': 'Cantidad de empleados contratistas',
            'cant_veh_empresa': 'Cantidad de vehículos comerciales livianos de la empresa',
            'cant_veh_contratista': 'Cantidad de vehículos comerciales de contratistas',
            'cant_veh_empresa_pesado': 'Cantidad de vehículos comerciales pesados de la empresa',
            'cant_veh_contratista_pesado': 'Cantidad de vehículos comerciales pesados de contratistas',
            'cant_maq_pesada_empresa': 'Cantidad de maquinaria pesada de la empresa',
            'cant_maq_pesada_contratista': 'Cantidad de maquinaria pesada de contratista',
        }
        exclude = [
            'id'
        ]
        widgets = {
            'cant_emp_contratados': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'cant_emp_contratista': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'cant_veh_empresa': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'cant_veh_contratista': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'cant_veh_empresa_pesado': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'cant_veh_contratista_pesado': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'cant_maq_pesada_empresa': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'cant_maq_pesada_contratista': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }


class FormTablaResultadosProcesos(ModelForm):

    class Meta:
        model = TablaResultadosProcesos
        fields = [
            'procesos'
        ]

        widgets = {
            'procesos': forms.CheckboxSelectMultiple
        }