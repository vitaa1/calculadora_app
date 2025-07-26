from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaInicial, name=""),
    path('login', views.loginUsuario,name='login'),
    path('registrar', views.registrarUsuario, name='registrar'),
    path('calculadora', views.calculadora, name='calculadora'),
    path('usuario-desconectado', views.usuario_desconectado, name='usuario-desconectado')
]