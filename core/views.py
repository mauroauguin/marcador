from django.shortcuts import render
from .models import Marcador
from django.http import JsonResponse

def admin(request):
    marcador, created = Marcador.objects.get_or_create(pk=1)
    return render(request, 'admin.html', {'marcador': marcador})

def home(request):
    marcador, created = Marcador.objects.get_or_create(pk=1)
    return render(request, 'home.html', {'marcador': marcador})

def actualizar_marcador(request):
    marcador, created = Marcador.objects.get_or_create(pk=1)
    return JsonResponse({
        'jugador1': marcador.jugador1,
        'jugador2': marcador.jugador2,
        'set1_jugador1': marcador.set1_jugador1,
        'set2_jugador1': marcador.set2_jugador1,
        'set3_jugador1': marcador.set3_jugador1,
        'set1_jugador2': marcador.set1_jugador2,
        'set2_jugador2': marcador.set2_jugador2,
        'set3_jugador2': marcador.set3_jugador2,
    })