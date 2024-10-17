from django.contrib import admin
from django.urls import path , include


urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('api/', include('api_rest.urls'), name='api_rest_urls'),
    path('', include('dashboard.urls'), name='dashboard_urls'),
]
