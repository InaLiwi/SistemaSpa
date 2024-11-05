from django import forms
from .models import SPA

class LibroForm(forms.ModelForm):
    class Meta:
        model = SPA
        fields = '__all__'
        
