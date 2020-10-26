from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ReviCompra, ReviProduc
# Create your views here.


def index(request):
    return render(request, 'controlop/index.html')

def recompra(request):
    context = {
        'form': ReviCompra()
    }
    form = ReviCompra()
    if request.method == "POST":
        form = ReviCompra(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return HttpResponseRedirect('recompra')
    return render(request, 'controlop/recompra.html', context)

def repro(request):
    context = {
        'form': ReviProduc()
    }
    form = ReviProduc()
    if request.method == "POST":
        form = ReviProduc(request.POST)
        if form.is_valid():
            instancia2 = form.save(commit=False)
            instancia2.save()
            return HttpResponseRedirect('repro')
    return render(request, 'controlop/repro.html', context)
