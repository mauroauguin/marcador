from django.shortcuts import render, redirect
from django.http import Http404
from .models import Marcador

def create_marcador(request):
    new_marcador = Marcador.objects.create()
    return redirect('view_marcador', marcador_id=new_marcador.id)

def view_marcador(request, marcador_id):
    try:
        marcador = Marcador.objects.get(id=marcador_id)
    except Marcador.DoesNotExist:
        raise Http404("Marcador no encontrado")
    return render(request, 'home.html', {'marcador': marcador})

def admin_marcador(request, marcador_id):
    try:
        marcador = Marcador.objects.get(id=marcador_id)
    except Marcador.DoesNotExist:
        raise Http404("Marcador no encontrado")
    return render(request, 'admin.html', {'marcador': marcador, 'marcador_id': marcador_id})

def custom_404(request, exception):
    return render(request, '404.html', status=404)