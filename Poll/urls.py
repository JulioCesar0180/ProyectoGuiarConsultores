from django.urls import path, include
from django.contrib import admin
from Poll import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('encuesta', views.index,),

    path('registrarse', views.signup, name='signup'),
    path('perfil', views.profile),


    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('', views.index, name="encuesta"),
    path('2/', views.polltwo),
    path('3/', views.pollthree),
    path('4/', views.pollfour),

    path('testpage1', views.poll_page_one),
    path('resultado/', views.resultado),
    path('denunciar', views.denunciar, name='denunciar'),
]
