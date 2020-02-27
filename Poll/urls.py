from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib import admin
from Poll import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('1', views.page_one_poll, name="test"),
    path('2', views.page_two_poll, name="pagina2"),
    path('3', views.page_three_poll, name="pagina3"),
    path('4', views.page_four_poll, name="pagina4"),
    path('resultado', views.page_results, name="resultado"),

    path('signup', views.signup, name='signup'),

    path('login', views.MTR_login, name='MTRlogin'),
    path('logout', views.logout_view, name='logout'),
    path('profile/<slug:pk>', login_required(views.PerfilView.as_view()), name='perfil'),
    path('profile/business/<slug:pk>', login_required(views.PerfilEmpresaView.as_view()), name='business-profile'),

    path('password/change/<slug:pk>', login_required(views.ChangePasswordView.as_view()), name='change_password'),
    path('password/reset', views.reset_password, name='reset_password'),

    path('PDFreport/', views.report, name="pdfReport"),
]
