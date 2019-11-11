# encoding: utf-8

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

@login_required(login_url='MTRlogin')
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
                elif x == "servicio":
                    servicios = True

            datoRubro = TablaResultadosProcesos(
                rut_empresa=empresa,
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

    try:
        empresa = TablaPerfilEmpresa.objects.get(rut_empresa_id = request.user.id)
        name = empresa.nombre_representante
        return render(request, 'home.html', {
            'name': name
        })
    except:
        return render(request, 'home.html', {
            'name': "Contacto"
        })


def Perfil(request):

    Obj_user = request.user
    idEmpresa = str(request.user.id)
    try:
        Obj_empresa = TablaPerfilEmpresa.objects.get(rut_empresa_id=idEmpresa)

        if request.method == 'POST':

            """Datos de contacto de la Obj_empresa"""

            """ Aquí solo falta validar el ingreso de datos para cada atributo, por ejemplo
             validar el ingreso de texto en blanco"""

            """Cada linea de este codigo, modifica los campos correpondientes"""
            Obj_empresa.nombre_representante = request.POST['nombre_representante']
            Obj_empresa.email_representante = request.POST['email_representante']
            Obj_empresa.telefono_representante = request.POST['telefono_representante']
            Obj_empresa.experiencia_empresa = request.POST['experiencia_empresa']
            Obj_empresa.razon_social_empresa = request.POST['razon_social_empresa']
            Obj_empresa.ventas_anuales_empresa = request.POST['ventas_anuales_empresa']
            Obj_empresa.comuna_empresa = request.POST['comuna_empresa']
            Obj_empresa.ciudad_empresa = request.POST['ciudad_empresa']

            "Nombre de la empresa se repite en las 2 tablas"
            Obj_empresa.nombre_empresa = request.POST['nombre_empresa']

            "Datos User Guiar"
            Obj_user.name = request.POST['nombre_empresa']
            Obj_user.address = request.POST['address']

            """ Actualiza la base de datos"""
            Obj_empresa.save()
            Obj_user.save()

        return render(request, 'perfil.html', {
            'Obj_empresa': Obj_empresa,
            'Obj_user': Obj_user,
        })
    except:
        """
        Todo usuario creado debe tener un perfil de empresa, salvo el super User, solo el deberia
        pasar por acá
        
        if request.method == 'POST':
        
            perfil_empresa = TablaPerfilEmpresa(
                nombre_representante = form.cleaned_data['nombre_representante'],
                email_representante = form.cleaned_data['email_representante'],
                telefono_representante = form.cleaned_data['telefono_representante'],
                experiencia_empresa = form.cleaned_data['experiencia_empresa'],
                razon_social_empresa = form.cleaned_data['razon_social_empresa'],
                ventas_anuales_empresa = form.cleaned_data['ventas_anuales_empresa'],
                comuna_empresa = form.cleaned_data['comuna_empresa'],
                ciudad_empresa = form.cleaned_data['ciudad_empresa'],
                nombre_empresa = form.cleaned_data['nombre_empresa'],
                rut_empresa_id = request.user.id
            )
            perfil_empresa.save()

        "Datos User Guiar"
        Obj_user.name = request.POST['nombre_empresa']
        Obj_user.address = request.POST['address']

        Obj_user.save()

        return render(request, 'perfil.html', {
            'Obj_user': Obj_user,
        })
        """
        return redirect('home')


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
                messages.error(request, 'El RUN o la clave ingresada no son correctos.')
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
    empresa = TablaPerfilEmpresa.objects.get(rut_empresa=request.user.id)
    dotacion_empresa = TablaResultadosDotacion.objects.get(rut_empresa_id=empresa.pk)
    empresa_procesos = TablaResultadosProcesos.objects.get(rut_empresa_id=empresa.pk)
    if request.method == "POST":
        form = FormPageOne(request.POST)
        if form.is_valid():
            return render(request, 'MideTuRiesgo/mideturiesgo2.html')
        else:
            context = {'form': form, 'empresa': empresa}
            return render(request, 'MideTuRiesgo/mideturiesgo.html', context=context)
    else:
        # Visualizar los datos en el formulario
        data = {
            # Datos de la empresa
            'razon_social': empresa.razon_social_empresa,
            'rut': empresa.rut_empresa,
            'experiencia': empresa.experiencia_empresa,
            'direccion': empresa.direccion_empresa,
            'comuna': empresa.comuna_empresa,
            'ciudad': empresa.ciudad_empresa,
            # Datos del representante
            'nombre_representante': empresa.nombre_representante,
            'email_representante': empresa.email_representante,
            'telefono_representante': empresa.telefono_representante,
            # ventas anuales empresa
            'ventas_anuales': empresa.ventas_anuales_empresa,
            # Dotacion Empresa
            'empContratados': dotacion_empresa.answer1,
            'empContratistas': dotacion_empresa.answer2,
            'vehLivianos': dotacion_empresa.answer3,
            'vehContratistas': dotacion_empresa.answer4,
            'vehPesados': dotacion_empresa.answer5,
            'vehPesadosContratistas': dotacion_empresa.answer6,
            'maqEmpresa': dotacion_empresa.answer7,
            'maqContratista': dotacion_empresa.answer8,
        }
        form = FormPageOne(data=data)
        
    context = {'form': form, 'empresa': empresa}
    return render(request, "MideTuRiesgo/mideturiesgo.html", context)


@login_required
def page_two_poll(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        construccion = request.POST.getlist('construccion[]')
        manufactura = request.POST.getlist('manufactura[]')
        transporte = request.POST.getlist('transporte[]')
        servicios = request.POST.getlist('servicios[]')
        # check whether it's valid:
        empresa = UserGuiar.objects.get(rut='12345678-5')

        #Construccion

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
            rut_empresa=empresa,
            answer1=estructura,
            answer2=gruesa,
            answer3=instalaciones,
            answer4=menores,
            answer5=tuberias,
            answer6=refuerzos
        )

        #Manufactura

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
            rut_empresa=empresa,
            answer1=produccion,
            answer2=confeccion,
            answer3=tornerias,
            answer4=pvc,
            answer5=muebles,
            answer6=prototipos
        )

        #Transporte

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
            rut_empresa=empresa,
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

        #Servicios

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
        for x in servicios:
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
            rut_empresa=empresa,
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

        construccion.save()
        manufactura.save()
        transporte.save()
        servicios.save()
        return HttpResponseRedirect('3')

    else:
        form = FormPageTwo()
        empresa = UserGuiar.objects.get(rut='12345678-5')
        respuestas = TablaResultadosProcesos.objects.get(rut_empresa=empresa)
        constru = respuestas.answer1
        manu = respuestas.answer2
        trans = respuestas.answer3
        serv = respuestas.answer4
        return render(request, "MideTuRiesgo/mideturiesgo2.html", {'constru':constru, 'manu': manu, 'trans': trans, 'serv': serv})

@login_required
def page_three_poll(request):
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
            rut_empresa=empresa,
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

        return HttpResponseRedirect('4')
    else:
        cont = 5
        empresa = UserGuiar.objects.get(rut='12345678-5')
        respuestas = TablaResultadosProcesos.objects.get(rut_empresa=empresa)
        constru = respuestas.answer1
        manu = respuestas.answer2
        trans = respuestas.answer3
        serv = respuestas.answer4
        if constru:
            cont += 1
        if manu:
            cont += 1
        if trans:
            cont += 1
        if serv:
            cont += 1
    return render(request, "MideTuRiesgo/mideturiesgo3.html", {'cont': cont})

@login_required
def page_four_poll(request):
    if request.method == 'POST':
        empresa = UserGuiar.objects.get(rut='12345678-5')

        explosivos = request.POST.getlist('explosivos[]')

        inscripcion = False
        certificado = False
        personal = False
        polvorin = False
        procedimientos = False
        dispositivos = False
        for x in explosivos:
            if x == "inscripcion":
                inscripcion = True
            elif x == "certificado":
                certificado = True
            elif x == "personal":
                personal = True
            elif x == "polvorin":
                polvorin = True
            elif x == "procedimientos":
                procedimientos = True
            elif x == "dispositivos":
                dispositivos = True

        explosivos = TablaResultadosExplosivos(
            rut_empresa=empresa,
            answer1=inscripcion,
            answer2=certificado,
            answer3=personal,
            answer4=polvorin,
            answer5=procedimientos,
            answer6=dispositivos
        )
        explosivos.save()

        electricidad = request.POST.getlist('electricidad[]')

        apertura = False
        encaramiento = False
        ausencia = False
        tierra = False
        delimitacion = False
        for x in electricidad:
            if x == "apertura":
                apertura = True
            elif x == "encaramiento":
                encaramiento = True
            elif x == "ausencia":
                ausencia = True
            elif x == "tierra":
                tierra = True
            elif x == "delimitacion":
                delimitacion = True

        electricidad = TablaResultadosElectricidad(
            rut_empresa=empresa,
            answer1=apertura,
            answer2=encaramiento,
            answer3=ausencia,
            answer4=tierra,
            answer5=delimitacion
        )
        electricidad.save()

        sustancias_peligrosas = request.POST.getlist('sustancias_peligrosas[]')

        distintivos = False
        tacografo = False
        antiguedad = False
        transporte = False
        embalaje = False
        carga = False
        tipoA = False
        tipoB = False
        tipoC = False
        for x in sustancias_peligrosas:
            if x == "distintivos":
                distintivos = True
            elif x == "tacografo":
                tacografo = True
            elif x == "antiguedad":
                antiguedad = True
            elif x == "transporte":
                transporte = True
            elif x == "embalaje":
                embalaje = True
            elif x == "carga":
                carga = True
            elif x == "tipoA":
                tipoA = True
            elif x == "tipoB":
                tipoB = True
            elif x == "tipoC":
                tipoC = True

        sustancias_peligrosas = TablaResultadosSustanciasPeligrosas(
            rut_empresa=empresa,
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

        altura = request.POST.getlist('altura[]')

        norma = False
        supervisor = False
        proteccion = False
        equipamiento = False
        for x in altura:
            if x == "norma":
                norma = True
            elif x == "supervisor":
                supervisor = True
            elif x == "proteccion":
                proteccion = True
            elif x == "equipamiento":
                equipamiento = True

        altura = TablaResultadosRiesgoAltura(
            rut_empresa=empresa,
            answer1=norma,
            answer2=supervisor,
            answer3=proteccion,
            answer4=equipamiento)
        altura.save()
        return HttpResponseRedirect('resultado')

    else:
        cont = 8
        empresa = UserGuiar.objects.get(rut='12345678-5')
        respuestas = TablaResultadosProcesos.objects.get(rut_empresa=empresa)
        constru = respuestas.answer1
        manu = respuestas.answer2
        trans = respuestas.answer3
        serv = respuestas.answer4
        if constru:
            cont += 1
        if manu:
            cont += 1
        if trans:
            cont += 1
        if serv:
            cont += 1
        return render(request, "MideTuRiesgo/mideturiesgo4.html", {'cont': cont})

def page_results(request):
    if request.method == 'GET':
        empresa = UserGuiar.objects.get(rut='12345678-5')
        transporte = TablaResultadosTransporte.objects.get(rut_empresa=empresa)
        construccion = TablaResultadosContruccion.objects.get(rut_empresa=empresa)
        manufactura = TablaResultadosManufactura.objects.get(rut_empresa=empresa)
        servicios = TablaResultadosServicios.objects.get(rut_empresa=empresa)
        dotacion = TablaResultadosDotacion.objects.get(rut_empresa=empresa)
        gestion = TablaResultadosGestion.objects.get(rut_empresa=empresa)
        procesos = TablaResultadosProcesos.objects.get(rut_empresa=empresa)
        explosivos = TablaResultadosExplosivos.objects.get(rut_empresa=empresa)
        electricidad = TablaResultadosElectricidad.objects.get(rut_empresa=empresa)
        sustancias = TablaResultadosSustanciasPeligrosas.objects.get(rut_empresa=empresa)
        altura = TablaResultadosRiesgoAltura.objects.get(rut_empresa=empresa)

        fin_procesos = 0
        fin_construccion = 0
        fin_manufactura = 0
        fin_transporte = 0
        fin_servicios = 0
        fin_dotacion = 0
        fin_gestion = 0
        fin_explosivos = 0
        fin_electricidad = 0
        fin_sustancias = 0
        fin_altura = 0
        total = 0
        minimo = 0
        resultado = 0
        constru = procesos.answer1
        manu = procesos.answer2
        trans = procesos.answer3
        serv = procesos.answer4
        if constru:
            fin_procesos += 5
            if construccion.answer1:
                fin_construccion += 2
            if construccion.answer2:
                fin_construccion += 2
            if construccion.answer3:
                fin_construccion += 2
            if construccion.answer4:
                fin_construccion += 3
            if construccion.answer5:
                fin_construccion += 1
            if construccion.answer6:
                fin_construccion += 1
            resultado += fin_construccion
            total += 16
            minimo += 6

        if manu:
            fin_procesos += 3
            if manufactura.answer1:
                fin_manufactura += 2
            if manufactura.answer2:
                fin_manufactura += 2
            if manufactura.answer3:
                fin_manufactura += 3
            if manufactura.answer4:
                fin_manufactura += 3
            if manufactura.answer5:
                fin_manufactura += 1
            if manufactura.answer6:
                fin_manufactura += 1
            resultado += fin_manufactura
            total += 15
            minimo += 4


        if trans:
            fin_procesos += 4
            if transporte.answer1:
                fin_transporte += 1
            if transporte.answer2:
                fin_transporte += 3
            if transporte.answer3:
                fin_transporte += 2
            if transporte.answer4:
                fin_transporte += 1
            if transporte.answer5:
                fin_transporte += 1
            if transporte.answer6:
                fin_transporte += 1
            if transporte.answer7:
                fin_transporte += 4
            if transporte.answer8:
                fin_transporte += 2
            if transporte.answer9:
                fin_transporte += 2
            resultado += fin_transporte
            total += 21
            minimo += 5

        if serv:
            fin_procesos += 2
            if servicios.answer1:
                fin_servicios += 2
            if servicios.answer2:
                fin_servicios += 3
            if servicios.answer3:
                fin_servicios += 3
            if servicios.answer4:
                fin_servicios += 5
            if servicios.answer5:
                fin_servicios += 3
            if servicios.answer6:
                fin_servicios += 3
            if servicios.answer7:
                fin_servicios += 1
            if servicios.answer8:
                fin_servicios += 1
            if servicios.answer9:
                fin_servicios += 3
            if servicios.answer10:
                fin_servicios += 3
            if servicios.answer11:
                fin_servicios += 1
            if servicios.answer12:
                fin_servicios += 2
            if servicios.answer13:
                fin_servicios += 3
            if servicios.answer14:
                fin_servicios += 2
            resultado += fin_servicios
            total += 37
            minimo += 3
        resultado += fin_procesos


        if int(dotacion.answer1) < 50:
            fin_dotacion += 1
        elif int(dotacion.answer1) >= 50 and int(dotacion.answer1) < 125:
            fin_dotacion += 2
        elif int(dotacion.answer1) >= 125 and int(dotacion.answer1) < 200:
            fin_dotacion += 3
        else:
            fin_dotacion += 4

        if int(dotacion.answer2) < 50:
            fin_dotacion += 1
        elif int(dotacion.answer2) >= 50 and int(dotacion.answer2) < 125:
            fin_dotacion += 2
        elif int(dotacion.answer2) >= 125 and int(dotacion.answer2) < 200:
            fin_dotacion += 3
        else:
            fin_dotacion += 5

        if int(dotacion.answer3) < 20:
            fin_dotacion += 1
        elif int(dotacion.answer3) >= 20 and int(dotacion.answer3) < 30:
            fin_dotacion += 3
        elif int(dotacion.answer3) >= 30 and int(dotacion.answer3) < 40:
            fin_dotacion += 5
        elif int(dotacion.answer3) >= 40 and int(dotacion.answer3) < 50:
            fin_dotacion += 6
        else:
            fin_dotacion += 7

        if int(dotacion.answer4) < 20:
            fin_dotacion += 1
        elif int(dotacion.answer4) >= 20 and int(dotacion.answer4) < 30:
            fin_dotacion += 3
        elif int(dotacion.answer4) >= 30 and int(dotacion.answer4) < 40:
            fin_dotacion += 5
        elif int(dotacion.answer4) >= 40 and int(dotacion.answer4) < 50:
            fin_dotacion += 6
        else:
            fin_dotacion += 7

        if int(dotacion.answer5) < 20:
            fin_dotacion += 3
        elif int(dotacion.answer5) >= 20 and int(dotacion.answer5) < 30:
            fin_dotacion += 6
        elif int(dotacion.answer5) >= 30 and int(dotacion.answer5) < 40:
            fin_dotacion += 9
        elif int(dotacion.answer5) >= 40 and int(dotacion.answer5) < 50:
            fin_dotacion += 12
        else:
            fin_dotacion += 15

        if int(dotacion.answer6) < 20:
            fin_dotacion += 3
        elif int(dotacion.answer6) >= 20 and int(dotacion.answer6) < 30:
            fin_dotacion += 6
        elif int(dotacion.answer6) >= 30 and int(dotacion.answer6) < 40:
            fin_dotacion += 9
        elif int(dotacion.answer6) >= 40 and int(dotacion.answer6) < 50:
            fin_dotacion += 12
        else:
            fin_dotacion += 15

        if int(dotacion.answer7) < 20:
            fin_dotacion += 1
        elif int(dotacion.answer7) >= 20 and int(dotacion.answer7) < 30:
            fin_dotacion += 3
        elif int(dotacion.answer7) >= 30 and int(dotacion.answer7) < 40:
            fin_dotacion += 5
        elif int(dotacion.answer7) >= 40 and int(dotacion.answer7) < 50:
            fin_dotacion += 6
        else:
            fin_dotacion += 7

        if int(dotacion.answer8) < 20:
            fin_dotacion += 1
        elif int(dotacion.answer8) >= 20 and int(dotacion.answer8) < 30:
            fin_dotacion += 3
        elif int(dotacion.answer8) >= 30 and int(dotacion.answer8) < 40:
            fin_dotacion += 5
        elif int(dotacion.answer8) >= 40 and int(dotacion.answer8) < 50:
            fin_dotacion += 6
        else:
            fin_dotacion += 7
        resultado += fin_dotacion
        total += 67
        minimo += 12

        if gestion.answer1:
            fin_gestion += 1
        if gestion.answer2:
            fin_gestion += 2
        if gestion.answer3:
            fin_gestion += 3
        if gestion.answer4:
            fin_gestion += 2
        if gestion.answer5:
            fin_gestion += 1
        if gestion.answer6:
            fin_gestion += 2
        if gestion.answer7:
            fin_gestion += 4
        if gestion.answer8:
            fin_gestion += 2
        if gestion.answer9:
            fin_gestion += 3
        if gestion.answer10:
            fin_gestion += 1
        resultado -= fin_gestion
        total -= 3
        minimo += 15

        if explosivos.answer1:
            fin_explosivos += 2
        if construccion.answer2:
            fin_explosivos += 2
        if explosivos.answer3:
            fin_explosivos += 2
        if explosivos.answer4:
            fin_explosivos += 3
        if explosivos.answer5:
            fin_explosivos += 1
        if explosivos.answer6:
            fin_explosivos += 1
        if explosivos.answer1 or explosivos.answer2 or explosivos.answer3 or explosivos.answer4 or explosivos.answer5 or explosivos.answer6:
            total += 11
            minimo += 1
            resultado += fin_explosivos

        if electricidad.answer1:
            fin_electricidad += 2
        if electricidad.answer2:
            fin_electricidad += 2
        if electricidad.answer3:
            fin_electricidad += 2
        if electricidad.answer4:
            fin_electricidad += 3
        if electricidad.answer5:
            fin_electricidad += 1
        if electricidad.answer1 or electricidad.answer2 or electricidad.answer3 or electricidad.answer4 or electricidad.answer5:
            total += 10
            minimo += 1
            resultado += fin_electricidad

        if sustancias.answer1:
            fin_sustancias += 1
        if sustancias.answer2:
            fin_sustancias += 2
        if sustancias.answer3:
            fin_sustancias += 3
        if sustancias.answer4:
            fin_sustancias += 2
        if sustancias.answer5:
            fin_sustancias += 1
        if sustancias.answer6:
            fin_sustancias += 2
        if sustancias.answer7:
            fin_sustancias += 4
        if sustancias.answer8:
            fin_sustancias += 2
        if sustancias.answer9:
            fin_sustancias += 3
        if sustancias.answer1 or sustancias.answer2 or sustancias.answer3 or sustancias.answer4 or sustancias.answer5 or sustancias.answer6 or sustancias.answer7 or sustancias.answer8 or sustancias.answer9:
            total += 20
            minimo += 3
            resultado += fin_sustancias

        if altura.answer1:
            fin_altura += 1
        if altura.answer2:
            fin_altura += 2
        if altura.answer3:
            fin_altura += 3
        if altura.answer4:
            fin_altura += 2
        if altura.answer1 or altura.answer2 or altura.answer3 or altura.answer4:
            total += 8
            minimo += 1
            resultado += fin_altura

        final = TablaResultadosFinales(
            rut_empresa = empresa,
            riesgo_transporte=fin_transporte,
            riesgo_construccion=fin_construccion,
            riesgo_manufactura=fin_manufactura,
            riesgo_servicios=fin_servicios,
            riesgo_dotacion=fin_dotacion,
            riesgo_gestion=fin_gestion,
            riesgo_procesos=fin_procesos,
            riesgo_explosivos=fin_explosivos,
            riesgo_electricidad=fin_electricidad,
            riesgo_sustancias_peligrosas=fin_sustancias,
            riesgo_altura=fin_altura
        )
        final.save()
        res_por = ((resultado-minimo)/(total-minimo))
        res_img = (379+19)*res_por
        res_fin = (379+19) - res_img
        res_fin = int(res_fin)
        cuartil = (total-minimo)/4
        if resultado < (minimo + cuartil):
            color = "VERDE"
        elif resultado >= (minimo + cuartil) and resultado < (2*cuartil + minimo):
            color = "AMARILLO"
        elif resultado >= (2*cuartil + minimo) and resultado <= (3*cuartil + minimo):
            color = "ANARANJADO"
        else:
            color = "ROJO"
        print(res_fin)
        print(total)
        print(minimo)
        print(resultado)
        print(cuartil)
        print(cuartil+minimo)

    else:
        # Error de metodo
        e = "Operacion Invalida"
    return render(request, "MideTuRiesgo/mideturiesgoresultado.html", {'total':total, 'minimo':minimo, 'resultado':resultado, 'res_fin':res_fin, 'color':color})