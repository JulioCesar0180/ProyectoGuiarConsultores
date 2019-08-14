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
    if request.method == 'POST':
        form1 = FormInicial(request.POST)
        form2 = FormDefault(request.POST)
        context = {'perfil_usuario':form1, 'resultados_dotacion':form2}
        if form1.is_valid():
            if form2.is_valid():
                nombre = form1.cleaned_data['nombre']
                email = form1.cleaned_data['email']
                telefono = form1.cleaned_data['telefono']
                razon = form1.cleaned_data['razon'] # Este dato actualmente no se usa
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
        context = {'perfil_usuario':form1, 'resultados_dotacion':form2}
    return render(request, "MideTuRiesgo/mideturiesgo.html", context)

@login_required
def polltwo(request):
    if request.method == 'POST':
        form1 = FormDefault(request.POST)
        form2 = FormDefault(request.POST)
        form3 = FormDefault(request.POST)
        form4 = FormDefault(request.POST)
        context = {'resultados_construccion':form1, 'resultados_manufactura':form2, 'resultados_transporte':form3, 'resultados_servicios':form4}
        if form1.is_valid():
            if form2.is_valid():
                if form3.is_valid():
                    if form4.is_valid():
                        estructura = form1.cleaned_data['estructura']
                        gruesa = form1.cleaned_data['gruesa']
                        instalaciones = form1.cleaned_data['instalaciones']
                        menores = form1.cleaned_data['menores']
                        tuberias = form1.cleaned_data['tuberias']
                        refuerzos = form1.cleaned_data['refuerzos']
                        otraConst = form1.cleaned_data['otraConst'] # Aca se especifica texto, puede dar errores
                        construccion = Tabla_resultados_construccion(user=1,
                                                                     answer1=estructura,
                                                                     answer2=gruesa,
                                                                     answer3=instalaciones,
                                                                     answer4=menores,
                                                                     answer5=tuberias,
                                                                     answer6=refuerzos,
                                                                     answer7=otraConst)
                        construccion.save()
                        # return HttpResponseRedirect('/thanks/')
                        produccion = form2.cleaned_data['produccion']
                        confeccion = form2.cleaned_data['confeccion']
                        tornerias = form2.cleaned_data['tornerias']
                        pvc = form2.cleaned_data['pvc']
                        muebles = form2.cleaned_data['muebles']
                        prototipos = form2.cleaned_data['prototipos']
                        otraManufac = form2.cleaned_data['otraManufac'] # Aca se especifica texto, puede dar errores
                        manufactura= Tabla_resultados_manufactura(user=1,
                                                                  answer1=produccion,
                                                                  answer2=confeccion,
                                                                  answer3=tornerias,
                                                                  answer4=pvc,
                                                                  answer5=muebles,
                                                                  answer6=prototipos,
                                                                  answer7=otraManufac)
                        manufactura.save()
                        # return HttpResponseRedirect('/thanks/')
                        materiales = form3.cleaned_data['materiales']
                        personas = form3.cleaned_data['personas']
                        maquinaria = form3.cleaned_data['maquinaria']
                        mercaderia = form3.cleaned_data['mercaderia']
                        granel = form3.cleaned_data['granel']
                        solidos = form3.cleaned_data['solidos']
                        corrosivo = form3.cleaned_data['corrosivo']
                        aceite = form3.cleaned_data['aceite']
                        carga = form3.cleaned_data['carga']
                        otraTerr = form3.cleaned_data['otraTerr'] # Aca se especifica texto, puede dar errores
                        transporte = Tabla_resultados_transporte(user=1,
                                                                 answer1=materiales,
                                                                 answer2=personas,
                                                                 answer3=maquinaria,
                                                                 answer4=mercaderia,
                                                                 answer5=granel,
                                                                 answer6=solidos,
                                                                 answer7=corrosivo,
                                                                 answer8=aceite,
                                                                 answer9=carga,
                                                                 answer10=otraTerr)
                        transporte.save()
                        # return HttpResponseRedirect('/thanks/')
                        maestranza = form4.cleaned_data['maestranza']
                        reparacion = form4.cleaned_data['reparacion']
                        electricos = form4.cleaned_data['electricos']
                        generador = form4.cleaned_data['generador']
                        repuesto = form4.cleaned_data['repuesto']
                        hidraulico = form4.cleaned_data['hidraulico']
                        computacional = form4.cleaned_data['computacional']
                        lavenderia = form4.cleaned_data['lavenderia']
                        movimiento = form4.cleaned_data['movimiento']
                        arriendo = form4.cleaned_data['arriendo']
                        ferreteria = form4.cleaned_data['ferreteria']
                        carretera = form4.cleaned_data['carretera']
                        izaje = form4.cleaned_data['izaje']
                        garage = form4.cleaned_data['garage']
                        servicios = Tabla_resultados_servicios(user=1,
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
                                                               answer14=garage)
                        servicios.save()
                    # hay problemas con el Form 4
                # hay problemas con el Form 3
            # hay problemas con el Form 2
        # hay problemas con el Form 1
    else:
        form1 = FormDefault()
        form2 = FormDefault()
        form3 = FormDefault()
        form4 = FormDefault()
        context = {'resultados_construccion':form1, 'resultados_manufactura':form2, 'resultados_transporte':form3, 'resultados_servicios':form4}
    return render(request, "MideTuRiesgo/mideturiesgo2.html", context)

@login_required
def pollthree(request):
    if request.method == 'POST':
        form1 = FormDefault(request.POST)
        context = {'resultados_gestion':form1}
        if form1.is_valid():
            iso9001 = form1.cleaned_data['iso9001']
            iso14001 = form1.cleaned_data['iso14001']
            ohsas18001 = form1.cleaned_data['ohsas18001']
            otraCert = form1.cleaned_data['otraCert'] # requiere texto por lo que puede dar errores
            procedimiento = form1.cleaned_data['procedimiento']
            asesoria = form1.cleaned_data['asesoria']
            gerencia = form1.cleaned_data['gerencia']
            tiempoCompleto = form1.cleaned_data['tiempoCompleto']
            tiempoParcial = form1.cleaned_data['tiempoParcial']
            proyectos = form1.cleaned_data['proyectos']
            noTiene = form1.cleaned_data['noTiene']
            gestion = Tabla_resultados_gestion(user=1,
                                               answer1=iso9001,
                                               answer2=iso14001,
                                               answer3=ohsas18001,
                                               answer4=otraCert,
                                               answer5=procedimiento,
                                               answer6=asesoria,
                                               answer7=gerencia,
                                               answer8=tiempoCompleto,
                                               answer9=tiempoParcial,
                                               answer10=proyectos,
                                               answer11=noTiene)
            gestion.save()
        # hay problemas con el Form 1
    else:
        form1 = FormDefault()
        context = {'resultados_gestion':form1}
    return render(request, "MideTuRiesgo/mideturiesgo3.html", context)

@login_required
def pollfour(request):
    if request.method == 'POST':
        form1 = FormDefault(request.POST)
        form2 = FormDefault(request.POST)
        form3 = FormDefault(request.POST)
        form4 = FormDefault(request.POST)
        context = {'resultados_explosivos':form1, 'resultados_electricidad':form2, 'resultados_sustancias_peligrosas':form3, 'resultados_altura':form4}
        if form1.is_valid():
            if form2.is_valid():
                if form3.is_valid():
                    if form4.is_valid():
                        inscripcion = form1.cleaned_data['inscripcion']
                        certificado = form1.cleaned_data['certificado']
                        personal = form1.cleaned_data['personal']
                        polvorin = form1.cleaned_data['polvorin']
                        procedimientos = form1.cleaned_data['procedimientos']
                        dispositivos = form1.cleaned_data['dispositivos']
                        explosivos = Tabla_resultados_explosivos(user=1,
                                                                 answer1=inscripcion,
                                                                 answer2=certificado,
                                                                 answer3=personal,
                                                                 answer4=polvorin,
                                                                 answer5=procedimientos,
                                                                 answer6=dispositivos)
                        explosivos.save()
                        # return HttpResponseRedirect('/thanks/')
                        apertura = form2.cleaned_data['apertura']
                        encaramiento = form2.cleaned_data['encaramiento']
                        ausencia = form2.cleaned_data['ausencia']
                        tierra = form2.cleaned_data['tierra']
                        delimitacion = form2.cleaned_data['delimitacion']
                        electricidad = Tabla_resultados_electricidad(user=1,
                                                                     answer1=apertura,
                                                                     answer2=encaramiento,
                                                                     answer3=ausencia,
                                                                     answer4=tierra,
                                                                     answer5=delimitacion)
                        electricidad.save()
                        # return HttpResponseRedirect('/thanks/')
                        distintivos = form3.cleaned_data['distintivos']
                        tacografo = form3.cleaned_data['tacografo']
                        antiguedad = form3.cleaned_data['antiguedad']
                        transporte = form3.cleaned_data['transporte']
                        embalaje = form3.cleaned_data['embalaje']
                        carga = form3.cleaned_data['carga']
                        tipoA = form3.cleaned_data['tipoA']
                        tipoB = form3.cleaned_data['tipoB']
                        tipoC = form3.cleaned_data['tipoC']
                        sustancias_peligrosas = Tabla_resultados_sustancias_peligrosas(user=1,
                                                                                       answer1=distintivos,
                                                                                       answer2=tacografo,
                                                                                       answer3=antiguedad,
                                                                                       answer4=transporte,
                                                                                       answer5=embalaje,
                                                                                       answer6=carga,
                                                                                       answer7=tipoA,
                                                                                       answer8=tipoB,
                                                                                       answer9=tipoC)
                        sustancias_peligrosas.save()
                        # return HttpResponseRedirect('/thanks/')
                        norma = form4.cleaned_data['norma']
                        supervisor = form4.cleaned_data['supervisor']
                        proteccion = form4.cleaned_data['proteccion']
                        equipamiento = form4.cleaned_data['equipamiento']
                        altura = Tabla_resultados_altura(user=1,
                                                         answer1=norma,
                                                         answer2=supervisor,
                                                         answer3=proteccion,
                                                         answer4=equipamiento)
                        altura.save()
                    # hay problemas con el Form 4
                # hay problemas con el Form 3
            # hay problemas con el Form 2
        # hay problemas con el Form 1
    else:
        form1 = FormDefault()
        form2 = FormDefault()
        form3 = FormDefault()
        form4 = FormDefault()
        context = {'resultados_explosivos':form1, 'resultados_electricidad':form2, 'resultados_sustancias_peligrosas':form3, 'resultados_altura':form4}
    return render(request, "MideTuRiesgo/mideturiesgo4.html", context)

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
