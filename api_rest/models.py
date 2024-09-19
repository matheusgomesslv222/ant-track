from django.db import models

class UsuarioInfo(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    data_nascimento = models.DateField()
    
    def atualizar_senha(self, nova_senha):
        self.senha = nova_senha
        self.save()
    
    def alterar_nome_usuario(self,id_usuario,nome):
        usuario = UsuarioInfo.objects.get(id=id_usuario)
        usuario.nome = nome
        usuario.save()
    
    def alterar_email_usuario(self,id_usuario,email):
        usuario = UsuarioInfo.objects.get(id=id_usuario)
        usuario.email = email
        usuario.save()

class Maquina(models.Model):
    nome_maquina = models.CharField(max_length=100)
    id_usuario = models.ForeignKey(UsuarioInfo, on_delete=models.CASCADE)
    tera_hash = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    pool = models.ForeignKey('Pool', on_delete=models.CASCADE, null=True, blank=True, related_name='maquinas')
    
    def new_register_maquina(self, id_usuario, nome_maquina, tera_hash, temperatura, rate, pool):
        maquina = Maquina(id_usuario=id_usuario, nome_maquina=nome_maquina, tera_hash=tera_hash, temperatura=temperatura, rate=rate, pool=pool)
        maquina.save()
    
    def alterar_nome_maquina(self,id_maquina,nome_maquina):
        maquina = Maquina.objects.get(id=id_maquina)
        maquina.nome_maquina = nome_maquina
        maquina.save()
    

class Pool(models.Model):
    nome = models.CharField(max_length=100)
    id_maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE, related_name='pools')
    id_usuario = models.ForeignKey(UsuarioInfo, on_delete=models.CASCADE)
    
class Historico(models.Model):
    data = models.DateField()
    id_maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    id_pool = models.ForeignKey(Pool, on_delete=models.CASCADE)
    hashrate = models.DecimalField(max_digits=10, decimal_places=2)
    temperatura = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    pool = models.CharField(max_length=100)
    id_usuario = models.ForeignKey(UsuarioInfo, on_delete=models.CASCADE)
    
class HistoricoBinance(models.Model):
    data = models.DateField()
    id_usuario = models.ForeignKey(UsuarioInfo, on_delete=models.CASCADE)
    moeda = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=100)
    taxa = models.DecimalField(max_digits=10, decimal_places=2)
    taxa_total = models.DecimalField(max_digits=10, decimal_places=2)
    lucro = models.DecimalField(max_digits=10, decimal_places=2)
    lucro_total = models.DecimalField(max_digits=10, decimal_places=2)
    preco_medio = models.DecimalField(max_digits=10, decimal_places=2)
    preco_medio_total = models.DecimalField(max_digits=10, decimal_places=2)
    preco_medio_total_total = models.DecimalField(max_digits=10, decimal_places=2)
    preco_medio_total_total_total = models.DecimalField(max_digits=10, decimal_places=2)
    preco_medio_total_total_total_total = models.DecimalField(max_digits=10, decimal_places=2)
    preco_medio_total_total_total_total_total = models.DecimalField(max_digits=10, decimal_places=2)
    preco_medio_total_total_total_total_total_total = models.DecimalField(max_digits=10, decimal_places=2)
    preco_medio_total_total_total_total_total_total_total = models.DecimalField(max_digits=10, decimal_places=2)
    preco_medio_total_total_total_total_total_total_total_total = models.DecimalField(max_digits=10, decimal_places=2)
    preco_medio_total_total_total_total_total_total_total_total_total = models.DecimalField(max_digits=10, decimal_places=2)
    preco_medio