import json


from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.core import serializers




from .models import Compra, Almacen_insumo, Formula_maestra, Despacho, Almacen_pt, Orden_de_produccion, Trazabilidad
# Register your models here.


all_data = serializers.serialize("json", Orden_de_produccion.objects.all())



admin.site.register(Formula_maestra)


class TrazabilidadAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "lote_compra", "cantidad", "orden_produccion", "lote_produccion", "fecha_de_emision")
    search_fields = ['lote_produccion']

admin.site.register(Trazabilidad, TrazabilidadAdmin)

class DespachoAdmin(admin.ModelAdmin):
    list_display = ("fecha_despacho", "gerente_encargado")

admin.site.register(Despacho, DespachoAdmin)


class Orden_de_produccion_Admin(admin.ModelAdmin):
    list_display = ("descripcion", "lote", "fecha_de_emision", "gerente_encargado")
    ordering = ["-fecha_de_emision"]
    search_fields = ['lote']

    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            Orden_de_produccion.objects.annotate(date=TruncDay("fecha_de_emision"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json, "all_data": all_data}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(Orden_de_produccion, Orden_de_produccion_Admin)


class CompraAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "medida", "fecha_compra")

admin.site.register(Compra, CompraAdmin)

class Almacen_insumo_Admin(admin.ModelAdmin):
    list_display = ("descripcion", "tipo", "fecha_ingreso", "medida")

admin.site.register(Almacen_insumo, Almacen_insumo_Admin)


class Almacen_pt_Admin(admin.ModelAdmin):
    list_display = ("descripcion", "cantidad")

admin.site.register(Almacen_pt, Almacen_pt_Admin)
