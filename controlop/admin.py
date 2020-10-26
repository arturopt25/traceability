from django.contrib import admin
from .models import Revision_compra, Revision_produccion
# Register your models here.






class ReviCompraAdmin(admin.ModelAdmin):
    list_display = ("Compra", "status")


admin.site.register(Revision_compra, ReviCompraAdmin)


class ReviProducAdmin(admin.ModelAdmin):
    list_display = ("Produccion_de_lote", "status")


admin.site.register(Revision_produccion, ReviProducAdmin)
