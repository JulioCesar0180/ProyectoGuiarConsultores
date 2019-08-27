from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .forms import *
from Poll.models import *
from django.contrib.auth.decorators import login_required


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def denunciar(request):
    return render(request, 'Navbar/denunciar.html')


@login_required
def page_one_poll(request):
    form1 = Form_datosPersonales()
    form2 = Form_datosEmpresa()
    if request.method == 'POST':
        form1 = Form_datosPersonales(request.POST)
        form2 = Form_datosEmpresa(request.POST)
        if form1.is_valid() and form2.is_valid():

            #obtener datos de Datos Personales
            nombre = form1.cleaned_data['nombre']
            email = form1.cleaned_data['email']
            telefono = form1.cleaned_data['telefono']

            #obtener datos de la Empresa
            razon_social = form2.cleaned_data['razon']
            rut = form2.cleaned_data['rut']
            experiencia = form2.cleaned_data['experiencia']
            direccion = form2.cleaned_data['direccion']
            comuna = form2.cleaned_data['comuna']
            ciudad = form2.cleaned_data['ciudad']

            #Se crea el objeto
            datosPersonales = Tabla_perfil_usuario(
                user_id=request.user.id,
                nombre_empresa=nombre,
                rut_empresa=rut,
                direccion_empresa=direccion,
                experiencia_empresa=experiencia,
                ciudad_empresa=ciudad,
                comuna_empresa=comuna,
                nombre_contacto_empresa="NULL",
                telefono_empresa=telefono,
                email_empresa=email,
                razon_social_empresa=razon_social,
                ventas_anuales_empresa="15.000"
            )

            datosPersonales.save()

            #Volver a la pagina de Inicio por el momento
            return render(request, "home/home.html")

    context = \
        {'datos_personales': form1,
         'datos_empresa': form2,
         }
    return render(request, "MideTuRiesgo/mideturiesgo01.html", context)
