from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('despacho', views.despacho, name= 'despacho'),
    path('compras', views.compras, name= 'compras'),
    path('insumos', views.insumos, name= 'insumos'),
    path('produccion', views.produccion, name= 'produccion'),
    path('terminado', views.terminado, name= 'terminado'),
    path('traza', views.traza, name= 'traza'),
]
