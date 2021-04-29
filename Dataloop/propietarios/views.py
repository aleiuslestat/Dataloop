from django.shortcuts import render, redirect
from .forms import ViviendaForm
from .models import Vivienda
from django.http import HttpResponseRedirect

# Create your views here.
def Propietarios(request):
    titulo = 'Home Propietarios'
    return render(request, "propietarios.html", {'titulo':titulo} )


def det_propietario(request, vivienda_id):
    titulo = 'Detalle Propietario'
    propietario = Vivienda.objects.get(pk=vivienda_id)
    return render(request, "det_propietario.html", {'titulo':titulo, 'propietario':propietario} )

def Propietario_form(request, vivienda_id=0):
    titulo = 'Editar Propietario'    
    if request.method == 'GET':
        if vivienda_id == 0:
            form = Propietario_form()
        else:
            propietario = Vivienda.objects.get(pk=vivienda_id)
            form = ViviendaForm(instance=propietario)
        return render(request,"mod_propietario.html", {'titulo':titulo, 'propietario':form} )
    else:
        if vivienda_id == 0:
            form = ViviendaForm(request.POST)
        else:
            propietario = Vivienda.objects.get(pk=vivienda_id)
            form = ViviendaForm(request.POST, instance=propietario)
            if form.is_valid():
                form.save()
                return redirect(det_propietario,vivienda_id = vivienda_id )
            else:
                return render(request,"mod_propietario.html", {'titulo':titulo, 'propietario':form} )

def del_propietario(request, vivienda_id=None):
    titulo = 'Borrar Propietario'
    propietario = Vivienda.objects.get(pk=vivienda_id)
    propietario.delete()
    return redirect(list_propietario)


def list_propietario(request):
    titulo = 'Lista de casas registradas'
    propietarios_lista = Vivienda.objects.all().order_by('numero')
    return render(request, "list_propietario.html", {'titulo':titulo, 'propietarios_lista':propietarios_lista} )

def add_propietario(request):
    enviado = False
    titulo = "Agregar Vivienda"
    if request.method == "POST":
        form = ViviendaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('.?enviado=True')
    else:
        form = ViviendaForm
        if 'enviado' in request.GET:
            enviado = True
    return render(request, "add_propietario.html", {'form':form , 'enviado':enviado, 'titulo':titulo} )