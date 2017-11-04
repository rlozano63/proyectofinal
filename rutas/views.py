from django.shortcuts import render

from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def mapa(request):
    return render(request, 'rutas.html', {})
