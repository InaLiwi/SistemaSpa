from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('promociones/', views.promociones, name='promociones'),
    path('reserva/<int:servicio_id>/', views.hacer_reserva, name='hacer_reserva'),
    path('mis-reservas/', views.mis_reservas, name='mis_reservas'),
    path('galeria/', views.galeria, name='galeria'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    
    # URLs para trabajadores y administradores
    path('gestion/servicios/', views.admin_servicios, name='admin_servicios'),
    path('gestion/servicios/crear_servicio/', views.crear_servicio, name='crear_servicio'),
    path('gestion/servicios/editar/<int:servicio_id>/', views.editar_servicio, name='editar_servicio'),
    path('gestion/servicios/eliminar/<int:servicio_id>/', views.eliminar_servicio, name='eliminar_servicio'),
    path('gestion/promociones/', views.admin_promociones, name='admin_promociones'),
    path('gestion/promociones/crear/', views.crear_promocion, name='crear_promocion'),
    path('gestion/promociones/editar/<int:promocion_id>/', views.editar_promocion, name='editar_promocion'),
    path('gestion/promociones/eliminar/<int:promocion_id>/', views.eliminar_promocion, name='eliminar_promocion'),
    path('gestion/galeria/', views.admin_galeria, name='admin_galeria'),
    path('gestion/galeria/crear/', views.crear_foto, name='crear_foto'),
    path('gestion/galeria/editar/<int:foto_id>/', views.editar_foto, name='editar_foto'),
    path('gestion/galeria/eliminar/<int:foto_id>/', views.eliminar_foto, name='eliminar_foto'),
    path('gestion/reservas/', views.admin_reservas, name='admin_reservas'),
    path('cancelar-reserva/<int:id>/', views.cancelar_reserva, name='cancelar_reserva'),
]
