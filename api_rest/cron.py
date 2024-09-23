from django_cron import CronJobBase, Schedule
from .models import Maquina
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializa o Firebase
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

class MinhaTaskPeriodica(CronJobBase):
    RUN_EVERY_MINS = 1  # Executa a cada 1 minuto

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api_rest.minha_task_periodica'  # Um identificador único para o job

    def do(self):
        # Conecta ao Firestore
        db = firestore.client()
        
        # Pega os dados da coleção 'dados_endpoint' do Firestore
        users_ref = db.collection('dados_endpoint')
        docs = users_ref.stream()
            
        for doc in docs:
            data = doc.to_dict()
            
            miner = data.get('miner_status', {})
            miner_status = miner.get('miner_status')
            tera_hash = data.get('average_hashrate')
            chip_temp = data.get('chip_temp', {})
            chip_temperature_min = chip_temp.get('min')
            chip_temperature_max = chip_temp.get('max')
            cooling_data = data.get('cooling_data', {})
            cooling = cooling_data.get('fan_duty')
            rate = 0
            pcb_temp = data.get('pcb_temp', {})
            pcb_temperature_min = pcb_temp.get('min')
            pcb_temperature_max = pcb_temp.get('max')
            power_consumption = data.get('power_consumption')
            power_efficiency = data.get('power_efficiency')
            power_usage = data.get('power_usage')

            # Cria ou atualiza a instância de Maquina
            maquina, created = Maquina.objects.update_or_create(
                miner_status=miner_status,
                defaults={
                    'tera_hash': tera_hash,
                    'chip_temperature_min': chip_temperature_min,
                    'chip_temperature_max': chip_temperature_max,
                    'cooling': cooling,
                    'rate': rate,
                    'pcb_temperature_min': pcb_temperature_min,
                    'pcb_temperature_max': pcb_temperature_max,
                    'power_consumption': power_consumption,
                    'power_efficiency': power_efficiency,
                    'power_usage': power_usage,
                }
            )
            print(f'Dados {"criados" if created else "atualizados"} em Maquina: {maquina}')