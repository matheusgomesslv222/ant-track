from django.contrib import admin
from django.urls import path , include

from . import views




urlpatterns = [
    path('getUsers/', views.getUsers, name='getUsers'),
    path('createUser/', views.createUser, name='createUser'),
    path('authUser/', views.userAuth, name='authUser'),
    path('userUpdate/', views.userUpdate, name='userUpdate'),
    path('deleteUser/', views.deleteUser, name='deleteUser'),
    
    # URL para atualizar os dados
    path('getData/', views.get_data, name='getData'),
    path('getMediaChip/', views.getMediaChip, name='getMediaChip'),
    path('getMediaPCB/', views.getMediaPCB, name='getMediaPCB'),
    path('getMediaPower/', views.getMediaPower, name='getMediaPower'),
]
