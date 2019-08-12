from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, FormInicial
from Poll.models import Tabla_perfil_usuario


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



def index(request):
    # codigo para la encuesta completa
    # nombre, email, telefono, razon, rut (empresa), experiencia, direccion, comuna, ciudad, ventas,
    if request.method == 'POST':
        form = FormInicial(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            razon = form.cleaned_data['razon']
            rut = form.cleaned_data['rut']
            experiencia = form.cleaned_data['experiencia']
            direccion = form.cleaned_data['direccion']
            comuna = form.cleaned_data['comuna']
            ciudad = form.cleaned_data['ciudad']
            ventas = form.cleaned_data['ventas']
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
    else:
        form = FormInicial()
    return render(request, "MideTuRiesgo/mideturiesgo.html", {'form': form})


def polltwo(request):
    # nombre = request.get('nombre')
    # nombre = request('nombre')
    if request.method == 'POST':
        form = FormInicial(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            razon = form.cleaned_data['razon']
            rut = form.cleaned_data['rut']
            experiencia = form.cleaned_data['experiencia']
            direccion = form.cleaned_data['direccion']
            comuna = form.cleaned_data['comuna']
            ciudad = form.cleaned_data['ciudad']
            ventas = form.cleaned_data['ventas']
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
    else:
        form = FormInicial()
    return render(request, "MideTuRiesgo/mideturiesgo2.html", {'form': form})

def pollthree(request):
    return render(request, "MideTuRiesgo/mideturiesgo3.html")

def pollfour(request):
    return render(request, "MideTuRiesgo/mideturiesgo4.html")

def profile(request):
    return render(request, "registration/profile.html")


