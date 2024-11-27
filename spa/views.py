from django.http import HttpResponse
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
def reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/index.html', {'reservas': reservas})

def c_reserva(request):
    formulario = ReservaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('reservas')
    return render(request, 'reservas/crear.html', {'formulario':formulario})

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

def c_promos(request):
    formulario = PromocionForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('promos')
    return render(request, 'promociones/crear.html', {'formulario':formulario})

def u_promos(request, promocion_id):
    promocion = get_object_or_404(Promocion, promocion_id=promocion_id)
    if request.method == 'POST':
        formulario = PromocionForm(request.POST, request.FILES, instance=promocion)
        if formulario.is_valid():
            formulario.save()  
            return redirect('promos')  
    else:
        formulario =PromocionForm(instance=promocion)  
    return render(request, 'promociones/editar.html', {'formulario': formulario})

def d_promos(request, promocion_id):
    promocion = Promocion.objects.get(promocion_id = promocion_id)
    promocion.delete()
    

# ----- OTROS ------
def galeria(request):
    return render(request, 'paginas/galeria.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')

def login(request):
    return render(request, 'paginas/login.html')

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



'''
def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario':formulario})

def editar(request):
    return render(request, 'libros/editar.html')'''