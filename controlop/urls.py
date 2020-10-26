from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recompra', views.recompra, name= 'recompra'),
    path('repro', views.repro, name= 'repro'),
]
