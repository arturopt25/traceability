from django.db import models
from logistica.models import *
from produccion.models import *
# Create your models here.


CHOICE = [(1, 'aprobado'), (2, 'rechazado')]


class Revision_compra(models.Model):



    id = models.AutoField(primary_key = True)
    Compra = models.OneToOneField(Compra, on_delete = models.CASCADE)
    status = models.BooleanField(choices=CHOICE, default=1, blank=False)

class Revision_produccion(models.Model):
    id = models.AutoField(primary_key = True)
    Produccion_de_lote = models.OneToOneField(Produccion_de_lote, on_delete = models.CASCADE)
    status = models.BooleanField(choices=CHOICE, default=1, blank=False)
