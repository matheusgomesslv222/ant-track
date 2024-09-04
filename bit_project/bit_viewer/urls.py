from django.contrib import admin
from django.urls import path , include

from .views import home, UserCreateView


urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', UserCreateView.as_view(), name='Cadastro'),
]
