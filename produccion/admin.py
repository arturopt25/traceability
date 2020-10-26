import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncDay

from .models import Produccion_de_lote
# Register your models here.



class Produccion_de_lote_Admin(admin.ModelAdmin):
    list_display = ("descripcion", "lote", "fecha_de_emision", "gerente_encargado")
    ordering = ["-fecha_de_emision"]


    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            Produccion_de_lote.objects.annotate(date=TruncDay("fecha_de_emision"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(Produccion_de_lote, Produccion_de_lote_Admin)
