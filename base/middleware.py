from base.models import distribuidor
from django.shortcuts import render


class verificar_usuario_distribuidor(object):
	def process_request(self, request):
		if not  distribuidor.objects.filter(usuario=self.request.user).exists() :
			return render(request, 'error.html')
