from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import PerfilCliente, Servicio, Promocion, Reserva

class PerfilClienteInline(admin.StackedInline):
    model = PerfilCliente
    can_delete = False
    verbose_name_plural = 'Perfil de Cliente'

class UserAdmin(BaseUserAdmin):
    inlines = (PerfilClienteInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Servicio)
admin.site.register(Promocion)
admin.site.register(Reserva)