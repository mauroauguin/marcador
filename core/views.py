from django.shortcuts import render, redirect
from django.http import Http404
from .models import Marcador

def create_marcador():
    # Crea un marcador solo si no existe
    marcador, created = Marcador.objects.get_or_create(id=1, defaults={
        'campeonato': 'Campeonato de Ejemplo',
        'jugador1': 'Jugador 1',
        'jugador2': 'Jugador 2',
        'set1_jugador1': 0,
        'set2_jugador1': 0,
        'set3_jugador1': 0,
        'set1_jugador2': 0,
        'set2_jugador2': 0,
        'set3_jugador2': 0,
    })
    return marcador

def view_marcador(request):
    marcador = create_marcador()  # Asegúrate de que solo haya un marcador
    return render(request, 'home.html', {'marcador': marcador})

def admin_marcador(request):
    marcador = create_marcador()  # Asegúrate de que solo haya un marcador
    return render(request, 'admin.html', {'marcador': marcador})

def custom_404(request, exception):
    return render(request, '404.html', status=404)
