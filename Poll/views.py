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
from django.db.models import Sum

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
    try:
        Obj_empresa = TablaPerfilEmpresa.objects.get(id=request.user)

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

    if request.method == 'POST':
        form_user = FormUserGuiar(request.POST, instance=user)
        form_perfil_empresa = FormTablaPerfilEmpresa(request.POST, instance=perfil_empresa)
        form_dotacion_empresa = FormTablaResultadosDotacion(request.POST, instance=dotacion_empresa)
        form_procesos_empresa = FormTablaResultadosProcesos(request.POST, instance=procesos_empresa)

        if form_user.is_valid() and form_perfil_empresa.is_valid() and form_dotacion_empresa.is_valid() and form_procesos_empresa.is_valid():

            form_user.save(commit=False)
            form_user.save()

            form_perfil_empresa.save(commit=False)
            form_perfil_empresa.save()

            form_dotacion_empresa.save(commit=False)
            form_dotacion_empresa.save()

            form_procesos_empresa.save(commit=False)
            form_procesos_empresa.save()

            return redirect('pagina2.1')
        else:
            context = {
                'form_perfil_empresa': form_perfil_empresa,
                'form_user': form_user,
                'form_dotacion_empresa': form_dotacion_empresa,
                'form_procesos_empresa': form_procesos_empresa,
            }
            return render(request, "MideTuRiesgo/mideturiesgo.html", context)
    else:
        form_user = FormUserGuiar(instance=user)
        form_perfil_empresa = FormTablaPerfilEmpresa(instance=perfil_empresa)
        form_dotacion_empresa = FormTablaResultadosDotacion(instance=dotacion_empresa)
        form_procesos_empresa = FormTablaResultadosProcesos(instance=procesos_empresa)

        context = {
            'form_perfil_empresa': form_perfil_empresa,
            'form_user': form_user,
            'form_dotacion_empresa': form_dotacion_empresa,
            'form_procesos_empresa': form_procesos_empresa,
        }

        return render(request, "MideTuRiesgo/mideturiesgo.html", context)


@login_required
def page_two_poll(request):
    # Query por un usuario existente
    user = UserGuiar.objects.get(rut=request.user)

    # Query por respuestas transporte existentes
    try:
        transporte = TablaResultadosTransporte.objects.get(id=user)
    except TablaResultadosTransporte.DoesNotExist:
        transporte = TablaResultadosTransporte(id=user)
        transporte.save()

    # Query por respuestas construccion existentes
    try:
        construccion = TablaResultadosConstruccion.objects.get(id=user)
    except TablaResultadosConstruccion.DoesNotExist:
        construccion = TablaResultadosConstruccion(id=user)
        construccion.save()

    # Query por respuestas manufactura existentes
    try:
        manufactura = TablaResultadosManufactura.objects.get(id=user)
    except TablaResultadosManufactura.DoesNotExist:
        manufactura = TablaResultadosManufactura(id=user)
        manufactura.save()

    # Query por respuestas servicios generales existentes
    try:
        servicios = TablaResultadosServicios.objects.get(id=user)
    except TablaResultadosServicios.DoesNotExist:
        servicios = TablaResultadosServicios(id=user)
        servicios.save()

    if request.method == 'POST':
        form_user = FormUserGuiar(request.POST, instance=user)
        form_transporte = FormTablaResultadosTransporte(request.POST, instance=transporte)
        form_construccion = FormTablaResultadosConstruccion(request.POST, instance=construccion)
        form_manufactura = FormTablaResultadosManufactura(request.POST, instance=manufactura)
        form_servicios = FormTablaResultadosServicios(request.POST, instance=servicios)

        if form_user.is_valid() and form_transporte.is_valid() and form_construccion.is_valid() and form_manufactura.is_valid() and form_servicios.is_valid():
            myuser = form_user.save(commit=False)
            myuser.save()

            form_transporte.save(commit=False)
            form_transporte.save()

            form_construccion.save(commit=False)
            form_construccion.save()

            form_manufactura.save(commit=False)
            form_manufactura.save()

            form_servicios.save(commit=False)
            form_servicios.save()

            return redirect('pagina3')
        else:
            context = {
                'form_transporte': form_transporte,
                'form_construccion': form_construccion,
                'form_manufactura': form_manufactura,
                'form_servicios': form_servicios,
                'form_user': form_user,
            }
            return render(request, "MideTuRiesgo/mideturiesgo2.1.html", context)
    else:
        form_user = FormUserGuiar(instance=user)
        form_transporte = FormTablaResultadosTransporte(instance=transporte)
        form_construccion = FormTablaResultadosConstruccion(instance=construccion)
        form_manufactura = FormTablaResultadosManufactura(instance=manufactura)
        form_servicios = FormTablaResultadosServicios(instance=servicios)

        context = {
            'form_transporte': form_transporte,
            'form_construccion': form_construccion,
            'form_manufactura': form_manufactura,
            'form_servicios': form_servicios,
            'form_user': form_user,
        }

        return render(request, "MideTuRiesgo/mideturiesgo2.1.html", context)


@login_required(login_url='MTRlogin')
def page_three_poll(request):
    # Obtener certificados de la empresa o crear para agregarlas
    cert_empresa, _ = TablaResultadosCertificaciones.objects.get_or_create(id=request.user)
    man_riesgo, _ = TablaResultadosManejoRiesgo.objects.get_or_create(id=request.user)
    preven_empresa, _ = TablaResultadosTiempoPreven.objects.get_or_create(id=request.user)

    # POST
    if request.method == "POST":
        form_cert_empresa = FormTablaResultadosCertificaciones(request.POST, instance=cert_empresa)
        form_man_riesgo = FormTablaResultadosManejoRiesgo(request.POST, instance=man_riesgo)
        form_preven_empresa = FormTablaResultadosTiempoPreven(request.POST, instance=preven_empresa)

        if form_cert_empresa.is_valid():

            form_cert_empresa.save(commit=False)
            form_cert_empresa.save()

            form_man_riesgo.save(commit=False)
            form_man_riesgo.save()

            form_preven_empresa.save(commit=False)
            form_preven_empresa.save()

            return redirect('home')
        else:

            context = {
                'form_cert_empresa': form_cert_empresa,
                'form_man_riesgo': form_man_riesgo,
                'form_preven_empresa': form_preven_empresa,
            }

            return render(request, "MideTuRiesgo/mideturiesgo3.html", context)
    # GET
    else:
        form_cert_empresa = FormTablaResultadosCertificaciones(instance=cert_empresa)
        form_man_riesgo = FormTablaResultadosManejoRiesgo(instance=man_riesgo)
        form_preven_empresa = FormTablaResultadosTiempoPreven(instance=preven_empresa)

        context = {
            'form_cert_empresa': form_cert_empresa,
            'form_man_riesgo': form_man_riesgo,
            'form_preven_empresa': form_preven_empresa,
        }

        return render(request, "MideTuRiesgo/mideturiesgo3.html", context)


@login_required(login_url='MTRlogin')
def page_four_poll(request):
    mani_explosivos_emp, _ = TablaResultadosManiExplosivos.objects.get_or_create(id=request.user)

    if request.method == 'POST':
        form_mani_explosivos = FormTablaResultadosManiExplosivos(request.POST, instance=mani_explosivos_emp)

        if form_mani_explosivos.is_valid():
            form_mani_explosivos.save(commit=False)
            form_mani_explosivos.save()

            return redirect('home')
        else:
            context = {
                'form_mani_explosivos': form_mani_explosivos,
            }

            return render(request, 'MideTuRiesgo/mideturiesgo4.html', context)
    else:
        form_mani_explosivos = FormTablaResultadosManiExplosivos(instance=mani_explosivos_emp)

        context = {
            'form_mani_explosivos': form_mani_explosivos,
        }

        return render(request, "MideTuRiesgo/mideturiesgo4.html", context)


@login_required(login_url='MTRlogin')
def page_results(request):
    # Indicadores
    total = 5
    minimo = 0
    resultado = 0

    # Resultados de la dotacion de la empresa Pag 1
    dotacion, _ = TablaResultadosDotacion.objects.get_or_create(id=request.user)
    result_dotacion = 0
    if dotacion.cant_emp_contratados < 50:
        result_dotacion += 1
    elif 50 <= dotacion.cant_emp_contratados < 125:
        result_dotacion += 2
    elif 125 <= dotacion.cant_emp_contratados < 200:
        result_dotacion += 3
    else:
        result_dotacion += 4

    if dotacion.cant_emp_contratista < 50:
        result_dotacion += 1
    elif 50 <= dotacion.cant_emp_contratista < 125:
        result_dotacion += 2
    elif 125 <= dotacion.cant_emp_contratista < 200:
        result_dotacion += 3
    else:
        result_dotacion += 5

    if dotacion.cant_veh_empresa < 20:
        result_dotacion += 1
    elif 20 <= dotacion.cant_veh_empresa < 30:
        result_dotacion += 3
    elif 30 <= dotacion.cant_veh_empresa < 40:
        result_dotacion += 5
    elif 40 <= dotacion.cant_veh_empresa < 50:
        result_dotacion += 6
    else:
        result_dotacion += 7

    if dotacion.cant_veh_contratista < 20:
        result_dotacion += 1
    elif 20 <= dotacion.cant_veh_contratista < 30:
        result_dotacion += 3
    elif 30 <= dotacion.cant_veh_contratista < 40:
        result_dotacion += 5
    elif 40 <= dotacion.cant_veh_contratista < 50:
        result_dotacion += 6
    else:
        result_dotacion += 7

    if dotacion.cant_veh_empresa_pesado < 20:
        result_dotacion += 3
    elif 20 <= dotacion.cant_veh_empresa_pesado < 30:
        result_dotacion += 6
    elif 30 <= dotacion.cant_veh_empresa_pesado < 40:
        result_dotacion += 9
    elif 40 <= dotacion.cant_veh_empresa_pesado < 50:
        result_dotacion += 12
    else:
        result_dotacion += 15

    if dotacion.cant_veh_contratista_pesado < 20:
        result_dotacion += 3
    elif 20 <= dotacion.cant_veh_contratista_pesado < 30:
        result_dotacion += 6
    elif 30 <= dotacion.cant_veh_contratista_pesado < 40:
        result_dotacion += 9
    elif 40 <= dotacion.cant_veh_contratista_pesado < 50:
        result_dotacion += 12
    else:
        result_dotacion += 15

    if dotacion.cant_maq_pesada_empresa < 20:
        result_dotacion += 1
    elif 20 <= dotacion.cant_maq_pesada_empresa < 30:
        result_dotacion += 3
    elif 30 <= dotacion.cant_maq_pesada_empresa < 40:
        result_dotacion += 5
    elif 40 <= dotacion.cant_maq_pesada_empresa < 50:
        result_dotacion += 6
    else:
        result_dotacion += 7

    if dotacion.cant_maq_pesada_contratista < 20:
        result_dotacion += 1
    elif 20 <= dotacion.cant_maq_pesada_contratista < 30:
        result_dotacion += 3
    elif 30 <= dotacion.cant_maq_pesada_contratista < 40:
        result_dotacion += 5
    elif 40 <= dotacion.cant_maq_pesada_contratista < 50:
        result_dotacion += 6
    else:
        result_dotacion += 7
    resultado += result_dotacion
    total += 67
    minimo += 12

    # Resultados de Construccion Pag 2
    result_const, _ = TablaResultadosConstruccion.objects.get_or_create(id=request.user)
    suma_const = result_const.construccion.all().aggregate(Sum('ri'))['ri__sum']
    if suma_const is None:
        suma_const = 0
    else:
        total += 16
        minimo += 6

    resultado += suma_const

    # Resultados de Manufactura Pag 2
    result_manu, _ = TablaResultadosManufactura.objects.get_or_create(id=request.user)
    suma_manu = result_manu.manufactura.all().aggregate(Sum('ri'))['ri__sum']
    if suma_manu is None:
        suma_manu = 0
    else:
        total += 15
        minimo += 4

    resultado += suma_manu

    # Resultados de Transporte Pag 2
    result_trans, _ = TablaResultadosTransporte.objects.get_or_create(id=request.user)
    suma_trans = result_trans.transporte.all().aggregate(Sum('ri'))['ri__sum']
    if suma_trans is None:
        suma_trans = 0
    else:
        total += 21
        minimo += 5

    resultado += suma_trans

    # Resultados de Servicios Generales Pag 2
    result_sergen,_ = TablaResultadosServicios.objects.get_or_create(id=request.user)
    suma_sergen = result_sergen.servicios.all().aggregate(Sum('ri'))['ri__sum']
    if suma_sergen is None:
        suma_sergen = 0
    else:
        total += 37
        minimo += 3

    resultado += suma_sergen

    # Resultados de los Certificados ISO pag 3
    result_cert, _ = TablaResultadosCertificaciones.objects.get_or_create(id=request.user)
    suma_result_cert = result_cert.certificaciones.all().aggregate(Sum('cr'))['cr__sum']
    if suma_result_cert is None:
        suma_result_cert = 0

    resultado += suma_result_cert

    # Resultado de manejo de Riesgos pag 3
    result_mriesgo, _ = TablaResultadosManejoRiesgo.objects.get_or_create(id=request.user)
    suma_mriesgo = result_mriesgo.opciones_manejo.all().aggregate(Sum('cr'))['cr__sum']
    if suma_mriesgo is None:
        suma_mriesgo = 0

    resultado += suma_mriesgo

    # Resultado de Tiempo de Prevencionista (Disponibilidad) Pag 3
    result_preven, _ = TablaResultadosTiempoPreven.objects.get_or_create(id=request.user)
    suma_preven = result_preven.opciones_prevencionista_t.cr
    if suma_preven is None:
        suma_preven = 0

    resultado += suma_preven

    # Resultados de Gestion pag 4

    # Resultados de Explosivos Pag 4

    # Resultados de Electricidad Pag 4

    # Resultados de Sustancias Pag 4

    # Resultados de Altura Pag 4

    # Despligue de Desiciones
    res_por = ((resultado - minimo) / (total - minimo))
    res_img = (379 + 19) * res_por
    res_fin = (379 + 19) - res_img
    res_fin = int(res_fin)
    cuartil = (total - minimo) / 4
    if resultado < (minimo + cuartil):
        color = "VERDE"
    elif (minimo + cuartil) <= resultado < (2 * cuartil + minimo):
        color = "AMARILLO"
    elif (2 * cuartil + minimo) <= resultado <= (3 * cuartil + minimo):
        color = "ANARANJADO"
    else:
        color = "ROJO"

    # return render(request,  'MideTuRiesgo/mideturiesgoresultado.html', {'suma': resultado})
    return render(request, "MideTuRiesgo/mideturiesgoresultado.html",{'total': total, 'minimo': minimo, 'resultado': resultado, 'res_fin': res_fin, 'color': color})
