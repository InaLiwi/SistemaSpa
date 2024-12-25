from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class BloqueHora(models.Model):
    bh_id = models.AutoField(primary_key=True, unique=True)
    bh_dia = models.DateField(verbose_name='Fecha')
    bh_hora_inicio = models.TimeField()
    bh_hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.bh_dia}, de {self.bh_hora_inicio} a {self.bh_hora_fin} hrs."


class Servicio(models.Model):
    servicio_id = models.AutoField(primary_key=True)
    servicio_precio = models.IntegerField(verbose_name='Precio del servicio: ')
    servicio_descripcion = models.CharField(max_length=200, verbose_name='Descripción: ')
    servicio_bh = models.ForeignKey(BloqueHora, on_delete=models.CASCADE, related_name='servicios')
    servicio_imagenes = models.ImageField(upload_to='imagenes/', verbose_name='Imagen Portada', null=True, blank=True)

    def __str__(self):
        return f"Servicio: {self.servicio_id} || Descripción: {self.servicio_descripcion} || Precio: ${self.servicio_precio}"

    def delete(self, using=None, keep_parents=False):
        self.servicio_imagenes.storage.delete(self.servicio_imagenes.name)
        super().delete()


class Promocion(models.Model):
    promocion_id = models.AutoField(primary_key=True)
    promocion_precio = models.IntegerField(verbose_name='Descuento en CLP: ')
    promocion_descripcion = models.CharField(max_length=200, verbose_name='Descripción: ')
    promocion_servicios = models.ManyToManyField(
        Servicio,
        related_name='promociones',
        verbose_name='Servicios aplicables',
        through='PromocionServicio'
    )
    def __str__(self):
        return f"Promoción: {self.promocion_id} || Descripción: {self.promocion_descripcion} || Descuento: ${self.promocion_precio}"


class PromocionServicio(models.Model):
    promo_id = models.ForeignKey(Promocion, on_delete=models.CASCADE, related_name='detalles_promocion_servicio', verbose_name='Promociones aplicables')
    servicios_id = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='detalles_promocion_servicio', verbose_name='Servicios aplicables')

    def __str__(self):
        return f"Promoción: {self.promo_id} - Servicio: {self.servicios_id}"

class PerfilCliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PerfilCliente.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfilcliente.save()


'''
class Usuario(models.Model):
    usuario_nombreUsuario = models.CharField(max_length=128, primary_key=True, unique=True, verbose_name='Ingrese un nombre de usuario único: ')
    usuario_password = models.CharField(max_length=255, verbose_name='Ingrese una contraseña: ')
    usuario_tipo = models.CharField(max_length=15, verbose_name='Tipo de usuario: administrador, trabajador, cliente')

    def __str__(self):
        return f"Usuario: {self.usuario_nombreUsuario} || Tipo de usuario: {self.usuario_tipo}"

class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    cliente_nombreCliente = models.CharField(max_length=50, verbose_name='Nombre y Apellido: ')
    cliente_direccion = models.CharField(max_length=200, verbose_name='Dirección: ')
    cliente_telefono = models.IntegerField(verbose_name='Número de teléfono: ')

    def __str__(self):
        return f"Usuario: {self.usuario.usuario_nombreUsuario} || Nombre: {self.cliente_nombreCliente} || Dirección: {self.cliente_direccion} || Teléfono: {self.cliente_telefono}"
'''

class Reserva(models.Model):
    reserva_id = models.AutoField(primary_key=True)
    reserva_servicios = models.ManyToManyField(
        Servicio,
        related_name='reservas',
        through='ReservaPromocion'
    )
    reserva_cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservas')

    def __str__(self):
        return f"Reserva: {self.reserva_id} || Cliente: {self.reserva_cliente.username}"
    
    def calcular_precio_total(self):
        total = 0
        # Iteramos sobre los objetos en la tabla intermedia 'ReservaPromocion'
        for detalle in ReservaPromocion.objects.filter(reserva_id=self):
            precio = detalle.servicio_id.servicio_precio  # Usamos 'servicio_id' para acceder al precio
            if detalle.promo_id:  # Si hay una promoción asociada
                precio -= detalle.promo_id.promocion_precio  # Aplicar descuento de la promoción
            total += precio
        return total




class ReservaPromocion(models.Model):
    reserva_id = models.ForeignKey(
        Reserva,
        on_delete=models.CASCADE,
        related_name='detalles_reserva_promocion',
        verbose_name='Reserva asociada'
    )
    servicio_id = models.ForeignKey(
        Servicio,
        on_delete=models.CASCADE,
        related_name='detalles_reserva_promocion',
        verbose_name='Servicio asociado'
    )
    promo_id = models.ForeignKey(
        Promocion,
        on_delete=models.CASCADE,
        related_name='reservas_promocion_aplicadas',
        verbose_name='Promoción asociada',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Reserva: {self.reserva_id}- Promoción: {self.promo_id}"

