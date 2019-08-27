from django.urls import path, include
from django.contrib import admin
from Poll import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('encuesta', views.page_one_poll, name="encuesta"),

    path('registrarse', views.signup, name='signup'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('denunciar', views.denunciar, name='denunciar'),
]
