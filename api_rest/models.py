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
    miner_status = models.CharField(max_length=100)
    #id_usuario = models.ForeignKey(UsuarioInfo, on_delete=models.CASCADE)
    tera_hash = models.DecimalField(max_digits=10, decimal_places=2)
    chip_temperature_min = models.IntegerField()
    chip_temperature_max = models.IntegerField()
    cooling = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    pcb_temperature_min = models.IntegerField()
    pcb_temperature_max = models.IntegerField()
    power_consumption = models.IntegerField()
    power_efficiency = models.DecimalField(max_digits=10, decimal_places=2)
    power_usage = models.IntegerField()
    
    @staticmethod
    def calcular_media_temperaturas_chip():
        temperaturas = Maquina.objects.aggregate(
            avg_temp_min=models.Avg('chip_temperature_min'),
            avg_temp_max=models.Avg('chip_temperature_max')
        )
        return (temperaturas['avg_temp_min'] + temperaturas['avg_temp_max']) / 2
    
    @staticmethod
    def calcular_media_temperaturas_pcb():
        temperaturas = Maquina.objects.aggregate(
            avg_temp_min=models.Avg('pcb_temperature_min'),
            avg_temp_max=models.Avg('pcb_temperature_max')
        )
        return (temperaturas['avg_temp_min'] + temperaturas['avg_temp_max']) / 2
    
    @staticmethod
    def calcular_media_consumo_energia():
        return Maquina.objects.aggregate(
            avg_power_consumption=models.Avg('power_consumption')
        )['avg_power_consumption']
   
    

class Pool(models.Model):
    id_usuario = models.ForeignKey(UsuarioInfo, on_delete=models.CASCADE)
    accepted = models.IntegerField()
    asic_boost = models.BooleanField()
    diff = models.CharField(max_length=100)
    diffa = models.IntegerField()
    ls_diff = models.IntegerField()
    ls_time = models.CharField(max_length=100)
    ping = models.IntegerField()
    pool_type = models.CharField(max_length=100)
    rejected = models.IntegerField()
    stale = models.IntegerField()
    status = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    user = models.CharField(max_length=100)
    
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