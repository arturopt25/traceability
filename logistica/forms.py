from django import forms
from .models import Compra, Almacen_insumo, Despacho, Almacen_pt, Orden_de_produccion, Trazabilidad

class DateInput(forms.DateInput):
    input_type = 'date'




class ComprasForm(forms.Form):
    descripcion = forms.CharField()
    medida = forms.IntegerField()
    fecha_compra = forms.DateField(widget=DateInput)


class NuevaCompra(forms.ModelForm):

    fecha_compra = forms.DateField(widget=DateInput)

    class Meta:
        model = Compra
        fields = ['descripcion', 'medida', 'fecha_compra']
        #widgets = {
        #    'fecha_compra' : forms.DateInput()
        #}

class NuevoInsumo(forms.ModelForm):
    fecha_ingreso = forms.DateField(widget=DateInput)

    class Meta:
        model = Almacen_insumo
        fields = ['descripcion', 'tipo', 'fecha_ingreso','medida']

class NuevoDespacho(forms.ModelForm):
    fecha_despacho = forms.DateField(widget=DateInput)

    class Meta:
        model = Despacho
        fields = ['fecha_despacho', 'gerente_encargado']


class NuevoPt(forms.ModelForm):

    class Meta:
        model = Almacen_pt
        fields = ['descripcion', 'cantidad']


class TrazabilidadForm(forms.ModelForm):

    fecha_de_emision = forms.DateField(widget=DateInput)

    class Meta:
        model = Trazabilidad
        fields = ['descripcion', 'lote_compra', 'lote_insumos', 'cantidad', 'orden_produccion', 'lote_produccion', 'lote_terminado', 'fecha_de_emision', 'lote_venta', 'orden_de_despacho', 'status', 'gerente_encargado']

class NuevaOrden(forms.ModelForm):

    fecha_de_emision = forms.DateField(widget=DateInput)

    class Meta:
        model = Orden_de_produccion
        fields = ['descripcion', 'lote', 'Orden_de_produccion', 'fecha_de_emision', 'gerente_encargado', 'Formula_maestra', 'observaciones']
