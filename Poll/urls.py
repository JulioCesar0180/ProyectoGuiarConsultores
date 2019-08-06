from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [

    path('home', views.home, name="home"),
    path('encuesta', views.index,),

    path('registrarse', views.signup, name='signup'),
    path('perfil', views.profile),


    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('/', views.index),
    path('/2/', views.dos)
]