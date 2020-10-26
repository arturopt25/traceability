from django.db import models
from logistica.models import *
# Create your models here.

class Produccion_de_lote(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField('descripcion', max_length = 255, blank = False, null = False)
    lote = models.IntegerField('lote')
    Orden_de_produccion = models.OneToOneField(Orden_de_produccion, on_delete = models.CASCADE)
    fecha_de_emision = models.DateField('fecha de emision', blank = False, null = False)
    fecha_de_fabricacion = models.DateField('fecha de fabricacion', blank = False, null = False)
    fecha_de_vencimiento = models.DateField('fecha de vencimiento', blank = False, null = False)
    gerente_encargado = models.CharField('gerente encargado', max_length = 255, blank = False, null = False)
    observaciones = models.CharField('observaciones', max_length = 255, blank = False, null = False)
