from django.urls import path, include
from django.contrib import admin
from Poll import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('test', views.page_one_poll, name="encuesta"),
    path('2', views.page_two_poll, name="pagina2"),
    path('3', views.page_three_poll, name="pagina3"),
    path('4', views.page_four_poll, name="pagina4"),
    path('resultado', views.page_results, name="resultado"),
    path('encuesta', views.get_name, name="test"),

    path('registrarse', views.signup, name='signup'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('login', views.MTR_login, name='MTRlogin'),
]
