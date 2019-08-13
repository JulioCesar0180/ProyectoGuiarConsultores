from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .form_datos_personales import *
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

    return render(request,'Navbar/denunciar.html')


@login_required
def index(request):
    # codigo para la encuesta completa
    # nombre, email, telefono, razon, rut (empresa), experiencia, direccion, comuna, ciudad, ventas,
    if request.method == 'POST':
        form1 = FormInicial(request.POST)
        form2 = FormDefault(request.POST)
        context = {'perfil_usuario':form1, 'dotacion':form2}
        if form1.is_valid():
            if form2.is_valid():
                nombre = form1.cleaned_data['nombre']
                email = form1.cleaned_data['email']
                telefono = form1.cleaned_data['telefono']
                razon = form1.cleaned_data['razon']
                rut = form1.cleaned_data['rut']
                experiencia = form1.cleaned_data['experiencia']
                direccion = form1.cleaned_data['direccion']
                comuna = form1.cleaned_data['comuna']
                ciudad = form1.cleaned_data['ciudad']
                ventas = 200 # form.cleaned_data['ventas']
                usuario = Tabla_perfil_usuario(user=1,
                                               nombre_empresa=nombre,
                                               rut_empresa=rut,
                                               direccion_empresa=direccion,
                                               experiencia_empresa=experiencia,
                                               ciudad_empresa=ciudad,
                                               comuna_empresa=comuna,
                                               nombre_contacto_empresa='placeholder',
                                               telefono_empresa=telefono,
                                               email_empresa=email,
                                               ventas_anuales_empresa=ventas)
                usuario.save()
                # return HttpResponseRedirect('/thanks/')
                empContratados = form2.cleaned_data['empContratados']
                empContratistas = form2.cleaned_data['empContratistas']
                vehLivianos = form2.cleaned_data['vehLivianos']
                vehContratistas = form2.cleaned_data['vehContratistas']
                vehPesados = form2.cleaned_data['vehPesados']
                vehPesadosContratistas = form2.cleaned_data['vehPesadosContratistas']
                maqEmpresa = form2.cleaned_data['maqEmpresa']
                marContratista = form2.cleaned_data['marContratista']
                dotacion = Tabla_resultados_dotacion(user=1,
                                                     empContratados=empContratados,
                                                     empContratistas=empContratistas,
                                                     vehLivianos=vehLivianos,
                                                     vehContratistas=vehContratistas,
                                                     vehPesados=vehPesados,
                                                     vehPesadosContratistas=vehPesadosContratistas,
                                                     maqEmpresa=maqEmpresa,
                                                     marContratista=marContratista)
                dotacion.save()
            # hay problemas con el Form 2
        # hay problemas con el Form 1
    else:
        form1 = FormInicial()
        form2 = FormDefault()
        context = {'perfil_usuario':form1, 'dotacion':form2}
    return render(request, "MideTuRiesgo/mideturiesgo.html", context)

@login_required
def polltwo(request):
    return render(request, "MideTuRiesgo/mideturiesgo2.html")

@login_required
def pollthree(request):
    return render(request, "MideTuRiesgo/mideturiesgo3.html")

@login_required
def pollfour(request):
    return render(request, "MideTuRiesgo/mideturiesgo4.html")

def resultado(request):
    return render(request, "MideTuRiesgo/mideturiesgoresultado.html")

def profile(request):
    return render(request, "registration/profile.html")


def poll_page_one(request):
    form1 = form_datos_personales()
    form2 = form_datosGeneralesEmpresa()
    form3 = form_ventasEmpresa()
    context = {'datos_personales':form1, 'datos_empresa': form2, 'ventas_empresa': form3}
    return render(request, "MideTuRiesgo/mideturiesgo01.html", context)
