# encoding: utf-8

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .models import UserGuiar
from .forms import *
from Poll.models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string

from django.contrib import messages

#rut
from django import template


def home(request):
    count = UserGuiar.objects.count()
    name = request.user.name
    return render(request, 'home.html', {
        'count': count, 'name': name
    })


def MTR_login(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data["password"]
            user = authenticate(username=rut, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'No existen registros de este usuario')
        else:
            return render(request, 'vips/login.html', {'form': form})

    form = LogInForm()
    return render(request, 'registration/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #form.save()
            username = form.cleaned_data.get('username')
            #username = rut_format(username, ".")
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def denunciar(request):
    return render(request, 'Navbar/denunciar.html')


def resetPassword():
    subject, from_email, to = 'hello', 'jdm006@alumnos.ucn.cl', 'juliocesardm93@gmail.com'
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def rut_format(value, separator=","):

    # Unformat the RUT
    value = rut_unformat(value)

    rut, verifier_digit = value[:-1], value[-1]

    try:
        # Add thousands separator
        rut = "{0:,}".format(int(rut))

        # If you specified another thousands separator instead of ','
        if separator != ",":
            # Apply the custom thousands separator
            rut = rut.replace(",", separator)

        return "%s-%s" % (rut, verifier_digit)

    except ValueError:
        # If the RUT cannot be converted to Int
        raise template.TemplateSyntaxError("RUT must be numeric, in order to be formatted")


def rut_unformat(value):

    return value.replace("-", "").replace(".", "").replace(",", "")


@login_required
def page_one_poll(request):
    form_page_one = FormPageOne()
    id_empresa = UserGuiar.objects.get(rut='12345678-5')
    form_page_one.nombre = id_empresa.rut
    form_page_one.direccion = id_empresa.address
    #form_page_one.changed_data

    answer1 = ""
    answer2 = ""
    answer3 = ""
    answer4 = ""
    answer5 = ""
    answer6 = ""
    answer7 = ""
    answer8 = ""

    dotacion = TablaResultadosDotacion(
        empresa=id_empresa,
        answer1=answer1,
        answer2=answer2,
        answer3=answer3,
        answer4=answer4,
        answer5=answer5,
        answer6=answer6,
        answer7=answer7,
        answer8=answer8
    )
    dotacion.save()

    answer1 = ""
    answer2 = ""
    answer3 = ""
    answer4 = ""
    answer5 = ""

    # acá se guardan los tipos de procesos en los que se desenvuelve la empresa
    procesos = TablaResultadosProcesos(
        empresa=id_empresa,
        answer1=answer1,
        answer2=answer2,
        answer3=answer3,
        answer4=answer4,
        answer5=answer5
    )
    procesos.save()

    return render(request, 'MideTuRiesgo/mideturiesgo01.html', {'form_page_one': form_page_one , 'user': id_empresa})


@login_required
def page_two_poll(request):
    form_page_two = FormPageTwo()
    id_empresa = UserGuiar.objects.get(rut='12345678-5')

    estructura = ""
    gruesa = ""
    instalaciones = ""
    menores = ""
    tuberias = ""
    refuerzos = ""

    construccion = TablaResultadosContruccion(
        empresa=id_empresa,
        answer1=estructura,
        answer2=gruesa,
        answer3=instalaciones,
        answer4=menores,
        answer5=tuberias,
        answer6=refuerzos
    )
    construccion.save()

    produccion = ""
    confeccion = ""
    tornerias = ""
    pvc = ""
    muebles = ""
    prototipos = ""

    manufactura= TablaResultadosManufactura(
        empresa=id_empresa,
        answer1=produccion,
        answer2=confeccion,
        answer3=tornerias,
        answer4=pvc,
        answer5=muebles,
        answer6=prototipos
    )
    manufactura.save()

    materiales = ""
    personas = ""
    maquinaria = ""
    mercaderia = ""
    granel = ""
    solidos = ""
    corrosivo = ""
    aceite = ""
    carga = ""

    transporte = TablaResultadosTransporte(
        empresa=id_empresa,
        answer1=materiales,
        answer2=personas,
        answer3=maquinaria,
        answer4=mercaderia,
        answer5=granel,
        answer6=solidos,
        answer7=corrosivo,
        answer8=aceite,
        answer9=carga
    )
    transporte.save()

    maestranza = ""
    reparacion = ""
    electricos = ""
    generador = ""
    repuesto = ""
    hidraulico = ""
    computacional = ""
    lavenderia = ""
    movimiento = ""
    arriendo = ""
    ferreteria = ""
    carretera = ""
    izaje = ""
    garage = ""

    servicios = TablaResultadosServicios(
        empresa=id_empresa,
        answer1=maestranza,
        answer2=reparacion,
        answer3=electricos,
        answer4=generador,
        answer5=repuesto,
        answer6=hidraulico,
        answer7=computacional,
        answer8=lavenderia,
        answer9=movimiento,
        answer10=arriendo,
        answer11=ferreteria,
        answer12=carretera,
        answer13=izaje,
        answer14=garage
    )
    servicios.save()

    return render(request, "MideTuRiesgo/mideturiesgo2.html", {'form_page_two': form_page_two})

@login_required
def page_three_poll(request):
    form_page_three = FormPageThree()
    id_empresa = UserGuiar.objects.get(rut='12345678-5')

    iso9001 = ""
    iso14001 = ""
    ohsas18001 = ""
    procedimiento = ""
    asesoria = ""
    gerencia = ""
    tiempoCompleto = ""
    tiempoParcial = ""
    proyectos = ""
    noTiene = ""

    gestion = TablaResultadosGestion(
        empresa=id_empresa,
        answer1=iso9001,
        answer2=iso14001,
        answer3=ohsas18001,
        answer4=procedimiento,
        answer5=asesoria,
        answer6=gerencia,
        answer7=tiempoCompleto,
        answer8=tiempoParcial,
        answer9=proyectos,
        answer10=noTiene
    )
    gestion.save()

    return render(request, "MideTuRiesgo/mideturiesgo3.html", {'form_page_three': form_page_three})

@login_required
def page_four_poll(request):
    form_page_four = FormPageFour()
    id_empresa = UserGuiar.objects.get(rut='12345678-5')

    inscripcion = ""
    certificado = ""
    personal = ""
    polvorin = ""
    procedimientos = ""
    dispositivos = ""

    explosivos = TablaResultadosExplosivos(
        empresa=id_empresa,
        answer1=inscripcion,
        answer2=certificado,
        answer3=personal,
        answer4=polvorin,
        answer5=procedimientos,
        answer6=dispositivos
    )
    explosivos.save()

    apertura = ""
    encaramiento = ""
    ausencia = ""
    tierra = ""
    delimitacion = ""

    electricidad = TablaResultadosElectricidad(
        empresa=id_empresa,
        answer1=apertura,
        answer2=encaramiento,
        answer3=ausencia,
        answer4=tierra,
        answer5=delimitacion
    )
    electricidad.save()

    distintivos = ""
    tacografo = ""
    antiguedad = ""
    transporte = ""
    embalaje = ""
    carga = ""
    tipoA = ""
    tipoB = ""
    tipoC = ""

    sustancias_peligrosas = TablaResultadosSustanciasPeligrosas(
        empresa=id_empresa,
        answer1=distintivos,
        answer2=tacografo,
        answer3=antiguedad,
        answer4=transporte,
        answer5=embalaje,
        answer6=carga,
        answer7=tipoA,
        answer8=tipoB,
        answer9=tipoC
    )
    sustancias_peligrosas.save()

    norma = ""
    supervisor = ""
    proteccion = ""
    equipamiento = ""

    altura = TablaResultadosRiesgoAltura(
        empresa=id_empresa,
        answer1=norma,
        answer2=supervisor,
        answer3=proteccion,
        answer4=equipamiento)
    altura.save()

    return render(request, "MideTuRiesgo/mideturiesgo4.html", {'form_page_four': form_page_four})


def page_results(request):
    if request.method == 'GET':
        a = "placeholder"
    else:
        # Error de metodo
        e = "Operacion Invalida"
    return render(request, "MideTuRiesgo/mideturiesgoresultado.html")
