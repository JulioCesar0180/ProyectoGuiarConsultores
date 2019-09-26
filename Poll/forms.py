from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserGuiar


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

    class Meta:
        model = UserGuiar
        fields = ('rut', 'name', 'address')


class FormPageOne(forms.Form):
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))