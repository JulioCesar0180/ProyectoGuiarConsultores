# encoding: utf-8
"""PDF"""
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from datetime import date



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

desgloce=[]
@login_required(login_url='MTRlogin')
def report(request):
    global desgloce
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=Reporte-Guiar-Consultores.pdf'

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    #Header
    logo = settings.MEDIA_ROOT + '/images/logoGC.png'
    c.drawImage(logo, 20, 750, 180, 90, preserveAspectRatio=True)
    c.setLineWidth(.3)

    c.setFont("Helvetica", 16)
    # Dibujamos una cadena en la ubicación X,Y especificada
    c.drawString(240, 750, u"MIDETURIESGO")
    c.setFont("Helvetica", 14)
    c.drawString(210, 730, u"REPORTE DE RESULTADOS")

    today = date.today()
    now = str(today.day)+"/"+str(today.month)+"/"+str(today.year)
    c.drawString(480, 790, now)

    #start X, height end Y, height
    c.line(475, 787, 560, 787)

    #Body
    """..."""

    #Table header
    styles = getSampleStyleSheet()
    styleBH = styles["Normal"]
    #styleBH.alignment = TA_CENTER
    styleBH.fontSize = 10

    numero = Paragraph('''No.''', styleBH)
    seccion = Paragraph('''Sección''', styleBH)
    porcentaje = Paragraph('''Porcentaje''', styleBH)

    data = []
    data.append([numero, seccion, porcentaje])

    #Table Content
    styleN = styles["BodyText"]
    #styleN.alignment = TA_CENTER
    styleN.fontSize = 7

    high = 650
    cont = 1
    for i in desgloce:
        i.insert(0, cont)
        cont += 1
        data.append(i)
        high = high-18


    #table size
    width, height = A4
    table = Table(data, colWidths = [1.2*cm, 9*cm, 2.2*cm])
    table.setStyle(TableStyle([ #estilos de la tabla
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black), ]))

    #pdf size
    table.wrapOn(c, width, height)
    table.drawOn(c, 30, high)
    c.showPage()


    #Guardar pdf
    c.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response



def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            empresa = TablaPerfilEmpresa.objects.get(email_representante=email)
            rut_empresa = empresa.id_id
            user = UserGuiar.objects.get(rut=rut_empresa)
            name = str(empresa.nombre_representante)

            """Crear Contraseña"""
            new_password = get_random_string(length=8)
            print("################################", new_password)

            """Cambiar la contraseña del usuario"""
            user.set_password(new_password)
            user.save()

            message = 'Se ha solicitado una nueva contraseña. Inicie Sesión con esta nueva contraseña: ' + new_password

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

"""Por ahora no se está usando"""
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
    empresa = TablaPerfilEmpresa.objects.get(id_id=request.user.rut)
    return render(request, 'home.html', {
        'empresa': empresa
    })


@login_required(login_url='MTRlogin')
def Perfil(request):

    Obj_user = request.user
    #try:
    Obj_empresa = TablaPerfilEmpresa.objects.get(id_id=request.user.rut)

    if request.method == 'POST':

        """Datos de contacto de la Obj_empresa"""

        """ Aquí solo falta validar el ingreso de datos para cada atributo, por ejemplo
         validar el ingreso de texto en blanco"""
        if(request.POST['nombre_representante'] and request.POST['email_representante'] and request.POST['telefono_representante'] != ""):
            if (phone_validator(request.POST['telefono_representante'])):
                """Cada linea de este codigo, modifica los campos correpondientes"""
                #Este es nuevo
                Obj_empresa.rut_representante = request.POST['rut_representante']
                Obj_empresa.nombre_representante = string_format(request.POST['nombre_representante'])
                Obj_empresa.email_representante = request.POST['email_representante']
                Obj_empresa.telefono_representante = phone_format(request.POST['telefono_representante'])
                Obj_empresa.experiencia_empresa = request.POST['experiencia_empresa']
                Obj_empresa.razon_social_empresa = request.POST['razon_social_empresa']
                #Obj_empresa.ventas_anuales_empresa = request.POST['ventas_anuales_empresa']
                Obj_empresa.comuna_empresa = string_format(request.POST['comuna_empresa'])
                Obj_empresa.ciudad_empresa = string_format(request.POST['ciudad_empresa'])

                "Nombre de la empresa se repite en las 2 tablas"
                #Obj_empresa.nombre_empresa = request.POST['nombre_empresa']
                Obj_empresa.id_id = request.user.rut

                "Datos User Guiar"
                Obj_user.name = string_format(request.POST['nombre_empresa'])
                Obj_user.address = string_format(request.POST['address'])

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
    """except:
        return redirect('home')
    """


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
        """Validar rut"""
        if rut_validator(request.POST['rut']):
            if rut_validator(request.POST['rut']):
                if(phone_validator(request.POST['telefono_representante'])):

                    """Se leen los datos de empresa"""
                    rut_empresa = request.POST['rut']
                    nombre_empresa = request.POST['name']
                    direccion_empresa = request.POST['address']

                    """Se leen los datos de Contacto"""
                    rut_representante = request.POST['rut_representante']
                    nombre_representante = request.POST['nombre_representante']
                    email_representante = request.POST['email_representante']
                    telefono_representante = phone_format(request.POST['telefono_representante'])


                    """Se leen las contraseñas"""
                    password1 = request.POST['password1']
                    password2 = request.POST['password2']
                    if password1 != "" or password2 != "":
                        if password1 == password2:

                            obj_user = UserGuiar(
                                rut=rut_format(rut_empresa),
                                name=nombre_empresa,
                                address=direccion_empresa,
                                password=password1
                            )

                            perfil_empresa = TablaPerfilEmpresa(
                                id=obj_user,
                                rut_representante=rut_format(rut_representante),
                                nombre_representante=nombre_representante,
                                email_representante=email_representante,
                                telefono_representante=telefono_representante
                            )

                            obj_user.set_password(password1)
                            obj_user.save()

                            login(request, obj_user)

                            perfil_empresa.save()

                            return redirect('home')
                        else:
                            messages.error(request, 'Las contraseñas no coinciden.')
                    else:
                        messages.error(request, 'No puede dejar la contraseñas en blanco.')
                else:
                    messages.error(request, "El formato del Número de Celular ingresado no es válido")
            else:
                messages.error(request, "El formato del Rut del Contacto ingresado no es válido")
        else:
            messages.error(request, "El formato del Rut de la Empresa ingresado no es válido")

    return render(request, 'registration/signup.html')


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

def string_format(string):
    return string.replace(' ','_',5)

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

            return redirect('pagina2')
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

    # Query por los procesos de la empresa
    procesos_empresa, _ = TablaResultadosProcesos.objects.get_or_create(id=user)

    # Query para obtener todos los procesos disponibles que considera GuiarConsultores
    tipos_procesos = TablaProcesos.objects.all()

    # Dichos tipos de procesos son listados en una lista
    list_procesos = []
    for p in tipos_procesos:
        list_procesos.append(p)

    # Forms
    # Query por respuestas construccion existentes
    construccion, _ = TablaResultadosConstruccion.objects.get_or_create(id=user)
    # Form Construccion
    form_construccion = FormTablaResultadosConstruccion(instance=construccion)
    form_construccion_valid = True

    # Query por respuestas manufacturas existentes
    manufactura, _ = TablaResultadosManufactura.objects.get_or_create(id=user)
    # Form Manufactura
    form_manufactura = FormTablaResultadosManufactura(instance=manufactura)
    form_manufactura_valid = True

    # Query por respuestas transportes existentes
    transporte, _ = TablaResultadosTransporte.objects.get_or_create(id=user)
    # Form Transporte
    form_transporte = FormTablaResultadosTransporte(instance=transporte)
    form_transporte_valid = True

    # Query por respuestas Servicios Generales existentes
    servicio, _ = TablaResultadosServicios.objects.get_or_create(id=user)
    # Form Servicios
    form_servicio = FormTablaResultadosServicios(instance=servicio)
    form_servicio_valid = True

    context = {
        'form_construccion': form_construccion,
        'form_manufactura': form_manufactura,
        'form_transporte': form_transporte,
        'form_servicio': form_servicio,
        'transporte': list_procesos[0],
        'construccion': list_procesos[1],
        'manufactura': list_procesos[2],
        'servicio': list_procesos[3],
        'procesos_empresa': procesos_empresa,
    }

    # list_procesos[0] = "Transporte Terrestre"
    if list_procesos[0] in procesos_empresa.procesos.all():
        if request.method == 'POST':
            form_transporte = FormTablaResultadosTransporte(request.POST, instance=transporte)
            if form_transporte.is_valid():
                form_transporte.save(commit=False)
                form_transporte.save()
                form_transporte_valid = True
            else:
                form_transporte_valid = False

    # list_procesos[1] = "Construccion"
    if list_procesos[1] in procesos_empresa.procesos.all():
        if request.method == "POST":
            form_construccion = FormTablaResultadosConstruccion(request.POST, instance=construccion)
            if form_construccion.is_valid():
                form_construccion.save(commit=False)
                form_construccion.save()
                form_construccion_valid = True
            else:
                form_construccion_valid = False

    # list_procesos[2] = "Manufactura"
    if list_procesos[2] in procesos_empresa.procesos.all():
        if request.method == "POST":
            form_manufactura = FormTablaResultadosManufactura(request.POST, instance=manufactura)
            if form_manufactura.is_valid():
                form_manufactura.save(commit=False)
                form_manufactura.save()
                form_manufactura_valid = True
            else:
                form_manufactura_valid = False

    # list_procesos[3] = "Servicios Generales"
    if list_procesos[3] in procesos_empresa.procesos.all():
        if request.method == 'POST':
            form_servicio = FormTablaResultadosServicios(request.POST, instance=servicio)
            if form_servicio.is_valid():
                form_servicio.save(commit=False)
                form_servicio.save()
                form_servicio_valid = True
            else:
                form_servicio_valid = False

    if request.method == 'POST' and form_construccion_valid and form_manufactura_valid and form_transporte_valid and form_servicio_valid:
        return redirect('pagina3')
    return render(request, "MideTuRiesgo/mideturiesgo2.1.html", context)


@login_required(login_url='MTRlogin')
def page_three_poll(request):
    # Obtener certificados de la empresa o crear para agregarlas
    cert_empresa, _ = TablaResultadosCertificaciones.objects.get_or_create(id=request.user)
    man_riesgo, _ = TablaResultadosManejoRiesgo.objects.get_or_create(id=request.user)
    preven_empresa, _ = TablaResultadosTiempoPreven.objects.get_or_create(id=request.user)
    procesos_empresa, _ = TablaResultadosProcesos.objects.get_or_create(id=request.user)
    cont = len(procesos_empresa.procesos.all())+5

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

            return redirect('pagina4')
        else:

            context = {
                'form_cert_empresa': form_cert_empresa,
                'form_man_riesgo': form_man_riesgo,
                'form_preven_empresa': form_preven_empresa,
                'cont': cont
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
            'cont': cont
        }

        return render(request, "MideTuRiesgo/mideturiesgo3.html", context)


@login_required(login_url='MTRlogin')
def page_four_poll(request):

    mani_explosivos_emp, _ = TablaResultadosManiExplosivos.objects.get_or_create(id=request.user)
    elect_emp, _ = TablaResultadoElectricidad.objects.get_or_create(id=request.user)
    sust_emp, _ = TablaResultadosSustancias.objects.get_or_create(id=request.user)
    alt_emp, _ = TablaResultadosAltura.objects.get_or_create(id=request.user)

    form_mani_explosivos = FormTablaResultadosManiExplosivos(instance=mani_explosivos_emp)
    form_elect_emp = FormTablaResultadoElectricidad(instance=elect_emp)
    form_sust_emp = FormTablaResultadosSustancias(instance=sust_emp)
    form_alt_emp = FormTablaResultadosAltura(instance=alt_emp)
    procesos_empresa, _ = TablaResultadosProcesos.objects.get_or_create(id=request.user)
    cont = len(procesos_empresa.procesos.all()) + 8

    if request.method == 'POST':
        form_mani_explosivos = FormTablaResultadosManiExplosivos(request.POST, instance=mani_explosivos_emp)
        form_elect_emp = FormTablaResultadoElectricidad(request.POST, instance=elect_emp)
        form_sust_emp = FormTablaResultadosSustancias(request.POST, instance=sust_emp)
        form_alt_emp = FormTablaResultadosAltura(request.POST, instance=alt_emp)
        if form_alt_emp.is_valid() and form_sust_emp.is_valid() and form_elect_emp.is_valid() and form_mani_explosivos.is_valid():
            form_mani_explosivos.save(commit=False)
            form_mani_explosivos.save()

            form_elect_emp.save(commit=False)
            form_elect_emp.save()

            form_sust_emp.save(commit=False)
            form_sust_emp.save()

            form_alt_emp.save(commit=False)
            form_alt_emp.save()

            return redirect('resultado')
        else:
            context = {
                'form_mani_explosivos': form_mani_explosivos,
                'form_elect_emp': form_elect_emp,
                'form_sust_emp': form_sust_emp,
                'form_alt_emp': form_alt_emp,
                'cont': cont
            }
            return render(request, "MideTuRiesgo/mideturiesgo4.html", context)
    else:
        context = {
            'form_mani_explosivos': form_mani_explosivos,
            'form_elect_emp': form_elect_emp,
            'form_sust_emp': form_sust_emp,
            'form_alt_emp': form_alt_emp,
            'cont': cont
        }
        return render(request, "MideTuRiesgo/mideturiesgo4.html", context)


@login_required(login_url='MTRlogin')
def page_results(request):
    # Indicadores
    total = 5
    minimo = 0
    resultado = 0

    # Se guardan resultados parciales con nombre de seccion y riesgo porcentual, el nombre se puede omitir pero implica recordar la posicion de cada seccion

    #Por Julio, te declaré desgloce como variable global porq lo necesito usar en report() y no se me ocurrio otra forma
    global desgloce
    desgloce.clear()

    for poliza in TablaPoliza.objects.all():
        desgloce.append([poliza.nombre_poliza,0,0,poliza.id])

    # Resultados de la dotacion de la empresa Pag 1
    dotacion, _ = TablaResultadosDotacion.objects.get_or_create(id=request.user)
    designacion = TablaDesignacionDotacion.objects.first()
    result_dotacion = 0
    cont_empl = 0
    cont_trans = 0

    if dotacion.cant_emp_contratados < 50:
        res_emp_contratados = 1
    elif 50 <= dotacion.cant_emp_contratados < 125:
        res_emp_contratados = 2
    elif 125 <= dotacion.cant_emp_contratados < 200:
        res_emp_contratados = 3
    else:
        res_emp_contratados = 4
    result_dotacion += res_emp_contratados
    cont_empl += res_emp_contratados

    for d in desgloce:
        if d[3] == designacion.campo1:
            d[1] += 4
            d[2] += res_emp_contratados

    if dotacion.cant_emp_contratista < 50:
        res_emp_contratista = 1
    elif 50 <= dotacion.cant_emp_contratista < 125:
        res_emp_contratista = 2
    elif 125 <= dotacion.cant_emp_contratista < 200:
        res_emp_contratista = 3
    else:
        res_emp_contratista = 5
    result_dotacion += res_emp_contratista
    cont_empl += res_emp_contratista

    for d in desgloce:
        if d[3] == designacion.campo2:
            d[1] += 5
            d[2] += res_emp_contratista

    if dotacion.cant_veh_empresa < 20:
        res_veh_empresa = 1
    elif 20 <= dotacion.cant_veh_empresa < 30:
        res_veh_empresa = 3
    elif 30 <= dotacion.cant_veh_empresa < 40:
        res_veh_empresa = 5
    elif 40 <= dotacion.cant_veh_empresa < 50:
        res_veh_empresa = 6
    else:
        res_veh_empresa = 7
    result_dotacion += res_veh_empresa
    cont_trans += res_veh_empresa

    for d in desgloce:
        if d[3] == designacion.campo3:
            d[1] += 7
            d[2] += res_veh_empresa

    if dotacion.cant_veh_contratista < 20:
        res_veh_contratista = 1
    elif 20 <= dotacion.cant_veh_contratista < 30:
        res_veh_contratista = 3
    elif 30 <= dotacion.cant_veh_contratista < 40:
        res_veh_contratista = 5
    elif 40 <= dotacion.cant_veh_contratista < 50:
        res_veh_contratista = 6
    else:
        res_veh_contratista = 7
    result_dotacion += res_veh_contratista
    cont_trans += res_veh_contratista

    for d in desgloce:
        if d[3] == designacion.campo4:
            d[1] += 7
            d[2] += res_veh_contratista

    if dotacion.cant_veh_empresa_pesado < 20:
        res_veh_empresa_pesado = 3
    elif 20 <= dotacion.cant_veh_empresa_pesado < 30:
        res_veh_empresa_pesado = 6
    elif 30 <= dotacion.cant_veh_empresa_pesado < 40:
        res_veh_empresa_pesado = 9
    elif 40 <= dotacion.cant_veh_empresa_pesado < 50:
        res_veh_empresa_pesado = 12
    else:
        res_veh_empresa_pesado = 15
    result_dotacion += res_veh_empresa_pesado
    cont_trans += res_veh_empresa_pesado

    for d in desgloce:
        if d[3] == designacion.campo5:
            d[1] += 15
            d[2] += res_veh_empresa_pesado

    if dotacion.cant_veh_contratista_pesado < 20:
        res_veh_contratista_pesado = 3
    elif 20 <= dotacion.cant_veh_contratista_pesado < 30:
        res_veh_contratista_pesado = 6
    elif 30 <= dotacion.cant_veh_contratista_pesado < 40:
        res_veh_contratista_pesado = 9
    elif 40 <= dotacion.cant_veh_contratista_pesado < 50:
        res_veh_contratista_pesado = 12
    else:
        res_veh_contratista_pesado= 15
    result_dotacion += res_veh_contratista_pesado
    cont_trans += res_veh_contratista_pesado

    for d in desgloce:
        if d[3] == designacion.campo6:
            d[1] += 15
            d[2] += res_veh_contratista_pesado

    if dotacion.cant_maq_pesada_empresa < 20:
        res_maq_pesada_empresa= 1
    elif 20 <= dotacion.cant_maq_pesada_empresa < 30:
        res_maq_pesada_empresa = 3
    elif 30 <= dotacion.cant_maq_pesada_empresa < 40:
        res_maq_pesada_empresa = 5
    elif 40 <= dotacion.cant_maq_pesada_empresa < 50:
        res_maq_pesada_empresa = 6
    else:
        res_maq_pesada_empresa = 7
    result_dotacion += res_maq_pesada_empresa

    for d in desgloce:
        if d[3] == designacion.campo7:
            d[1] += 7
            d[2] += res_maq_pesada_empresa

    if dotacion.cant_maq_pesada_contratista < 20:
        res_maq_pesada_contratista = 1
    elif 20 <= dotacion.cant_maq_pesada_contratista < 30:
        res_maq_pesada_contratista = 3
    elif 30 <= dotacion.cant_maq_pesada_contratista < 40:
        res_maq_pesada_contratista = 5
    elif 40 <= dotacion.cant_maq_pesada_contratista < 50:
        res_maq_pesada_contratista = 6
    else:
        res_maq_pesada_contratista = 7
    result_dotacion += res_maq_pesada_contratista

    for d in desgloce:
        if d[3] == designacion.campo8:
            d[1] += 7
            d[2] += res_maq_pesada_contratista
        if d[3] == 3:
            d[1] += 53
            d[2] += cont_trans + cont_empl

    resultado += result_dotacion
    total += 67
    minimo += 12

    riesgoporcentual_dotacion = round((result_dotacion / 67) * 100,2)
    # desgloce.append(["Dotacion",riesgoporcentual_dotacion])

    for d in desgloce:
        if d[3] == 1:
            d[1] += 67
            d[2] += result_dotacion

    # Resultados de Construccion Pag 2
    result_const, _ = TablaResultadosConstruccion.objects.get_or_create(id=request.user)
    suma_const = result_const.construccion.all().aggregate(Sum('ri'))['ri__sum']
    if suma_const is None:
        suma_const = 0
    else:
        total += 16
        minimo += 6

        riesgoporcentual_construccion = round((suma_const / 16) * 100,2)
        # desgloce.append(["Construccion", riesgoporcentual_construccion])
        for re in result_const.construccion.all():
            for d in desgloce:
                if d[3] == re.poliza.id:
                    d[1] += 16
                    d[2] += suma_const

    resultado += suma_const

    # Resultados de Manufactura Pag 2
    result_manu, _ = TablaResultadosManufactura.objects.get_or_create(id=request.user)
    suma_manu = result_manu.manufactura.all().aggregate(Sum('ri'))['ri__sum']
    if suma_manu is None:
        suma_manu = 0
    else:
        total += 15
        minimo += 4
        riesgoporcentual_manufactura = round((suma_manu / 15) * 100,2)
        # desgloce.append(["Manufactura", riesgoporcentual_manufactura])
        for re in result_manu.manufactura.all():
            for d in desgloce:
                if d[3] == re.poliza.id:
                    d[1] += 15
                    d[2] += suma_manu

    resultado += suma_manu

    # Resultados de Transporte Pag 2
    result_trans, _ = TablaResultadosTransporte.objects.get_or_create(id=request.user)
    suma_trans = result_trans.transporte.all().aggregate(Sum('ri'))['ri__sum']
    if suma_trans is None:
        suma_trans = 0
    else:
        total += 21
        minimo += 5
        riesgoporcentual_Transporte = round((suma_trans / 21) * 100,2)
        # desgloce.append(["Transporte", riesgoporcentual_Transporte])
        for re in result_trans.transporte.all():
            for d in desgloce:
                if d[3] == re.poliza.id:
                    d[1] += 21
                    d[2] += suma_trans

    resultado += suma_trans

    # Resultados de Servicios Generales Pag 2
    result_sergen,_ = TablaResultadosServicios.objects.get_or_create(id=request.user)
    suma_sergen = result_sergen.servicios.all().aggregate(Sum('ri'))['ri__sum']
    if suma_sergen is None:
        suma_sergen = 0
    else:
        total += 37
        minimo += 3
        riesgoporcentual_servicios = round((suma_sergen / 37) * 100,2)
        # desgloce.append(["Servicios", riesgoporcentual_servicios])
        for re in result_sergen.servicios.all():
            for d in desgloce:
                if d[3] == re.poliza.id:
                    d[1] += 37
                    d[2] += suma_sergen

    resultado += suma_sergen

    # Resultados de los Certificados ISO pag 3
    result_cert, _ = TablaResultadosCertificaciones.objects.get_or_create(id=request.user)
    suma_result_cert = result_cert.certificaciones.all().aggregate(Sum('cr'))['cr__sum']
    if suma_result_cert is None:
        suma_result_cert = 0
    else:
        riesgoporcentual_certificacion = round((1 - (suma_result_cert / 10)) * 100, 2)
        # desgloce.append(["Certificacion", riesgoporcentual_certificacion])
        for re in result_cert.certificaciones.all():
            for d in desgloce:
                if d[3] == re.poliza.id:
                    d[1] += 0
                    d[2] -= suma_result_cert
    resultado -= suma_result_cert

    # Resultado de manejo de Riesgos pag 3
    result_mriesgo, _ = TablaResultadosManejoRiesgo.objects.get_or_create(id=request.user)
    suma_mriesgo = result_mriesgo.opciones_manejo.all().aggregate(Sum('cr'))['cr__sum']
    if suma_mriesgo is None:
        suma_mriesgo = 0
    else:
        riesgoporcentual_manejoriesgo = round((1 - (suma_mriesgo / 5)) * 100, 2)
        # desgloce.append(["ManejoRiesgo", riesgoporcentual_manejoriesgo])
        for re in result_mriesgo.opciones_manejo.all():
            for d in desgloce:
                if d[3] == re.poliza.id:
                    d[1] += 0
                    d[2] -= suma_mriesgo
    resultado -= suma_mriesgo

    # Resultado de Tiempo de Prevencionista (Disponibilidad) Pag 3
    result_preven, _ = TablaResultadosTiempoPreven.objects.get_or_create(id=request.user)
    suma_preven = result_preven.opciones_prevencionista_t.cr
    if suma_preven is None:
        suma_preven = 0
    else:
        riesgoporcentual_prevencionista = round((1 - (suma_preven / 10)) * 100, 2)
        # desgloce.append(["TiempoPrevencionista", riesgoporcentual_prevencionista])
        for d in desgloce:
            if d[3] == result_preven.opciones_prevencionista_t.poliza.id:
                d[1] += 0
                d[2] -= suma_preven
    resultado -= suma_preven

    # Resultados de Explosivos Pag 4
    result_mani_explosivos, _ = TablaResultadosManiExplosivos.objects.get_or_create(id=request.user)
    suma_mani_explosivos = 0
    if result_mani_explosivos.is_expo:
        suma_mani_explosivos = result_mani_explosivos.tipos_exp.all().aggregate(Sum('ri'))['ri__sum']
        if suma_mani_explosivos is not None:
            total += 11
            minimo += 1
            resultado += suma_mani_explosivos
            riesgoporcentual_explosivos = round((suma_mani_explosivos / 11) * 100, 2)
            # desgloce.append(["Explosivos", riesgoporcentual_explosivos])
            for re in result_mani_explosivos.tipos_exp.all():
                for d in desgloce:
                    if d[3] == re.poliza.id:
                        d[1] += 11
                        d[2] += suma_mani_explosivos

    # Resultados de Electricidad Pag 4
    result_electricidad, _ = TablaResultadoElectricidad.objects.get_or_create(id=request.user)
    suma_electricidad = 0
    if result_electricidad.is_elec:
        suma_electricidad = result_electricidad.tipos_elec.all().aggregate(Sum('ri'))['ri__sum']
        if suma_electricidad is not None:
            total += 10
            minimo += 1
            resultado += suma_electricidad
            riesgoporcentual_electricidad = round((suma_electricidad / 10) * 100, 2)
            # desgloce.append(["Electricidad", riesgoporcentual_electricidad])
            for re in result_electricidad.tipos_elec.all():
                for d in desgloce:
                    if d[3] == re.poliza.id:
                        d[1] += 10
                        d[2] += suma_electricidad

    # Resultados de Sustancias Pag 4
    result_sustancia, _ = TablaResultadosSustancias.objects.get_or_create(id=request.user)
    suma_sustancia = 0
    if result_sustancia.is_sust:
        suma_sustancia = result_sustancia.tipos_sust.all().aggregate(Sum('ri'))['ri__sum']
        if suma_sustancia is not None:
            total += 20
            minimo += 3
            resultado += suma_sustancia
            riesgoporcentual_sustancias = round((suma_sustancia / 20) * 100, 2)
            # desgloce.append(["Sustancias", riesgoporcentual_sustancias])
            for re in result_sustancia.tipos_sust.all():
                for d in desgloce:
                    if d[3] == re.poliza.id:
                        d[1] += 20
                        d[2] += suma_sustancia

    # Resultados de Altura Pag 4
    result_altura, _ = TablaResultadosAltura.objects.get_or_create(id=request.user)
    suma_altura = 0
    if result_altura.is_alt:
        suma_altura = result_altura.tipos_alt.all().aggregate(Sum('ri'))['ri__sum']
        if suma_altura is not None:
            total += 8
            minimo += 1
            resultado += suma_altura
            riesgoporcentual_altura = round((suma_altura / 8) * 100, 2)
            # desgloce.append(["Altura", riesgoporcentual_altura])
            for re in result_altura.tipos_alt.all():
                for d in desgloce:
                    if d[3] == re.poliza.id:
                        d[1] += 8
                        d[2] += suma_altura

    # Despligue de Desiciones
    res_por = ((resultado) / (total))
    res_img = (379 + 19) * res_por
    res_fin = (379 + 19) - res_img
    res_fin = int(res_fin)
    cuartil = (total) / 4
    if resultado < (cuartil):
        color = "VERDE"
    elif (cuartil) <= resultado < (2 * cuartil):
        color = "AMARILLO"
    elif (2 * cuartil) <= resultado <= (3 * cuartil):
        color = "ANARANJADO"
    else:
        color = "ROJO"

    #sort arreglo desgloce
    desgloce_ordenado = []

    for des in desgloce:
        if des[1] != 0:
            desgloce_ordenado.append([des[0],round((des[2]/des[1])*100,1)])
    desgloce_ordenado.sort(key = lambda array: array[1], reverse=True)

    '''
    aux = 0
    for des in desgloce_ordenado:
        ant = des[1]
        if aux != 0:
            if des[1] == ant:
                if ant.priority < des[1]:
                    ordenar esa seccion por prioridad
        aux = 1
    '''

    # return render(request,  'MideTuRiesgo/mideturiesgoresultado.html', {'suma': resultado})
    return render(request, "MideTuRiesgo/mideturiesgoresultado.html",{'total': total, 'minimo': minimo, 'resultado': resultado, 'res_fin': res_fin, 'color': color, 'desgloce':desgloce_ordenado})
