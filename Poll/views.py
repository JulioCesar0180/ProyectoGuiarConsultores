# encoding: utf-8
"""Se utiliza en el rut validator, es para iterar o una especie de foreach"""
from itertools import cycle

"""Libreria de expresiones regulares"""
import re

from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import commit
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView

from .models import UserGuiar
from .forms import *
from Poll.models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string

from django.contrib import messages

#rut
from django import template

"""Password change"""
from django.contrib.auth.hashers import check_password

"""Correo Electrónico"""
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

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

def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            empresa = TablaPerfilEmpresa.objects.get(email_representante=email)
            id_empresa = empresa.rut_empresa_id
            user = UserGuiar.objects.get(id=id_empresa)
            name = str(empresa.nombre_representante)

            """Crear Contraseña"""
            new_password = get_random_string(length=8)
            print("################################", new_password)

            """Cambiar la contraseña del usuario"""
            user.set_password(new_password)
            user.save()

            message = 'Se ha solicitado una nueva contraseña. Inicie Sesión con esta nueva ccontraseña: ' + new_password

            """Enviar el Correo"""
            send_mail(
                'Recuperación de contraseña para MideTuRiesgo',
                'Estimado(a) ' + name + ',\n' + message,
                'juliocesardm93@gmail.com', # Admin
                [
                    email
                ]
            )
            messages.info(request, 'Se ha enviado una contraseña a su correo')
        except:
            messages.error(request, 'El correo ingresado no se encuentra en nuestros registros')

    return render(request, 'reset_password.html')

def reset_password_form(request):
    """Id recibida"""
    id = ""

    obj_user = UserGuiar.objects.get(id=id)

    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != "" or password2 != "":
            if password1 == password2:
                obj_user.set_password(password1)
                obj_user.save()
                messages.success(request, 'Su contraseña ha sido actualizada!')
            else:
                messages.error(request, 'Las contraseñas no coinciden.')
        else:
            messages.error(request, 'No puede dejar la contraseñas en blanco.')

    return render(request, 'reset_password_form.html')

@login_required(login_url='MTRlogin')
def change_password(request):
    obj_user = request.user
    en_password = str(request.user.password)
    if request.method == 'POST':
        old_password = request.POST['old_password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if check_password(old_password, en_password):
            if password1 != "" or password2 != "":
                if password1 == password2:
                    obj_user.set_password(password1)
                    obj_user.save()
                    messages.success(request, 'Su contraseña ha sido actualizada!')
                    user = authenticate(username=request.user.rut, password=request.user.password)
                    if user is not None:
                        login(request, user)
                        return redirect('home')
                else:
                    messages.error(request, 'Las nuevas contraseñas no coinciden.')
            else:
                messages.error(request, 'No puede dejar la contraseñas en blanco.')
        else:
            messages.error(request, 'Ha ingresado su contraseña incorrectamente.')

    return render(request, 'change_password.html')

@login_required(login_url='MTRlogin')
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

@login_required(login_url='MTRlogin')
def Perfil(request):

    Obj_user = request.user
    idEmpresa = str(request.user.id)
    try:
        Obj_empresa = TablaPerfilEmpresa.objects.get(rut_empresa_id=idEmpresa)

        if request.method == 'POST':

            """Datos de contacto de la Obj_empresa"""

            """ Aquí solo falta validar el ingreso de datos para cada atributo, por ejemplo
             validar el ingreso de texto en blanco"""
            if(request.POST['nombre_representante'] and request.POST['email_representante'] and request.POST['telefono_representante'] != ""):
                if (phone_validator(request.POST['telefono_representante'])):
                    """Cada linea de este codigo, modifica los campos correpondientes"""
                    Obj_empresa.nombre_representante = request.POST['nombre_representante']
                    Obj_empresa.email_representante = request.POST['email_representante']
                    Obj_empresa.telefono_representante = phone_format(request.POST['telefono_representante'])
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

                    messages.success(request, "Los datos han sido actualizados con éxito!")
                else:
                    messages.error(request, "El formato del Número de Celular ingresado no es válido")
            else:
                messages.error(request, "Los campos Nombre, Email y Número de contacto no pueden estar vacíos")
        return render(request, 'perfil.html', {
            'Obj_empresa': Obj_empresa,
            'Obj_user': Obj_user,
        })
    except:
        return redirect('home')


def MTR_login(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            if(rut_validator(form.cleaned_data['rut'])):
                rut = rut_format(form.cleaned_data['rut'])
                password = form.cleaned_data["password"]
                user = authenticate(username=rut, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'El RUT o la clave ingresada no son correctos.')
            else:
                messages.error(request, "El formato del Rut ingresado no es válido")
        else:
            return render(request, 'registration/login.html', {'form': form})

    form = LogInForm()
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            """Validar rut"""
            if rut_validator(form.cleaned_data['rut']):
                if(phone_validator(form.cleaned_data['telefono_representante'])):
                    user = form.save()

                    """Se leen los demas datos de empresa"""
                    nombre_empresa = form.cleaned_data['name']
                    direccion_empresa = form.cleaned_data['address']
                    nombre_representante = form.cleaned_data['nombre_representante']
                    email_representante = form.cleaned_data['email_representante']
                    telefono_representante = phone_format(form.cleaned_data['telefono_representante'])

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

                    """Se corrige el formato del rut"""
                    Obj_user = request.user
                    Obj_user.rut = rut_format(form.cleaned_data['rut'])
                    Obj_user.save()

                    return redirect('home')
                else:
                    messages.error(request, "El formato del Número de Celular ingresado no es válido")
            else:
                messages.error(request, "El formato del Rut ingresado no es válido")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def rut_validator(rut):
    try:
        rut = rut.upper()
        rut = rut.replace("-", "").replace(".", "")
        num = rut[:-1]
        dv = rut[-1:]

        reversed_digits = map(int, reversed(str(num)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        res = (-s) % 11

        if str(res) == dv:
            return True
        elif dv == "K" and res == 10:
            return True
        else:
            return False
    except:
        return False


"""valida el numero de celular"""
def phone_validator(num):
    if(bool(re.match("^(\+?56)?(9)[9876543]\d{7}$", num))):
        return True
    return False

"""Le da el formato al numero de celular, incluyendo el +56"""
def phone_format(num):
    if num[0] == "9" and len(num) == 9:
        return "%s%s" % ("+56", num)
    elif num[0] == "5" and len(num) == 11:
        return "%s%s" % ("+", num)
    elif num[0] == "+" and len(num) == 12:
        return num
    elif len(num) == 8:
        return "%s%s" % ("+569", num)

"""Se encarga de dar formato al rut, por ejemplo, si se ingresa 18.502.184-K te lo deja 18502184-k"""
def rut_format(value, separator=""):
    # unformat the rut
    value = rut_unformat(value)
    rut, dv = value[:-1], value[-1]

    try:
        rut = "{0:,}".format(int(rut))

        if separator != ",":
            rut = rut.replace(",", separator)

        return "%s-%s" % (rut, dv)

    except ValueError:
        raise template.TemplateSyntaxError("El rut debe ser númerico")


def rut_unformat(value):
    return value.replace("-", "").replace(".", "").replace(",", "")

@login_required(login_url='MTRlogin')
def page_one_poll(request):

    # Query por un usuario existente
    user = UserGuiar.objects.get(rut=request.user)

    # Query por un perfil empresa existente
    try:
        perfil_empresa = TablaPerfilEmpresa.objects.get(id=user)
    except TablaPerfilEmpresa.DoesNotExist:
        perfil_empresa = TablaPerfilEmpresa(id=user)
        perfil_empresa.save()

    # Query por dotacion de la empresa
    try:
        dotacion_empresa = TablaResultadosDotacion.objects.get(id=user)
    except TablaResultadosDotacion.DoesNotExist:
        dotacion_empresa = TablaResultadosDotacion(id=user)
        dotacion_empresa.save()

    try:
        procesos_empresa = TablaResultadosProcesos.objects.get(id=user)
    except TablaResultadosProcesos.DoesNotExist:
        procesos_empresa = TablaResultadosProcesos(id=user)
        procesos_empresa.save()


@login_required(login_url='MTRlogin')
def page_two_poll(request):
    return render(request, 'MideTuRiesgo/mideturiesgo2.html')


@login_required(login_url='MTRlogin')
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

@login_required(login_url='MTRlogin')
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

@login_required(login_url='MTRlogin')
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