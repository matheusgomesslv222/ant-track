from django.contrib import admin
from django.urls import path , include
from django.urls import path
import dashboard.views as dashboard_views

urlpatterns = [
    path('', dashboard_views.index, name='home'),
]
