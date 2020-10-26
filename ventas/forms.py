from django import forms
from .models import Venta



class DateInput(forms.DateInput):
    input_type = 'date'



class NuevaVenta(forms.ModelForm):

    fecha = forms.DateField(widget=DateInput)

    class Meta:
        model = Venta
        fields = ['descripcion', 'cantidad', 'fecha']
