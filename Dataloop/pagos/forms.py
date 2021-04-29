from django import forms
from django.forms import ModelForm
from .models import recibo

#create recibo form
MESES =(
    ("Enero","1"),
    ("Febrero","2"),
    ("Marzo","3"),
    ("Abril","4"),
    ("Mayo","5"),
    ("Junio","6"),
    ("Julio","7"),
    ("Agosto","8"),
    ("Septiembre","9"),
    ("Octubre","10"),
    ("Noviembre","11"),
    ("Diciembre","12"),        
    )

class reciboForm(ModelForm):
    class Meta:
        model = recibo
        fields = ('casa','mes','monto')
        model.casa = forms.IntegerField(required=True, min_value=1)
        model.mes  = forms.ChoiceField(choices = MESES)
        labels = {
            'casa' : 'Numero de Casa',
            'mes'  : 'Mes a pagar',
            'monto'  : 'Monto a pagar',
        }

def clean(self):
    super(reciboForm, self).clean()

    # getting username and password from cleaned_data
    casa = self.cleaned_data.get('casa')
    mes = self.cleaned_data.get('mes')

    # validating the username and password
    if type(casa) == int:
        self._errors['casa'] = self.error_class(['Solo se permite valores numericos'])

    if type(monto) == int:
        self._errors['monto'] = self.error_class(['Solo se permite valores numericos'])
    return self.cleaned_data