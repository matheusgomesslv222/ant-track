from django.contrib import admin
from django.urls import path , include

from . import views


urlpatterns = [
    path('getUsers/', views.getUsers, name='getUsers'),
    path('createUser/', views.createUser, name='createUser'),
    path('authUser/', views.userAuth, name='authUser'),
]
