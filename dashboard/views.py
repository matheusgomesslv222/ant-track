from django.shortcuts import render
from django.http import HttpResponse
from api_rest.models import Maquina
from django.db.models import Avg , Max , Min

def index(request):
    maquinas = Maquina.objects.all().order_by('created_at')
    
    # Preparar dados para o gráfico
    labels = [maquina.created_at.strftime('%H:%M') for maquina in maquinas]
    hashrates = Maquina.calcular_media_rate()
    temperatures_min = [float(maquina.chip_temperature_min) for maquina in maquinas]
    temperatures_max = [float(maquina.chip_temperature_max) for maquina in maquinas]
    pcb_temperatures = Maquina.calcular_media_temperaturas_pcb()
    chip_temperatures = Maquina.calcular_media_temperaturas_chip()

    context = {
        'maquinas': maquinas,
        'labels': labels,
        'hashrates': hashrates,
        'temperatures_min': temperatures_min,
        'temperatures_max': temperatures_max,
        'pcb_temperatures': pcb_temperatures,
        'chip_temperatures': chip_temperatures,
        
    }
    return render(request, 'dashboard/dashboard.html', context)
