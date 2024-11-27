from django import forms
'''
from .models import SPA

class LibroForm(forms.ModelForm):
    class Meta:
        model = SPA
        fields = '__all__'
        
'''

from .models import *

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class PromocionForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'