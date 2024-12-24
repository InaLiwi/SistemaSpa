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

    

'''class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
'''

class ReservaForm(forms.ModelForm):
    servicios = forms.ModelMultipleChoiceField(
        queryset=Servicio.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        empty_label="Seleccione un cliente",
        required=True
    )

    class Meta:
        model = Reserva
        fields = ['cliente', 'servicios']

    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].label = "Cliente"
        self.fields['servicios'].label = "Servicios"

    def save(self, commit=True):
        reserva = super(ReservaForm, self).save(commit=False)
        if commit:
            reserva.save()
            self.save_m2m()  # Guarda las relaciones ManyToMany
        return reserva