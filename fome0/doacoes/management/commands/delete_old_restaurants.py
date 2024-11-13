from django.core.management.base import BaseCommand
from doacoes.models import Restaurante
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Exclui restaurantes que possuem mais de 7 dias de criação'

    def handle(self, *args, **kwargs):
        limite_data = timezone.now() - timedelta(days=7)
        antigos = Restaurante.objects.filter(criado_em__lt=limite_data)
        quantidade = antigos.count()
        antigos.delete()
        self.stdout.write(self.style.SUCCESS(f'{quantidade} registros foram excluídos'))
