from django.shortcuts import render, redirect
from . forms import CriarFormularioUsuario, LoginFormulario
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def paginaInicial(request):
    
    return render(request, 'usuario/index.html')

def loginUsuario(request):

    form = LoginFormulario()
    if request.method == "POST":
        form = LoginFormulario(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('calculadora')
            
    context = {'loginformulario': form}
    return render(request, 'usuario/login.html', context=context)

def registrarUsuario(request):

    form = CriarFormularioUsuario()
    if request.method == "POST":
        form = CriarFormularioUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    context = {'registroformulario': form}
    return render(request, 'usuario/registro.html', context=context)

@login_required(login_url='')
def calculadora(request):

    return render(request, 'usuario/calculadora.html')

def usuario_desconectado(request):
    auth.logout(request)

    return redirect('')


