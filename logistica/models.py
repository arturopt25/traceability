from django.db import models

# Create your models here.



class Compra(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField('descripcion', max_length = 255, blank = False, null = False)
    medida = models.IntegerField('medida', default =0)
    fecha_compra = models.DateField('fecha de compra', blank = False, null= False)


class Almacen_insumo(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField('descripcion', max_length = 255, blank = False, null = False)
    tipo = models.CharField('tipo', max_length = 255, blank = False, null = False)
    fecha_ingreso = models.DateField('fecha de ingreso', blank = False, null= False)
    medida = models.IntegerField('medida', default =0)


class Formula_maestra(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField('descripcion', max_length = 255, blank = False, null = False)
    cantidad = models.FloatField('cantidad')


class Despacho(models.Model):
    id = models.AutoField(primary_key = True)
    fecha_despacho = models.DateField('fecha de despacho', blank = False, null= False)
    gerente_encargado = models.CharField('gerente encargado', max_length = 255, blank = False, null = False)


class Almacen_pt(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField('descripcion', max_length = 255, blank = False, null = False)
    cantidad = models.IntegerField('cantidad', default =0)


class Orden_de_produccion(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField('descripcion', max_length = 255, blank = False, null = False)
    lote = models.IntegerField('lote')
    Orden_de_produccion = models.IntegerField('orden de produccion')
    fecha_de_emision = models.DateField('fecha de emision', blank = False, null = False)
    gerente_encargado = models.CharField('gerente encargado', max_length = 255, blank = False, null = False)
    Formula_maestra = models.OneToOneField(Formula_maestra, on_delete = models.CASCADE)
    observaciones = models.CharField('observaciones', max_length = 255, blank = False, null = False)


    class Meta:

        verbose_name = 'Orden de produccion'
        verbose_name_plural = 'Ordenes de produccion'

    def __str__(self):
        return self.descripcion


class Trazabilidad(models.Model):

    CHOICE = [(1, 'aprobado'), (2, 'rechazado')]

    descripcion = models.CharField('descripcion', max_length = 255, blank = False, null = False)
    lote_compra = models.IntegerField('codigo de compra')
    lote_insumos = models.IntegerField('lote de insumos')
    cantidad = models.IntegerField('unidad de medida')
    orden_produccion = models.IntegerField('orden de produccion')
    lote_produccion = models.IntegerField('produccion de lote')
    lote_terminado = models.IntegerField('codigo de producto terminado')
    fecha_de_emision = models.DateField('fecha de emision', blank = False, null = False)
    lote_venta = models.IntegerField('numero de factura')
    orden_de_despacho = models.IntegerField('orden de despacho')
    status = models.BooleanField(choices=CHOICE, default=1, blank=False)
    gerente_encargado = models.CharField('gerente encargado', max_length = 255, blank = False, null = False)
