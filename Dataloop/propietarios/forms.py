from django import forms
from django.forms import ModelForm
from .models import Vivienda

#create vivienda form

class ViviendaForm(ModelForm):
    class Meta:
        model = Vivienda
        fields = ('numero','nombres','apellido_pat','apellido_mat')
        labels = {
            'numero' : 'Numero de Casa',
            'nombres'  : 'Nombre(s)',
            'apellido_pat'  : 'Apellido Paterno',
            'apellido_mat'  : 'Apellido materno'
        }