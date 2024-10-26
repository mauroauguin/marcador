from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.view_marcador, name='view_marcador'),
    path('admin/', views.admin_marcador, name='admin_marcador'),
]