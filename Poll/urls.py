from django.urls import path, include
from . import views

urlpatterns = [
    path('encuesta', views.index,),
    path('registrarse', views.signup),
    path('perfil', views.profile),
    path('accounts/', include('django.contrib.auth.urls')),

    path('/', views.index),
    path('/2/', views.dos)
]