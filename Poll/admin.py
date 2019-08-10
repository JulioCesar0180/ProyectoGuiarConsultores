from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Tabla_usuario)
admin.site.register(Tabla_resultados_transporte)
admin.site.register(Tabla_resultados_construccion)
admin.site.register(Tabla_resultados_manufactura)
admin.site.register(Tabla_resultados_servicios)
admin.site.register(Tabla_resultados_dotacion)
admin.site.register(Tabla_resultados_gestion)
admin.site.register(Tabla_resultados_procesos)
admin.site.register(Tabla_resultados_explosivos)
admin.site.register(Tabla_resultados_electricidad)
admin.site.register(Tabla_resultados_sustancias_peligrosas)
admin.site.register(Tabla_resultados_altura)
admin.site.register(Tabla_resultados_finales)
admin.site.register(Tabla_priorizacion_riesgos)