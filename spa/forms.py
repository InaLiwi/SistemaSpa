from django import forms
from django.contrib.auth.models import Group, User
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
    servicios = forms.ModelMultipleChoiceField(
        queryset=Servicio.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    cliente = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='clientes'),
        empty_label="Seleccione un cliente",
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            clientes_group = Group.objects.get(name='clientes')
            self.fields['cliente'].queryset = clientes_group.user_set.all()
        except Group.DoesNotExist:
            self.fields['cliente'].queryset = User.objects.none()

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
        return reserva'''



class ReservaForm(forms.ModelForm):
    servicios = forms.ModelMultipleChoiceField(
        queryset=Servicio.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    cliente = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='clientes'),
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
        try:
            clientes_group = Group.objects.get(name='clientes')
            self.fields['cliente'].queryset = clientes_group.user_set.all()
        except Group.DoesNotExist:
            self.fields['cliente'].queryset = User.objects.none()