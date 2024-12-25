from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import *
from .forms import *


# Create your views here.
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

def inicio(request):
    return render(request, 'paginas/inicio.html')

# ----- RESERVAS ------

from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ReservaForm  # Suponiendo que tienes un formulario predefinido

def reservas(request):
    reservas = Reserva.objects.all()
    # Calcular el precio total de cada reserva antes de enviarla al template
    for reserva in reservas:
        reserva.precio_total = reserva.calcular_precio_total()  # Método en el modelo Reserva
    return render(request, 'reservas/index.html', {'reservas': reservas})

@login_required
def c_reserva(request):
    if request.method == 'POST':
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            reserva = formulario.save(commit=False)
            # Obtener el usuario seleccionado del formulario
            user = formulario.cleaned_data['cliente']            
            # Obtener o crear el objeto Cliente asociado con este User
            cliente, created = Cliente.objects.get_or_create(
                usuario=user,
                defaults={
                    'cliente_nombreCliente': user.get_full_name() or user.username,
                    'cliente_direccion': '',  # Puedes agregar un campo para esto en el formulario si lo necesitas
                    'cliente_telefono': ''  # Puedes agregar un campo para esto en el formulario si lo necesitas
                }
            )
            reserva.reserva_cliente = cliente
            reserva.save()
            # Guardar los servicios seleccionados
            servicios = formulario.cleaned_data['servicios']
            for servicio in servicios:
                # Buscar si hay una promoción aplicable para este servicio
                promocion = PromocionServicio.objects.filter(
                    servicios_id=servicio,
                    promo_id__promocion_servicios=servicio
                ).first()
                ReservaPromocion.objects.create(
                    reserva_id=reserva,
                    servicio_id=servicio,
                    promo_id=promocion.promo_id if promocion else None
                )
            return redirect('reservas')
    else:
        formulario = ReservaForm()
    return render(request, 'reservas/crear.html', {'formulario': formulario})

def u_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, reserva_id=reserva_id)
    if request.method == 'POST':
        formulario = ReservaForm(request.POST, request.FILES, instance=reserva)
        if formulario.is_valid():
            formulario.save()  
            return redirect('reservas')  
    else:
        formulario = ReservaForm(instance=reserva)  
    return render(request, 'reservas/editar.html', {'formulario': formulario})

def d_reserva(request, reserva_id):
    reserva = Reserva.objects.get(reserva_id = reserva_id)
    reserva.delete()
    return redirect('reservas')


# ----- PROMOCIONES ------
def promos(request):
    promos = Promocion.objects.all()
    return render(request, 'promociones/index.html', {'promos': promos})

def c_promo(request):
    formulario = PromocionForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('promos')
    return render(request, 'promociones/crear.html', {'formulario':formulario})

def u_promo(request, promocion_id):
    promocion = get_object_or_404(Promocion, promocion_id=promocion_id)
    if request.method == 'POST':
        formulario = PromocionForm(request.POST, request.FILES, instance=promocion)
        if formulario.is_valid():
            formulario.save()  
            return redirect('promos')  
    else:
        formulario =PromocionForm(instance=promocion)  
    return render(request, 'promociones/editar.html', {'formulario': formulario})

def d_promo(request, promocion_id):
    promocion = Promocion.objects.get(promocion_id = promocion_id)
    promocion.delete()
    

# ----- SERVICIOS -----
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/index.html', {'servicios': servicios})

def c_servicio(request):
    formulario = ServicioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('servicios')
    return render(request, 'servicios/crear.html', {'formulario':formulario})

def u_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, servicio_id=servicio_id)
    if request.method == 'POST':
        formulario = ServicioForm(request.POST, request.FILES, instance=servicio)
        if formulario.is_valid():
            formulario.save()  
            return redirect('servicios')  
    else:
        formulario = ServicioForm(instance=servicio)  
    return render(request, 'servicios/editar.html', {'formulario': formulario})

def d_servicio(request, servicio_id):
    servicio = Servicio.objects.get(servicio_id = servicio_id)
    servicio.delete()
    return redirect('servicios')


# ----- OTROS ------
def galeria(request):
    return render(request, 'paginas/galeria.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')

def login(request):
    return render(request, 'spa/login.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('inicio') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})























from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservaForm
from .models import Reserva, Cliente, PromocionServicio, ReservaPromocion



