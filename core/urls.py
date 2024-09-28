from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_marcador, name='create_marcador'),
    path('<uuid:marcador_id>/', views.view_marcador, name='view_marcador'),
    path('<uuid:marcador_id>/admin/', views.admin_marcador, name='admin_marcador'),
]