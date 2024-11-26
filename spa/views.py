from django.http import HttpResponse
from django.shortcuts import redirect, render
#from .models import SPA
#from .forms import SPAForm

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

# Servicios #

def servicios(request):
    return render(request, 'paginas/servicios.html')

def c_servicios(request):
    return render(request, 'paginas/c_servicios.html')

def u_servicios(request):
    return render(request, 'paginas/u_servicios.html')

def d_servicios(request):
    return render(request, 'paginas/d_servicios.html')

# Resrvas #

def reservas(request):
    return render(request, 'reservas/index.html')

def c_reserva(request):
    return render(request, 'paginas/c_reserva.html')

def u_reserva(request):
    return render(request, 'paginas/u_reserva.html')

def d_reserva(request):
    return render(request, 'paginas/d_reserva.html')

# Promos #

def promos(request):
    return render(request, 'paginas/promos.html')

def c_promos(request):
    return render(request, 'paginas/c_promos.html')

def u_promos(request):
    return render(request, 'paginas/u_promos.html')

def d_promos(request):
    return render(request, 'paginas/d_promos.html')

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