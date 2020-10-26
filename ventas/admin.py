from django.contrib import admin
from .models import Venta
# Register your models here.




class VentaAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "cantidad", "fecha")

admin.site.register(Venta, VentaAdmin)
