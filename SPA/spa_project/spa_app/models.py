from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class Usuario(AbstractUser):
    ADMIN = 'admin'
    TRABAJADOR = 'trabajador'
    USUARIO = 'usuario'
    TIPO_USUARIO_CHOICES = [
        (ADMIN, 'Administrador'),
        (TRABAJADOR, 'Trabajador'),
        (USUARIO, 'Usuario'),
    ]
    tipo_usuario = models.CharField(
        max_length=20,
        choices=TIPO_USUARIO_CHOICES,
        default=USUARIO,
    )
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    def is_trabajador_or_admin(self):
        return self.tipo_usuario in [self.ADMIN, self.TRABAJADOR]

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    duracion = models.DurationField()
    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Promocion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    servicios = models.ManyToManyField(Servicio, related_name='promociones')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reservas')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    promocion = models.ForeignKey(Promocion, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ], default='pendiente')

    def __str__(self):
        return f"Reserva de {self.usuario.username} para {self.servicio.nombre}"

class GaleriaFoto(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='galeria/')
    descripcion = models.TextField(blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

