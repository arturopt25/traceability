from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import NuevaProduccion
# Create your views here.

def index(request):
    return render(request, 'produccion/index.html')


def produc(request):
    context = {
        'form': NuevaProduccion()
    }
    form = NuevaProduccion()
    if request.method == "POST":
        form =NuevaProduccion(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return HttpResponseRedirect('produc')
    return render(request, 'produccion/produc.html', context)
