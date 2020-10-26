from django.db import models

# Create your models here.

class Venta(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField('descripcion', max_length = 255, blank = False, null = False)
    cantidad = models.IntegerField('cantidad', default =0)
    fecha = models.DateField('fecha', blank = False, null= False)
