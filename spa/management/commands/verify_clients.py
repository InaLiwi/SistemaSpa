from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from spa.models import Usuario, Cliente

class Command(BaseCommand):
    help = 'Verifies and creates missing Cliente objects'

    def handle(self, *args, **options):
        for user in User.objects.all():
            usuario, created = Usuario.objects.get_or_create(
                usuario_nombreUsuario=user.username,
                defaults={
                    'usuario_password': user.password,
                    'usuario_tipo': 'cliente'
                }
            )
            cliente, created = Cliente.objects.get_or_create(
                usuario=usuario,
                defaults={
                    'cliente_nombreCliente': user.get_full_name() or user.username,
                    'cliente_direccion': '',
                    'cliente_telefono': 0
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Cliente for {user.username}'))
            else:
                self.stdout.write(f'Cliente already exists for {user.username}')

        self.stdout.write(self.style.SUCCESS('Verification complete'))