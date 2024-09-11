from django.contrib import admin

# Register your models here.
from .models import UsuarioInfo, Maquina, Pool, Historico, HistoricoBinance

admin.site.register(UsuarioInfo)
admin.site.register(Maquina)
admin.site.register(Pool)
admin.site.register(Historico)
admin.site.register(HistoricoBinance)
