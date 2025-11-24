from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre', 'tipo_plato', 'ingredientes', 'tiempo_preparacion', 'instrucciones', 'imagen']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_plato': forms.Select(attrs={'class': 'form-select'}),
            'ingredientes': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'id': 'id_ingredientes'
            }),
            'tiempo_preparacion': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'instrucciones': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }
