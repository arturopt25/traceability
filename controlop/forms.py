from django import forms
from .models import Revision_compra, Revision_produccion
from logistica.models import *
from produccion.models import *



class DateInput(forms.DateInput):
    input_type = 'date'



class ReviCompra(forms.ModelForm):
    class Meta:
        model = Revision_compra
        fields = ['Compra', 'status']

class ReviProduc(forms.ModelForm):
    class Meta:
        model = Revision_produccion
        fields = ['Produccion_de_lote', 'status']
