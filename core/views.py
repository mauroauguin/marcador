from django.shortcuts import render, redirect
from django.http import Http404
from .models import Marcador
import uuid

def create_marcador(request):
    new_marcador = Marcador.objects.create()
    return redirect('view_marcador', marcador_id=new_marcador.id)

def view_marcador(request):
    # Intenta obtener el marcador por ID
    try:
        marcador = Marcador.objects.get(id=1)  # Cambiado a un entero
    except Marcador.DoesNotExist:
        # Si no existe, crea un nuevo marcador sin especificar el ID
        marcador = Marcador(campeonato="Campeonato Default", jugador1="Jugador 1", jugador2="Jugador 2")
        marcador.save()  # Guarda el nuevo marcador en la base de datos
    return render(request, 'home.html', {'marcador': marcador})

def admin_marcador(request):
    try:
        marcador = Marcador.objects.get(id=1)  # Cambiado a un entero
    except Marcador.DoesNotExist:
        raise Http404("Marcador no encontrado")
    return render(request, 'admin.html', {'marcador': marcador})  # Renderiza admin.html

def custom_404(request, exception):
    return render(request, '404.html', status=404)
