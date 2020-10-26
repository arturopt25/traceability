from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import NuevaVenta
# Create your views here.

def index(request):

    return render(request, 'ventas/index.html')

def venta(request):
    context = {
        'form': NuevaVenta()
    }
    form = NuevaVenta()
    if request.method == "POST":
        form =NuevaVenta(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return HttpResponseRedirect('venta')
    return render(request, 'ventas/venta.html', context)
