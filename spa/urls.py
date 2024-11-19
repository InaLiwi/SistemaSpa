from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

'''
PÁGINAS QUE SE VERÁN:
- Inicio
- Reservaciones
- Servicios que tenemos (y sus promociones)
- Promociones
- Perfil
- Galería
- Contacto
'''

# path(palabra_del_SLACH, FUNCION_DE_views, NOMBRE_PARA_LLAMAR_DESDE_EL_html) 
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios', views.servicios, name='servicios'),
    path('libros', views.libros, name='libros'),
    path('crear', views.crear, name='crear'),
    path('editar', views.editar, name='editar'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
