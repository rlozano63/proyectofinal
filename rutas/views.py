from django.shortcuts import render

from django.shortcuts import render

def mapa(request):
    return render(request, 'rutas.html', {})
