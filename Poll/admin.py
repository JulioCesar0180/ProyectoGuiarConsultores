from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForm
from .models import UserGuiar


@admin.register(UserGuiar)
class UserGuiarAdmin(UserAdmin):
    #add_form = SignUpForm
    model = UserGuiar
    list_display = ['rut', 'name']
    list_filter = ['is_admin', 'name', 'address']
    ordering = ['rut']


admin.site.site_header = "MideTuRiesgo"
admin.site.site_index = "GuiarConsultores"
admin.site.site_title = "MideTuRiesgo"