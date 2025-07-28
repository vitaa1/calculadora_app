from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Operacao

@login_required
def calculadora(request):
    resultadoS = None
    if request.method == 'POST':
        operacao = request.POST.get('operacao')
        try:
            if operacao in ['+', '-', '*', '/', '+/-', '%']:
                numero1 = float(request.POST.get('numero1', 0))
                numero2 = float(request.POST.get('numero2', 0))

                if operacao == '+':
                    resultado = numero1 + numero2
                elif operacao == '-':
                    resultado = numero1 - numero2
                elif operacao == '*':
                    resultado = numero1 * numero2
                elif operacao == '/':
                    if numero2 != 0:
                        resultado = numero1 / numero2
                    else:
                        resultado = "Erro: divisão por zero"
                elif operacao == '+/-':
                    resultado = -numero1
                    numero2 = None  
                elif operacao == "%":
                    resultado = (numero1 * numero2) / 100

                if isinstance(resultado, (int, float)):
                    resultado = round(resultado, 8)
                    resultadoS = '{:.8f}'.format(resultado).rstrip('0').rstrip('.')

                n1 = formatar_numero(numero1)
                n2 = formatar_numero(numero2)

                simbolo = 'x'
                simbolo1 = '÷'
                if operacao == '*':
                    parametro = f"{n1} {simbolo} {n2}"
                elif operacao == '/':
                    parametro = f"{n1} {simbolo1} {n2}"
                else:
                    parametro = f"{n1} {operacao} {n2}"
                Operacao.objects.create(
                    Usuario=request.user,
                    Parametros=parametro,
                    Resultado=resultadoS
                )
        except Exception:
            resultadoS = "Erro ao calcular"
        historico = Operacao.objects.filter(Usuario=request.user).order_by('-DtaInclusao')[:10]
        
        return render(request, 'operacao/calculadora.html', {'result': resultadoS, 'historico': historico})
    return render(request, 'operacao/calculadora.html')

def formatar_numero(n):
    return int(n) if float(n).is_integer() else float(n)

@login_required
def limpar_historico(request):
    Operacao.objects.filter(Usuario=request.user).delete()
    return redirect('calculadora')




