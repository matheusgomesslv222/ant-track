from django.db import models

class UsuarioInfo (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    data_nascimento = models.DateField()


class Pool(models.Model):
    nome = models.CharField(max_length=100)
    url = models.URLField()

class Maquina(models.Model):
    nome_maquina = models.CharField(max_length=100)
    usuario = models.ForeignKey(UsuarioInfo, on_delete=models.CASCADE)
    pool = models.ForeignKey(Pool, on_delete=models.CASCADE, default=None)
    tera_hash = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)