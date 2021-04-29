from django.shortcuts import render, redirect
from .forms import reciboForm
from .models import recibo
from django.http import HttpResponseRedirect

def home_pago(request):
    titulo = 'Home Pagos'
    return render(request, "pagos.html", {'titulo':titulo} )

def MESES(i):
    switcher={
    1:'Enero',
    2:'Febrero',
    3:'Marzo',
    4:'Abril',
    5:'Mayo',
    6:'Junio',
    7:'Julio',
    8:'Agosto',
    9:'Septiembre',
    10:'Octubre',
    11:'Noviembre',
    12:'Diciembre'
    }
    return switcher.get(i, "Mes invalido")

def find_pagos(request):
    valido  = False
    titulo  = 'Busca Pagos por casa'
    recibos = ''
    mensaje = ''
    if request.method == 'POST':
        buscar = request.POST['buscando']
        valido = True
        if buscar == '':
            mensaje = 'Favor de infomar # de Casa valida '
            valido = False
        if valido:
            recibos = recibo.objects.filter(casa__exact=buscar).order_by('mes')
            valido = True
    else:
        valido = False
        buscar = ''
    return render(request, "busca_pago.html", {'titulo':titulo, 'buscando':buscar, 'recibos':recibos, 'mensaje':mensaje, 'valido':valido } )

def add_pago(request):
    enviado = False
    titulo = "Ingresar Pago"
    mensaje =''
    pago = reciboForm(request.POST)    
    if request.method == "POST":
        if pago.is_valid():
            pago.save()
            return HttpResponseRedirect('.?enviado=True')
    else:
        mensaje ='Recibo ingresado'
        if 'enviado' in request.GET:
            enviado = True
    return render(request, "aplicar_pagos.html", {'form':pago , 'enviado':enviado, 'titulo':titulo,'mensaje':mensaje} )

def pago_form(request, pago_id=0):
    titulo = 'Editar Pago'    
    if request.method == 'GET':
        if pago_id == 0:
            form = pago_form()
        else:
            pago = recibo.objects.get(pk=pago_id)
            form = reciboForm(instance=recibo)
        return render(request,"mod_pago.html", {'titulo':titulo, 'pago':form, 'pago_id':pago_id} )
    else:
        if pago_id == 0:
            form = reciboForm(request.POST)
        else:
            pago = recibo.objects.get(pk=pago_id)
            form = reciboForm(request.POST, instance=pago)
            if form.is_valid():
                form.save()
                return redirect(find_pagos)
            else:
                return render(request,"mod_pago.html", {'titulo':titulo, 'pago':form,'pago_id':pago_id} )

def del_pago(request, pago_id=0):
    pago = recibo.objects.get(pk=pago_id)
    pago.delete()
    return redirect(find_pagos)            
