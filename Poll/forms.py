from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import *

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
        help_text='Requerido', label="Rut Empresa",
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el RUT de Empresa'}))

    name = forms.CharField(
        max_length=30, required=True,
        help_text='Requerido', label='Nombre Empresa',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el Nombre de la Empresa'}))

    nombre_representante = forms.CharField(max_length=254, label="Nombre de Contacto", help_text='Requerido',
                                           widget=forms.TextInput(attrs={'placeholder': 'Ejemplo: Pedro Herrera'}))

    email_representante = forms.EmailField(max_length=40, label="Email de Contacto", help_text='Requerido',
                                           widget=forms.TextInput(
                                               attrs={'placeholder': 'Ejemplo: example@dominio.cl'}))

    telefono_representante = forms.CharField(max_length=9, label="Número de Contacto (+56)", help_text='Requerido',
                                             widget=forms.TextInput(
                                                 attrs={'placeholder': 'Ejemplo: 955555555'}))

    address = forms.CharField(
        max_length=254, label="Dirección", help_text='Requerido',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la Dirección de la Empresa'}))

    password1 = forms.CharField(label='Contraseña', max_length=30, help_text='Requerido',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese una Contraseña'}))

    password2 = forms.CharField(label='Confirmar Contraseña', max_length=30, help_text='Requerido',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese la Contraseña nuevamente'}))

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


class FormTablaResultadosCertificaciones(ModelForm):

    class Meta:
        model = TablaResultadosCertificaciones
        fields = [
            'certificaciones',
        ]

        widgets = {
            'certificaciones': forms.CheckboxSelectMultiple
        }


class FormTablaResultadosManejoRiesgo(ModelForm):

    class Meta:
        model = TablaResultadosManejoRiesgo
        fields = [
            'opciones_manejo'
        ]

        widgets = {
            'opciones_manejo': forms.CheckboxSelectMultiple
        }


class FormTablaResultadosTiempoPreven(ModelForm):

    def __init__(self, *args, **kwargs):
        super(FormTablaResultadosTiempoPreven, self).__init__(*args, **kwargs)
        self.fields['opciones_prevencionista_t'].required = True

    class Meta:
        model = TablaResultadosTiempoPreven
        fields = [
            'opciones_prevencionista_t'
        ]

        widgets = {
            'opciones_prevencionista_t': forms.RadioSelect
        }


class FormTablaResultadosTransporte(ModelForm):

    class Meta:
        model = TablaResultadosTransporte
        fields = [
            'transporte'
        ]

        widgets = {
            'transporte': forms.CheckboxSelectMultiple
        }


class FormTablaResultadosConstruccion(ModelForm):

    class Meta:
        model = TablaResultadosConstruccion
        fields = [
            'construccion'
        ]

        widgets = {
            'construccion': forms.CheckboxSelectMultiple
        }


class FormTablaResultadosManufactura(ModelForm):

    class Meta:
        model = TablaResultadosManufactura
        fields = [
            'manufactura'
        ]

        widgets = {
            'manufactura': forms.CheckboxSelectMultiple
        }


class FormTablaResultadosServicios(ModelForm):

    class Meta:
        model = TablaResultadosServicios
        fields = [
            'servicios'
        ]

        widgets = {
            'servicios': forms.CheckboxSelectMultiple
        }


class FormTablaResultadosManiExplosivos(ModelForm):

    class Meta:
        model = TablaResultadosManiExplosivos

        fields = [
            'is_expo',
            'tipos'
        ]

        widgets = {
            'tipos': forms.CheckboxSelectMultiple,
            'is_expo': forms.RadioSelect
        }


class FormTablaResultadoElectricidad(ModelForm):

    class Meta:
        model = TablaResultadoElectricidad

        fields = [
            'is_elec',
            'tipos'
        ]

        widgets = {
            'tipos': forms.CheckboxSelectMultiple,
            'is_elec': forms.RadioSelect
        }

    def is_valid(self):
        return True


class FormTablaResultadosSustancias(ModelForm):

    class Meta:
        model = TablaResultadosSustancias

        fields = [
            'is_sust',
            'tipos'
        ]

        widgets = {
            'tipos': forms.CheckboxSelectMultiple,
            'is_sust': forms.RadioSelect
        }

    def is_valid(self):
        return True


class FormTablaResultadosAltura(ModelForm):

    class Meta:
        model = TablaResultadosAltura

        fields = [
            'is_alt',
            'tipos'
        ]

        widgets = {
            'tipos': forms.CheckboxSelectMultiple,
            'is_alt': forms.RadioSelect
        }

    def is_valid(self):
        return True