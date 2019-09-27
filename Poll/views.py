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

from django.http import HttpResponseRedirect
from django.shortcuts import render

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormPageOne(request.POST)
        rubro = request.POST.getlist('rubro[]')
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            rutEmpresa = form.cleaned_data['rut']
            empresa = UserGuiar.objects.get(rut=rutEmpresa)
            #Datos del usuario
            nombreUser = form.cleaned_data['representante']
            correo = form.cleaned_data['email']
            fono = form.cleaned_data['telefono']
            #Datos de la empresa
            nombreEmpresa = form.cleaned_data['nombre']
            razonEmpresa = form.cleaned_data['razon']
            experienciaEmpresa = form.cleaned_data['experiencia']
            direccionEmpresa = form.cleaned_data['direccion']
            comunaEmpresa = form.cleaned_data['comuna']
            ciudadEmpresa = form.cleaned_data['ciudad']
            #Datos ganancias
            ganancia = form.cleaned_data['ventas']
            #Datos dotación empresa
            empleadosCont = form.cleaned_data['empContratados']
            empleadosContra = form.cleaned_data['empContratistas']
            vehiculosLiv = form.cleaned_data['vehLivianos']
            vehiculosCont = form.cleaned_data['vehContratistas']
            vehiculosPes = form.cleaned_data['vehPesados']
            vehiculosPesCont = form.cleaned_data['vehPesadosContratistas']
            maquinariaEmpr = form.cleaned_data['maqEmpresa']
            maquinariaCont = form.cleaned_data['marContratista']
            datoDotacion = TablaResultadosDotacion(
                rut_empresa = empresa,
                answer1 = empleadosCont,
                answer2 = empleadosContra,
                answer3 = vehiculosLiv,
                answer4 = vehiculosCont,
                answer5 = vehiculosPes,
                answer6 = vehiculosPesCont,
                answer7 = maquinariaEmpr,
                answer8 = maquinariaCont,
            )
            datoNombre = TablaPerfilEmpresa(
                nombre_empresa = nombreEmpresa,
                razon_social_empresa = razonEmpresa,
                rut_empresa = empresa,
                experiencia_empresa = experienciaEmpresa,
                direccion_empresa = direccionEmpresa,
                comuna_empresa = comunaEmpresa,
                ciudad_empresa = ciudadEmpresa,
                nombre_representante = nombreUser,
                email_representante = correo,
                telefono_representante = fono,
                ventas_anuales_empresa = ganancia
            )
            construccion = False
            manufactura = False
            transporte = False
            servicios = False
            for x in rubro:
                if x == "construccion":
                    construccion = True
                elif x == "manufactura":
                    manufactura = True
                elif x == "transporte":
                    transporte = True
                elif x == "servicios":
                    servicios = True
            datoRubro = TablaResultadosProcesos(
                rut_empresa = empresa,
                answer1=construccion,
                answer2=manufactura,
                answer3=transporte,
                answer4=servicios
            )
            datoDotacion.save()
            datoRubro.save()
            datoNombre.save()
            # redirect to a new URL:
            return HttpResponseRedirect('2')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormPageOne()

    return render(request, 'MideTuRiesgo/test.html', {'form': form})

def home(request):
    count = UserGuiar.objects.count()
    name = request.user.name
    return render(request, 'home.html', {
        'count': count, 'name': name
    })


def Perfil(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = UpdateForm()
    #return render(request, 'u_perfil.html', {'form': form})
    return render(request, 'perfil.html', {'form': form})


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
            return render(request, 'registration/login.html', {'form': form})

    form = LogInForm()
    return render(request, 'registration/login.html', {'form': form})

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            rut_empresa = form.cleaned_data['rut']
            nombre_empresa = form.cleaned_data['name']
            direccion_empresa = form.cleaned_data['address']
            nombre_representante = form.cleaned_data['nombre_representante']
            email_representante = form.cleaned_data['email_representante']
            telefono_representante = form.cleaned_data['telefono_representante']

            perfil_empresa = TablaPerfilEmpresa(
                rut_empresa=user,
                nombre_empresa=nombre_empresa,
                direccion_empresa=direccion_empresa,
                nombre_representante=nombre_representante,
                email_representante=email_representante,
                telefono_representante=telefono_representante
            )
            perfil_empresa.save()

            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


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

    answer1 = ""
    answer2 = ""
    answer3 = ""
    answer4 = ""
    answer5 = ""
    answer6 = ""
    answer7 = ""
    answer8 = ""


    answer1 = ""
    answer2 = ""
    answer3 = ""
    answer4 = ""
    answer5 = ""

    return render(request, "MideTuRiesgo/mideturiesgo01.html", {'form_page_one': form_page_one})


@login_required
def page_two_poll(request):
    form = FormPageTwo()
    empresa = UserGuiar.objects.get(rut='12345678-5')
    respuestas = TablaResultadosProcesos.objects.get(rut_empresa=empresa)
    print(respuestas.answer1)
    print(respuestas.answer2)
    print(respuestas.answer3)
    print(respuestas.answer4)
    '''
    construccion = request.POST.getlist('construccion[]')

    estructura = False
    gruesa = False
    instalaciones = False
    menores = False
    tuberias = False
    refuerzos = False
    for x in construccion:
        if x == "estructura":
            estructura = True
        if x == "gruesa":
            gruesa = True
        if x == "instalaciones":
            instalaciones = True
        if x == "menores":
            menores = True
        if x == "tuberias":
            tuberias = True
        if x == "refuerzos":
            refuerzos = True
            
    construccion = TablaResultadosContruccion(
        empresa=empresa,
        answer1=estructura,
        answer2=gruesa,
        answer3=instalaciones,
        answer4=menores,
        answer5=tuberias,
        answer6=refuerzos
    )
    construccion.save()

    manufactura = request.POST.getlist('manufactura[]')

    produccion = False
    confeccion = False
    tornerias = False
    pvc = False
    muebles = False
    prototipos = False
    for x in manufactura:
        if x == "produccion":
            produccion = True
        if x == "confeccion":
            confeccion = True
        if x == "tornerias":
            tornerias = True
        if x == "pvc":
            pvc = True
        if x == "muebles":
            muebles = True
        if x == "prototipos":
            prototipos = True
            
    manufactura= TablaResultadosManufactura(
        empresa=empresa,
        answer1=produccion,
        answer2=confeccion,
        answer3=tornerias,
        answer4=pvc,
        answer5=muebles,
        answer6=prototipos
    )
    manufactura.save()

    transporte = request.POST.getlist('transporte[]')

    materiales = False
    personas = False
    maquinaria = False
    mercaderia = False
    granel = False
    solidos = False
    corrosivo = False
    aceite = False
    carga = False
    for x in transporte:
        if x == "materiales":
            materiales = True
        if x == "personas":
            personas = True
        if x == "maquinaria":
            maquinaria = True
        if x == "mercaderia":
            mercaderia = True
        if x == "granel":
            granel = True
        if x == "solidos":
            solidos = True
        if x == "corrosivo":
            corrosivo = True
        if x == "aceite":
            aceite = True
        if x == "carga":
            carga = True


    transporte = TablaResultadosTransporte(
        empresa=empresa,
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

    servicios = request.POST.getlist('servicios[]')
    
    maestranza = False
    reparacion = False
    electricos = False
    generador = False
    repuesto = False
    hidraulico = False
    computacional = False
    lavenderia = False
    movimiento = False
    arriendo = False
    ferreteria = False
    carretera = False
    izaje = False
    garage = False
    for x in transporte:
        if x == "maestranza":
            maestranza = True
        if x == "reparacion":
            reparacion = True
        if x == "electricos":
            electricos = True
        if x == "generador":
            generador = True
        if x == "repuesto":
            repuesto = True
        if x == "hidraulico":
            hidraulico = True
        if x == "computacional":
            computacional = True
        if x == "lavenderia":
            lavenderia = True
        if x == "movimiento":
            movimiento = True
        if x == "arriendo":
            arriendo = True
        if x == "ferreteria":
            ferreteria = True
        if x == "carretera":
            carretera = True
        if x == "izaje":
            izaje = True
        if x == "garage":
            garage = True

    servicios = TablaResultadosServicios(
        empresa=empresa,
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
    '''
    return render(request, "MideTuRiesgo/mideturiesgo2.html", {'form_page_two': form})

@login_required
def page_three_poll(request):
    form = FormPageThree()
    if request.method == 'POST':

        empresa = UserGuiar.objects.get(rut='12345678-5')

        iso = request.POST.getlist('iso[]')

        iso9001 = False
        iso14001 = False
        ohsas18001 = False
        for x in iso:
            if x == "iso9001":
                iso9001 = True
            elif x == "iso14001":
                iso14001 = True
            elif x == "ohsas18001":
                ohsas18001 = True
        '''
        manejoRiesgo = request.POST.getlist('manejoRiesgo[]')
        procedimiento = False
        asesoria = False
        gerencia = False
        for x in manejoRiesgo:
            if x == "procedimiento":
                procedimiento = True
            elif x == "asesoria":
                asesoria = True
            elif x == "gerencia":
                gerencia = True
        
        prevensionista = request.POST.getlist('prevensionista[]')
        tiempoCompleto = False
        tiempoParcial = False
        proyectos = False
        noTiene = False
        for x in prevensionista:
            if x == "tiempoCompleto":
                tiempoCompleto = True
            elif x == "tiempoParcial":
                tiempoParcial = True
            elif x == "proyectos":
                proyectos = True
            elif x == "noTiene":
                noTiene = True
        
        gestion = TablaResultadosGestion(
            empresa=empresa,
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
        '''
        return HttpResponseRedirect('4')
    return render(request, "MideTuRiesgo/mideturiesgo3.html", {'form_page_three': form})

@login_required
def page_four_poll(request):
    form = FormPageFour()
    empresa = UserGuiar.objects.get(rut='12345678-5')
    '''
    inscripcion = form.cleaned_data["inscripcion"]
    certificado = form.cleaned_data["certificado"]
    personal = form.cleaned_data["personal"]
    polvorin = form.cleaned_data["polvorin"]
    procedimientos = form.cleaned_data["procedimientos"]
    dispositivos = form.cleaned_data["dispositivos"]

    explosivos = TablaResultadosExplosivos(
        empresa=empresa,
        answer1=inscripcion,
        answer2=certificado,
        answer3=personal,
        answer4=polvorin,
        answer5=procedimientos,
        answer6=dispositivos
    )
    explosivos.save()

    apertura = form.cleaned_data["apertura"]
    encaramiento = form.cleaned_data["encaramiento"]
    ausencia = form.cleaned_data["ausencia"]
    tierra = form.cleaned_data["tierra"]
    delimitacion = form.cleaned_data["delimitacion"]

    electricidad = TablaResultadosElectricidad(
        empresa=empresa,
        answer1=apertura,
        answer2=encaramiento,
        answer3=ausencia,
        answer4=tierra,
        answer5=delimitacion
    )
    electricidad.save()

    distintivos = form.cleaned_data["distintivos"]
    tacografo = form.cleaned_data["tacografo"]
    antiguedad = form.cleaned_data["antiguedad"]
    transporte = form.cleaned_data["transporte"]
    embalaje = form.cleaned_data["embalaje"]
    carga = form.cleaned_data["carga"]
    tipoA = form.cleaned_data["tipoA"]
    tipoB = form.cleaned_data["tipoB"]
    tipoC = form.cleaned_data["tipoC"]

    sustancias_peligrosas = TablaResultadosSustanciasPeligrosas(
        empresa=empresa,
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

    norma = form.cleaned_data["norma"]
    supervisor = form.cleaned_data["supervisor"]
    proteccion = form.cleaned_data["proteccion"]
    equipamiento = form.cleaned_data["equipamiento"]

    altura = TablaResultadosRiesgoAltura(
        empresa=empresa,
        answer1=norma,
        answer2=supervisor,
        answer3=proteccion,
        answer4=equipamiento)
    altura.save()
    '''
    return render(request, "MideTuRiesgo/mideturiesgo4.html", {'form_page_four': form})


def page_results(request):
    if request.method == 'GET':
        a = "placeholder"
    else:
        # Error de metodo
        e = "Operacion Invalida"
    return render(request, "MideTuRiesgo/mideturiesgoresultado.html")
