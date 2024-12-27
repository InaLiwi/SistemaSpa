from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Servicio, Promocion, Reserva, GaleriaFoto
from .forms import ServicioForm, PromocionForm, ReservaForm, GaleriaFotoForm, RegistroForm

def inicio(request):
    servicios = Servicio.objects.all()[:3]  # Mostrar solo 3 servicios en la página de inicio
    return render(request, 'inicio.html', {'servicios': servicios})

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})

def promociones(request):
    promociones = Promocion.objects.all()
    return render(request, 'promociones.html', {'promociones': promociones})

@login_required
def hacer_reserva(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.servicio = servicio
            reserva.save()
            messages.success(request, 'Reserva realizada con éxito.')
            return redirect('mis_reservas')
    else:
        form = ReservaForm()
    return render(request, 'hacer_reserva.html', {'form': form, 'servicio': servicio})

@login_required
def mis_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'mis_reservas.html', {'reservas': reservas})

def galeria(request):
    fotos = GaleriaFoto.objects.all()
    return render(request, 'galeria.html', {'fotos': fotos})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.tipo_usuario = form.cleaned_data['tipo_usuario']
            user.save()
            login(request, user)
            messages.success(request, f'Registro exitoso. Bienvenido, {user.username}!')
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

@user_passes_test(lambda u: u.is_trabajador_or_admin())
def admin_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'gestion/servicios.html', {'servicios': servicios})

@user_passes_test(lambda u: u.is_trabajador_or_admin())
def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Servicio creado con éxito.')
            return redirect('admin_servicios')
    else:
        form = ServicioForm()
    return render(request, 'gestion/crear_servicio.html', {'form': form})

@user_passes_test(lambda u: u.is_trabajador_or_admin())
def editar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Servicio actualizado con éxito.')
            return redirect('admin_servicios')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'gestion/editar_servicio.html', {'form': form, 'servicio': servicio})

@user_passes_test(lambda u: u.is_trabajador_or_admin())
def eliminar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    if request.method == 'POST':
        servicio.delete()
        messages.success(request, 'Servicio eliminado con éxito.')
        return redirect('admin_servicios')
    return render(request, 'gestion/eliminar_servicio.html', {'servicio': servicio})

@user_passes_test(lambda u: u.is_trabajador_or_admin())
def admin_promociones(request):
    promociones = Promocion.objects.all()
    return render(request, 'gestion/promociones.html', {'promociones': promociones})

@user_passes_test(lambda u: u.is_trabajador_or_admin())
def crear_promocion(request):
    if request.method == 'POST':
        form = PromocionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Promoción creada con éxito.')
            return redirect('admin_promociones')
    else:
        form = PromocionForm()
    return render(request, 'gestion/crear_promocion.html', {'form': form})

@user_passes_test(lambda u: u.is_trabajador_or_admin())
def editar_promocion(request, promocion_id):
    promocion = get_object_or_404(Promocion, id=promocion_id)
    if request.method == 'POST':
        form = PromocionForm(request.POST, instance=promocion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Promoción actualizada con éxito.')
            return redirect('admin_promociones')
    else:
        form = PromocionForm(instance=promocion)
    return render(request, 'gestion/editar_promocion.html', {'form': form, 'promocion': promocion})

@user_passes_test(lambda u: u.is_trabajador_or_admin())
def eliminar_promocion(request, promocion_id):
    promocion = get_object_or_404(Promocion, id=promocion_id)
    if request.method == 'POST':
        promocion.delete()
        messages.success(request, 'Promoción eliminada con éxito.')
        return redirect('admin_promociones')
    return render(request, 'gestion/eliminar_promocion.html', {'promocion': promocion})

@user_passes_test(lambda u: u.is_trabajador_or_admin())
def admin_galeria(request):
    fotos = GaleriaFoto.objects.all()
    form = GaleriaFotoForm()
    return render(request, 'gestion/galeria.html', {'fotos': fotos, 'form': form})

@user_passes_test(lambda u: u.is_trabajador_or_admin())
def crear_foto(request):
    if request.method == 'POST':
        form = GaleriaFotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto añadida con éxito.')
            return redirect('admin_galeria')
    return redirect('admin_galeria')

@user_passes_test(lambda u: u.is_trabajador_or_admin())
def editar_foto(request, foto_id):
    foto = get_object_or_404(GaleriaFoto, id=foto_id)
    if request.method == 'POST':
        form = GaleriaFotoForm(request.POST, request.FILES, instance=foto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto actualizada con éxito.')
            return redirect('admin_galeria')
    else:
        form = GaleriaFotoForm(instance=foto)
    return render(request, 'gestion/editar_foto.html', {'form': form, 'foto': foto})

@user_passes_test(lambda u: u.is_trabajador_or_admin())
def eliminar_foto(request, foto_id):
    foto = get_object_or_404(GaleriaFoto, id=foto_id)
    if request.method == 'POST':
        foto.delete()
        messages.success(request, 'Foto eliminada con éxito.')
        return redirect('admin_galeria')
    return render(request, 'gestion/eliminar_foto.html', {'foto': foto})

@user_passes_test(lambda u: u.is_trabajador_or_admin())
def admin_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'gestion/reservas.html', {'reservas': reservas})

def cancelar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if reserva.usuario == request.user:  # Verifica que el usuario sea el propietario de la reserva
        reserva.delete()
        messages.success(request, "Reserva cancelada con éxito.")
    else:
        messages.error(request, "No tienes permiso para cancelar esta reserva.")
    return redirect('mis_reservas')
