from rest_framework import serializers

from .models import UsuarioInfo, Maquina, Pool, Historico, HistoricoBinance

class UsuarioInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioInfo
        fields = '__all__'

class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'

class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = '__all__'
        
class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'

class HistoricoBinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoBinance
        fields = '__all__'
