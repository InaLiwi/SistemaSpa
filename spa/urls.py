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
    path('c_servicios', views.c_servicios, name='c_servicios'),
    path('u_servicios', views.u_servicios, name='u_servicios'),
    path('d_servicios', views.d_servicios, name='d_servicios'),   
    
# Promociones
    path('promos', views.promos, name='promos'),
    path('c_promos', views.c_promos, name='c_promos'),
    path('u_promos', views.u_promos, name='u_promos'),
    path('d_promos', views.d_promos, name='d_promos'),

# Galeria
    path('galeria', views.galeria, name='galeria'),

# Contacto
    path('contacto', views.contacto, name='contacto'),

# Login
    path('login', views.login, name='login'),

# Registro
    path('registro/', views.registro, name='registro'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
