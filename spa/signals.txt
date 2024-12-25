from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Usuario, Cliente

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        usuario = Usuario.objects.create(
            usuario_nombreUsuario=instance.username,
            usuario_password=instance.password,
            usuario_tipo='cliente'
        )
        Cliente.objects.create(
            usuario=usuario,
            cliente_nombreCliente=instance.get_full_name(),
            cliente_direccion='',
            cliente_telefono=0
        )
    else:
        Usuario.objects.filter(usuario_nombreUsuario=instance.username).update(usuario_password=instance.password)
        Cliente.objects.filter(usuario__usuario_nombreUsuario=instance.username).update(cliente_nombreCliente=instance.get_full_name())