from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUsuario,name='login'),
    path('registrar', views.registrarUsuario, name='registrar'),
    path('usuario-desconectado', views.usuario_desconectado, name='usuario-desconectado')
]