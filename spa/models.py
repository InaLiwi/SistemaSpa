from django.db import models

# Create your models here.
"""
class SPA(models.Model):
    libro_id = models.AutoField(primary_key=True)
    libro_nombre = models.CharField(max_length=100, verbose_name='Nombre Libro')
    libro_imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen Portada', null=True, blank=True)
    libro_descripcion = models.TextField(verbose_name='Descripción',null=True, blank=True)
    libro_fecha_publicacion = models.DateField(verbose_name='Fecha Publicación',null=True, blank=True)


#python manage.py makemigrations
#nos permite crear un archivo para migrar, debemos ejecutar este comando cada vez que modifiquemos el modelo de la bd

#python manage.py migrate
#aplica las migraciones creadas, sincroniza su estructura, modificaciones etc...
    def __str__(self):
        fila = "Libro: " + self.libro_nombre + " || "  + "Descripción: " + self.libro_descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.libro_imagen.storage.delete(self.libro_imagen.name)
        super().delete()
   """     

class Dia(models.Model):    
    dia_id = models.AutoField(primary_key=True)
    dia_fecha = models.DateField(unique=True)

class BloqueHora(models.Model):
    bh_id = models.AutoField(primary_key=True, unique=True)
    bh_dia = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name='bloques')
    bh_hora_inicio = models.TimeField()  # Hora de inicio del bloque
    bh_hora_fin = models.TimeField()     # Hora de fin del bloque

    def __str__(self):
        fila =  f"{self.bh_dia}, de {self.bh_hora_inicio} a {self.bh_hora_fin} hrs."
        return fila



class Servicio(models.Model):
    servicio_id = models.AutoField(primary_key=True)
    servicio_precio = models.IntegerField( verbose_name='Precio del servicio: ')
    servicio_descripcion = models.CharField(max_length=200, verbose_name='Descripción: ')
    servicio_bh = models.ForeignKey(BloqueHora, on_delete=models.CASCADE, related_name='servicios')
    servicio_imagenes = models.ImageField(upload_to='imagenes/', verbose_name='Imagen Portada', null=True, blank=True)

    def __str__(self):
        fila = "Servicio: " + str(self.servicio_id) + " || "  + "Descripción: " + self.servicio_descripcion + " || "  + "Precio: $" + str(self.servicio_precio) + " || "  + "Fecha y Hora: " + str(self.servicio_bh)
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.servicio_imagenes.storage.delete(self.servicio_imagenes.name)
        super().delete()


class Promocion(models.Model):
    promocion_id = models.AutoField(primary_key=True)
    promocion_precio = models.IntegerField(verbose_name='Precio del servicio: ')
    promocion_descripcion = models.CharField(max_length=200, verbose_name='Descripción: ')
    promocion_servicios = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='promos')
    #promocion_servicios = models.arreglo(verbose_name= 'Fecha y Hora del servicio: ')
    
    def __str__(self):
        fila = "Promoción: " + str(self.promocion_id) + " || "  + "Descripción: " + self.promocion_descripcion + " || "  + "Precio: $" + str(self.promocion_precio)
        return fila


class Usuario(models.Model):
    usuario_nombreUsuario = models.CharField(max_length=50, primary_key=True, unique=True, verbose_name='Ingrese un nombre de usuario único: ')
    usuario_password = models.CharField(max_length=20, verbose_name='Ingrese una contraseña: ')
    usuario_tipo = models.CharField(max_length=15, verbose_name='Tipo de usuario: administrador, trabajador, cliente')

    def __str__(self):
        fila = "Usuario: " + self.usuario_nombreUsuario + " || "  + "Tipo de usuario: " + self.usuario_tipo
        return fila

    def modificarReserva():
        pass



class Cliente(Usuario):
    cliente_nombreCliente = models.CharField(max_length=50, verbose_name='Nombre y Apellido: ')
    cliente_direccion = models.CharField(max_length=200, verbose_name='Dirección: ')
    cliente_telefono = models.IntegerField(verbose_name='Número de teléfono: ')

    def __str__(self):
        fila = "Usuario: " + self.usuario_nombreUsuario + " || "  + "Nombre: " + self.cliente_nombreCliente + " || "  + "Dirección: " + self.cliente_direccion + " || "  + "Nombre: " + str(self.cliente_telefono)
        return fila




class Reserva(models.Model):
    reserva_id = models.AutoField(primary_key=True)
    reserva_servicios = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='reservaServicios')
    reserva_promos = models.ForeignKey(Promocion, on_delete=models.CASCADE, related_name='reservaPromos')
    reserva_precioTotal = models.IntegerField()
    reserva_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente')

    def __str__(self):
        fila = "Reserva: " + str(self.reserva_id) + " || "  + "Cliente: " + self.reserva_cliente  + " || "  + "Precio total: " + str(self.reserva_precioTotal)
        return fila