from django import forms
from .models import Produccion_de_lote
from logistica.models import *


class DateInput(forms.DateInput):
    input_type = 'date'




class NuevaProduccion(forms.ModelForm):

    fecha_de_emision = forms.DateField(widget=DateInput)
    fecha_de_fabricacion = forms.DateField(widget=DateInput)
    fecha_de_vencimiento = forms.DateField(widget=DateInput)

    class Meta:
        model = Produccion_de_lote
        fields = ['descripcion', 'lote', 'Orden_de_produccion', 'fecha_de_emision', 'fecha_de_fabricacion','fecha_de_vencimiento', 'gerente_encargado', 'observaciones']
