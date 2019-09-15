from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForm
from .models import UserGuiar


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
            'fields': ('rut', 'name', 'address', 'password1', 'password2',)}),
    )

    fieldsets = (
        (None, {'fields': ('rut', 'password')}),
        ('Informacion', {'fields': ('name', 'address')}),
        ('Permisos', {'fields': ('is_admin',)})
    )


admin.site.site_header = "MideTuRiesgo"
admin.site.site_index = "GuiarConsultores"
admin.site.site_title = "MideTuRiesgo"