from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForm
from .models import *


@admin.register(UserGuiar)
class UserGuiarAdmin(UserAdmin):
    add_form = SignUpForm
    model = UserGuiar
    list_display = ['rut', 'name', 'address', 'is_admin']
    list_filter = ['is_admin', 'name', 'address']
    ordering = ['rut']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('rut', 'name', 'address', 'password1', 'password2',)
        }),
    )

    fieldsets = (
        (None, {'fields': ('rut', 'password')}),
        ('Informacion', {'fields': ('name', 'address')}),
        ('Permisos', {'fields': ('is_admin',)})
    )


admin.site.register(TablaPerfilEmpresa)
admin.site.register(TablaVentasAnuales)
admin.site.register(TablaResultadosDotacion)
admin.site.register(TablaProcesos)
admin.site.register(TablaResultadosProcesos)
admin.site.register(TablaTransporte)
admin.site.register(TablaResultadosTransporte)
admin.site.register(TablaConstruccion)
admin.site.register(TablaResultadosConstruccion)
"""
admin.site.register(TablaResultadosTransporte)
admin.site.register(TablaResultadosContruccion)
admin.site.register(TablaResultadosManufactura)
admin.site.register(TablaResultadosServicios)

admin.site.register(TablaResultadosGestion)

admin.site.register(TablaResultadosExplosivos)
admin.site.register(TablaResultadosElectricidad)
admin.site.register(TablaResultadosSustanciasPeligrosas)
admin.site.register(TablaResultadosRiesgoAltura)
admin.site.register(TablaResultadosFinales)

"""
"""
admin.register(TablaPriorizacionRiesgos)
"""
admin.site.site_header = "MideTuRiesgo"
admin.site.site_index = "GuiarConsultores"
admin.site.site_title = "MideTuRiesgo"