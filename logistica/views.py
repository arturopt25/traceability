from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ComprasForm, NuevaCompra, NuevoInsumo, NuevoDespacho, NuevoPt, NuevaOrden, TrazabilidadForm

# Create your views here.
def index(request):
    return render(request, 'logistica/index.html')

def despacho(request):
    context = {
        'form': NuevoDespacho()
    }
    form = NuevoDespacho()
    if request.method == "POST":
        form =NuevoDespacho(request.POST)
        if form.is_valid():
            instancia3 = form.save(commit=False)
            instancia3.save()
            return HttpResponseRedirect('despacho')
    return render(request, 'logistica/despacho.html', context)

def compras(request):
    context = {
        'form': NuevaCompra()
    }
    form = NuevaCompra()
    if request.method == "POST":
        form =NuevaCompra(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return HttpResponseRedirect('compras')

    return render(request, 'logistica/compras.html', context)

def insumos(request):
    context = {
        'form': NuevoInsumo()
    }
    form = NuevoInsumo()
    if request.method == "POST":
        form =NuevoInsumo(request.POST)
        if form.is_valid():
            instancia2 = form.save(commit=False)
            instancia2.save()
            return HttpResponseRedirect('insumos')
    return render(request, 'logistica/insumos.html', context)

def produccion(request):
    context = {
        'form': NuevaOrden()
    }
    form = NuevaOrden()
    if request.method == "POST":
        form =NuevaOrden(request.POST)
        if form.is_valid():
            instancia5 = form.save(commit=False)
            instancia5.save()
            return HttpResponseRedirect('produccion')
    return render(request, 'logistica/produccion.html', context)

def terminado(request):
    context = {
        'form': NuevoPt()
    }
    form = NuevoPt()
    if request.method == "POST":
        form =NuevoPt(request.POST)
        if form.is_valid():
            instancia4 = form.save(commit=False)
            instancia4.save()
            return HttpResponseRedirect('terminado')
    return render(request, 'logistica/terminado.html', context)


def traza(request):
    context = {
        'form': TrazabilidadForm()
    }
    form = TrazabilidadForm()
    if request.method == "POST":
        form =TrazabilidadForm(request.POST)
        if form.is_valid():
            instancia8 = form.save(commit=False)
            instancia8.save()
            return HttpResponseRedirect('traza')
    return render(request, 'logistica/traza.html', context)



# aqui esta la seccion de los formularios in the mix




#def crear_compras(request):
#    print(request.method)
#    if request.method == 'POST':
#        form = ComprasForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/logistica/compras.html')
#    else:
#        form = ComprasForm()

#    return render(request, '/logistica/compras.html', {'form': form})

    #form = ComprasForm(request.POST or None)
    #if form.is_valid():
    #    form.save()
    #    form = ComprasForm()

    #context = {
    #    'form': form
    #}
    #return render(request, "logistica/compras.html", context)
