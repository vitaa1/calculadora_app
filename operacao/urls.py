from django.urls import path
from . import views

urlpatterns = [
    path('calculadora', views.calculadora, name='calculadora'),
    path('limpar-historico', views.limpar_historico, name='limpar-historico')
]