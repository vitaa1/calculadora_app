from django.db import models
from django.contrib.auth.models import User

class Operacao(models.Model):
    IdOperacao = models.AutoField(primary_key=True)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Parametros = models.CharField(max_length=100)
    Resultado = models.CharField(max_length=100)
    DtaInclusao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.Parametros} = {self.Resultado}'


