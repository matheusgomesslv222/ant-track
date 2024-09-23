from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import UsuarioInfo, Maquina
from .serializers import UsuarioInfoSerializer

import json

import firebase_admin
from firebase_admin import credentials, firestore
from .serializers import MaquinaSerializer

# Inicializa o Firebase
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)


def get_data(request):
    # Conecta ao Firestore
    db = firestore.client()
    
    # Pega todos os documentos da coleção 'dados_endpoint' do Firestore
    try:
        users_ref = db.collection('dados_endpoint')
        docs = list(users_ref.stream())
        if not docs:
            return JsonResponse({'status': 'Nenhum dado encontrado no Firestore'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'Erro ao acessar o Firestore', 'message': str(e)}, status=500)
    
    # Log dos documentos recuperados
    print(f'Recuperados {len(docs)} documentos do Firestore')
    
    # Ordena os documentos manualmente pelo campo 'hr_realtime' dentro de 'miner'
    sorted_docs = sorted(docs, key=lambda doc: doc.to_dict().get('miner', {}).get('hr_realtime', 0), reverse=True)
    
    maquina = None
    for doc in sorted_docs:
        data = doc.to_dict().get('miner', {})
        
        miner = data.get('miner_status', {})
        miner_status = miner.get('miner_state')
        tera_hash = 0
        chip_temp = data.get('chip_temp', {})
        chip_temperature_min = chip_temp.get('min')
        chip_temperature_max = chip_temp.get('max')
        cooling_data = data.get('cooling', {})
        cooling = cooling_data.get('fan_duty')
        rate = 0
        pcb_temp = data.get('pcb_temp', {})
        pcb_temperature_min = pcb_temp.get('min')
        pcb_temperature_max = pcb_temp.get('max')
        power_consumption = data.get('power_consumption')
        power_efficiency = data.get('power_efficiency')
        power_usage = data.get('power_usage')

        # Cria uma nova instância de Maquina
        maquina = Maquina.objects.create(
            miner_status=miner_status,
            tera_hash=tera_hash,
            chip_temperature_min=chip_temperature_min,
            chip_temperature_max=chip_temperature_max,
            cooling=cooling,
            rate=rate,
            pcb_temperature_min=pcb_temperature_min,
            pcb_temperature_max=pcb_temperature_max,
            power_consumption=power_consumption,
            power_efficiency=power_efficiency,
            power_usage=power_usage,
        )
        print(f'Nova instância de Maquina criada: {maquina}')
    
    # Retorna a instância dos dados salvos
    if maquina :
        serializer = MaquinaSerializer(maquina)
        return JsonResponse({
            'status': 'Dados atualizados com sucesso',
            'maquina': serializer.data
        }, status=200)
    else:
        return JsonResponse({
            'status': 'Nenhum dado encontrado no Firestore'
        }, status=404)


@api_view(['GET'])
def getUsers(request):
    # Get all the usuarios from the database
    usuarios = UsuarioInfo.objects.all()

    # Serialize the usuarios
    serializer = UsuarioInfoSerializer(usuarios, many=True)

    # Return the serialized data
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def createUser(request):
    
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the data from the request
        nome = request.data.get('nome')
        senha = request.data.get('senha')
        email = request.data.get('email')
        data_nascimento = request.data.get('data_nascimento')
        

        # Check if any data is missing
        if not nome or not senha or not email or not data_nascimento:
            return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the usuario already exists
        if UsuarioInfo.objects.filter(email=email).exists():
            return Response({'message': 'Usuario already exists'}, status=status.HTTP_409_CONFLICT)

        # Create a new instance of UsuarioInfo
        usuario = UsuarioInfo(nome=nome, senha=senha, email=email, data_nascimento=data_nascimento)

        # Save the new usuario to the database
        usuario.save()

        # Return a success response
        return Response({'message': 'Usuario created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def userAuth(request):
    if request.method == 'POST':
        nome = request.data.get('nome')
        senha = request.data.get('senha')

        try:
            usuario = UsuarioInfo.objects.get(nome=nome, senha=senha)
        except UsuarioInfo.DoesNotExist:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'message': 'User authenticated successfully'}, status=status.HTTP_200_OK)
    
@api_view(['PUT'])
def userUpdate(request):
    if request.method == 'PUT':
        nome = request.data.get('nome')
        senha = request.data.get('senha')
        email = request.data.get('email')
        data_nascimento = request.data.get('data_nascimento')

        try:
            usuario = UsuarioInfo.objects.get(nome=nome)
        except UsuarioInfo.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        usuario.senha = senha
        usuario.email = email
        usuario.data_nascimento = data_nascimento

        usuario.save()

        return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)
    
@api_view(['DELETE'])
def deleteUser(request):
    if request.method == 'DELETE':
        id = request.data.get('id')

        try:
            usuario = UsuarioInfo.objects.get(id=id)
        except UsuarioInfo.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        usuario.delete()

        return Response({'message': 'User deleted successfully'}, status=status.HTTP_200_OK)
