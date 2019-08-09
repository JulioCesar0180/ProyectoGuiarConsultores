from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [

    path('home', views.home, name="home"),
    path('signup', views.signupTest, name='signup'),

    path('encuesta', views.index,),

    path('registrarse', views.signup),
    path('perfil', views.profile),

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('', views.index),
    path('2/', views.polltwo),
    path('3/', views.pollthree),
    path('4/', views.pollfour)
]