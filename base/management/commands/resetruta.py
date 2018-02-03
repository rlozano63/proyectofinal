from django.core.management.base import BaseCommand, CommandError
from base.models import cliente

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        cliente.objects.update(ruta_activa=0)
