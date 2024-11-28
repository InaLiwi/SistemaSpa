from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

'''
PÁGINAS QUE SE VERÁN:
- Inicio
- Reservaciones
    - c_reserva --> crear reserva
    - u_reserva --> editar reserva (update)
    - d_reserva --> delete/eliminar reserva
- Servicios que tenemos (y sus promociones)
- Promociones
- Perfil
- Galería
- Contacto
'''

# path(palabra_del_SLACH, FUNCION_DE_views, NOMBRE_PARA_LLAMAR_DESDE_EL_html) 
urlpatterns = [
    path('', views.inicio, name='inicio'),

# Reservas
    path('reservas', views.reservas, name='reservas'),
    path('c_reserva', views.c_reserva, name='c_reserva'),
    path('u_reserva', views.u_reserva, name='u_reserva'),
    path('d_reserva', views.d_reserva, name='d_reserva'),    
    
# Servicios    
    path('servicios', views.servicios, name='servicios'),
    path('c_servicio', views.c_servicio, name='c_servicio'),
    path('u_servicio', views.u_servicio, name='u_servicio'),
    path('d_servicio', views.d_servicio, name='d_servicio'),   
    
# Promociones
    path('promos', views.promos, name='promos'),
    path('c_promo', views.c_promo, name='c_promo'),
    path('u_promo', views.u_promo, name='u_promo'),
    path('d_promo', views.d_promo, name='d_promo'),

# Galeria
    path('galeria', views.galeria, name='galeria'),

# Contacto
    path('contacto', views.contacto, name='contacto'),

# Login
    path('login', views.login, name='login'),

# Registro
    path('registro/', views.registro, name='registro'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
