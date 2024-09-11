from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import UsuarioInfo
from .serializers import UsuarioInfoSerializer

import json

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
