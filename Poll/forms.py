from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

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