# encoding: utf-8

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
from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string

#rut
from django import template


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
            username = rut_format(username, ".")
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
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
    form1 = Form_datosPersonales()
    form2 = Form_datosEmpresa()
    form3 = Form_ventasEmpresa()
    form4 = Form_dotacionEmpresa()
    if request.method == 'POST':
        form1 = Form_datosPersonales(request.POST)
        form2 = Form_datosEmpresa(request.POST)
        form3 = Form_ventasEmpresa(request.POST)
        form4 = Form_dotacionEmpresa(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():

            #obtener datos de Datos Personales
            nombre = form1.cleaned_data['nombre']
            email = form1.cleaned_data['email']
            telefono = form1.cleaned_data['telefono']

            #obtener datos de la Empresa
            razon_social = form2.cleaned_data['razon']
            rut = form2.cleaned_data['rut']
            representante = form2.cleaned_data['nombre_representante']
            experiencia = form2.cleaned_data['experiencia']
            direccion = form2.cleaned_data['direccion']
            comuna = form2.cleaned_data['comuna']
            ciudad = form2.cleaned_data['ciudad']
            ventas = form3.cleaned_data['ventas']

            empContratados = form3.cleaned_data['empContratados']
            empContratistas = form3.cleaned_data['empContratistas']
            vehLivianos = form3.cleaned_data['vehLivianos']
            vehContratistas = form3.cleaned_data['vehContratistas']
            vehPesados = form3.cleaned_data['vehPesados']
            vehPesadosContratistas = form3.cleaned_data['vehPesadosContratistas']
            maqEmpresa = form3.cleaned_data['maqEmpresa']
            marContratista = form3.cleaned_data['marContratista']

            #Se crea el objeto
            datosPersonales = Tabla_perfil_usuario(
                user_id=request.user.id,
                nombre_empresa=nombre,
                rut_empresa=rut,
                direccion_empresa=direccion,
                experiencia_empresa=experiencia,
                ciudad_empresa=ciudad,
                comuna_empresa=comuna,
                nombre_contacto_empresa=representante,
                telefono_empresa=telefono,
                email_empresa=email,
                razon_social_empresa=razon_social,
                ventas_anuales_empresa=ventas
            )
            datosPersonales.save()

            # obtener los datos que reflejan la dotacion de la empresa
            empContratados = form4.cleaned_data['empContratados']
            empContratistas = form4.cleaned_data['empContratistas']
            vehLivianos = form4.cleaned_data['vehLivianos']
            vehContratistas = form4.cleaned_data['vehContratistas']
            vehPesados = form4.cleaned_data['vehPesados']
            vehPesadosContratistas = form4.cleaned_data['vehPesadosContratistas']
            maqEmpresa = form4.cleaned_data['maqEmpresa']
            marContratista = form4.cleaned_data['marContratista']
            dotacion = Tabla_resultados_dotacion(
                user=1,
                empContratados=empContratados,
                empContratistas=empContratistas,
                vehLivianos=vehLivianos,
                vehContratistas=vehContratistas,
                vehPesados=vehPesados,
                vehPesadosContratistas=vehPesadosContratistas,
                maqEmpresa=maqEmpresa,
                marContratista=marContratista
            )
            dotacion.save()
            #Volver a la pagina de Inicio por el momento
            return render(request, "home/home.html")
    else:
        # Error de metodo
        e = "Operacion Invalida"
    context = \
        {'datos_personales': form1,
         'datos_empresa': form2,
         'ventas_empresa': form3,
         'dotacion_empresa': form4
         }
    return render(request, "MideTuRiesgo/mideturiesgo.html", context)

@login_required
def page_two_poll(request):
    if request.method == 'POST':
        form1 = Form_elementosRiesgo(request.POST)
        form2 = Form_actManufaturas(request.POST)
        form3 = Form_tipoCargas(request.POST)
        form4 = Form_serviciosGenerales(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            estructura = form1.cleaned_data['estructura']
            gruesa = form1.cleaned_data['gruesa']
            instalaciones = form1.cleaned_data['instalaciones']
            menores = form1.cleaned_data['menores']
            tuberias = form1.cleaned_data['tuberias']
            refuerzos = form1.cleaned_data['refuerzos']
            construccion = Tabla_resultados_construccion(
                empresa=1,
                answer1=estructura,
                answer2=gruesa,
                answer3=instalaciones,
                answer4=menores,
                answer5=tuberias,
                answer6=refuerzos
            )
            construccion.save()
            # return HttpResponseRedirect('/thanks/')
            produccion = form2.cleaned_data['produccion']
            confeccion = form2.cleaned_data['confeccion']
            tornerias = form2.cleaned_data['tornerias']
            pvc = form2.cleaned_data['pvc']
            muebles = form2.cleaned_data['muebles']
            prototipos = form2.cleaned_data['prototipos']
            manufactura= Tabla_resultados_manufactura(
                empresa=1,
                answer1=produccion,
                answer2=confeccion,
                answer3=tornerias,
                answer4=pvc,
                answer5=muebles,
                answer6=prototipos
            )
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
            transporte = Tabla_resultados_transporte(
                empresa=1,
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
            servicios = Tabla_resultados_servicios(
                empresa=1,
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
            # Volver a la pagina de Inicio por el momento
            return render(request, "home/home.html")
        else:
            # hay problemas con los Forms
            e = "Operacion Invalida"
    else:
        # Error de metodo
        e = "Operacion Invalida"
    context = \
        {'resultados_construccion':form1,
         'resultados_manufactura':form2,
         'resultados_transporte':form3,
         'resultados_servicios':form4
         }
    return render(request, "MideTuRiesgo/mideturiesgo2.html", context)

@login_required
def page_three_poll(request):
    if request.method == 'POST':
        form1 = Form_certificacionesEmpresa(request.POST)
        form2 = Form_elementosManejoRiesgos(request.POST)
        form3 = Form_jornadaPrevencionista(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            iso9001 = form1.cleaned_data['iso9001']
            iso14001 = form1.cleaned_data['iso14001']
            ohsas18001 = form1.cleaned_data['ohsas18001']
            procedimiento = form2.cleaned_data['procedimiento']
            asesoria = form2.cleaned_data['asesoria']
            gerencia = form2.cleaned_data['gerencia']
            tiempoCompleto = form3.cleaned_data['tiempoCompleto']
            tiempoParcial = form3.cleaned_data['tiempoParcial']
            proyectos = form3.cleaned_data['proyectos']
            noTiene = form3.cleaned_data['noTiene']
            gestion = Tabla_resultados_gestion(
                empresa=1,
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
            return render(request, "home/home.html")
        else:
            # hay problemas con los Forms
            e = "Operacion Invalida"
    else:
        # Error de metodo
        e = "Operacion Invalida"
    context = \
        {'resultados_gestion_certificaciones':form1,
         'resultados_gestion_elementos':form2,
         'resultados_gestion_jornada':form3
         }
    return render(request, "MideTuRiesgo/mideturiesgo3.html", context)

@login_required
def page_four_poll(request):
    if request.method == 'POST':
        form1 = FormDefault(request.POST)
        form2 = FormDefault(request.POST)
        form3 = FormDefault(request.POST)
        form4 = FormDefault(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            inscripcion = form1.cleaned_data['inscripcion']
            certificado = form1.cleaned_data['certificado']
            personal = form1.cleaned_data['personal']
            polvorin = form1.cleaned_data['polvorin']
            procedimientos = form1.cleaned_data['procedimientos']
            dispositivos = form1.cleaned_data['dispositivos']
            explosivos = Tabla_resultados_explosivos(
                empresa=1,
                answer1=inscripcion,
                answer2=certificado,
                answer3=personal,
                answer4=polvorin,
                answer5=procedimientos,
                answer6=dispositivos
            )
            explosivos.save()
            # return HttpResponseRedirect('/thanks/')
            apertura = form2.cleaned_data['apertura']
            encaramiento = form2.cleaned_data['encaramiento']
            ausencia = form2.cleaned_data['ausencia']
            tierra = form2.cleaned_data['tierra']
            delimitacion = form2.cleaned_data['delimitacion']
            electricidad = Tabla_resultados_electricidad(
                empresa=1,
                answer1=apertura,
                answer2=encaramiento,
                answer3=ausencia,
                answer4=tierra,
                answer5=delimitacion
            )
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
            sustancias_peligrosas = Tabla_resultados_sustancias_peligrosas(
                empresa=1,
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
            # return HttpResponseRedirect('/thanks/')
            norma = form4.cleaned_data['norma']
            supervisor = form4.cleaned_data['supervisor']
            proteccion = form4.cleaned_data['proteccion']
            equipamiento = form4.cleaned_data['equipamiento']
            altura = Tabla_resultados_altura(
                empresa=1,
                answer1=norma,
                answer2=supervisor,
                answer3=proteccion,
                answer4=equipamiento)
            altura.save()
            return render(request, "home/home.html")
        else:
            # hay problemas con los Forms
            e = "Operacion Invalida"
    else:
        # Error de metodo
        e = "Operacion Invalida"
    context = \
        {'resultados_explosivos':form1,
         'resultados_electricidad':form2,
         'resultados_sustancias_peligrosas':form3,
         'resultados_altura':form4
         }
    return render(request, "MideTuRiesgo/mideturiesgo4.html", context)


def page_results(request):
    if request.method == 'GET':
        a = "placeholder"
    else:
        # Error de metodo
        e = "Operacion Invalida"
    return render(request, "MideTuRiesgo/mideturiesgoresultado.html")
