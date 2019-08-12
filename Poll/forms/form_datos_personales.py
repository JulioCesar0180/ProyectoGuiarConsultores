from django import forms


class form_datos_personales(forms.Form):
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'placeholder': ''}))
    email = forms.EmailField(label='Correo Electronico', max_length=30, widget=forms.EmailInput(attrs={'placeholder': ''}))
    telefono = forms.IntegerField(label='Teléfono', max_value=8, widget=forms.NumberInput())


class form_datosGeneralesEmpresa(forms.Form):
    razon_social = forms.CharField(label='Razon Social', widget=forms.TextInput())
    rut = forms.CharField(label='Rut', widget=forms.TextInput())
    antiguedad = forms.IntegerField(label='Antigüedad de la empresa', widget=forms.TextInput())
    direccion = forms.CharField(label='Direccion', widget=forms.TextInput())
    comuna = forms.CharField(label='Comuna', widget=forms.TextInput())
    ciudad = forms.CharField(label='Ciudad', widget=forms.TextInput())

