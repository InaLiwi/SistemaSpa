from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Servicio, Promocion, Reserva, GaleriaFoto

class RegistroForm(UserCreationForm):
    tipo_usuario = forms.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES, required=True)
    codigo_seguridad = forms.CharField(required=False, help_text="Requerido para crear administradores o trabajadores")

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'telefono', 'direccion', 'tipo_usuario']

    def clean(self):
        cleaned_data = super().clean()
        tipo_usuario = cleaned_data.get('tipo_usuario')
        codigo_seguridad = cleaned_data.get('codigo_seguridad')

        if tipo_usuario in [Usuario.ADMIN, Usuario.TRABAJADOR]:
            if not codigo_seguridad or codigo_seguridad != "codigo_secreto":  # Cambia esto por un código seguro real
                raise forms.ValidationError("Código de seguridad inválido para crear un administrador o trabajador")

        return cleaned_data

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio', 'duracion', 'imagen']

class PromocionForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = ['nombre', 'descripcion', 'descuento', 'servicios', 'fecha_inicio', 'fecha_fin']

        widgets = {
            'servicios': forms.CheckboxSelectMultiple(),
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha', 'promocion']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class GaleriaFotoForm(forms.ModelForm):
    class Meta:
        model = GaleriaFoto
        fields = ['titulo', 'imagen', 'descripcion']