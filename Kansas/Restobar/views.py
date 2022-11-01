from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models  import Clientes, Mesas, Meseros
# Create your views here.


def clientes(request, nombre, apellido):

    clientes = Clientes(nombre=nombre, apellido=apellido)
    clientes.save()

    return HttpResponse(f"""
    <p>Cliente:{clientes.nombre} - Apellido {clientes.apellido} Agregado! </p>
    """)

def mesero(request, nombre, apellido, dni):

    mesero = Meseros(nombre=nombre, apellido=apellido, dni=dni)
    mesero.save()

    return HttpResponse(f"""
    <p>Cliente:{mesero.nombre} - Apellido {mesero.apellido} con dni {mesero.dni} Agregado! </p>
    """)

def mesa(request, nombre, numero):

    mesa = Mesas(nombre=nombre, numero=numero)
    mesa.save()

    return HttpResponse(f"""
    <p>Cliente:{mesa.nombre} - Numero de mesa {mesa.numero} Agregado! </p>
    """)



def lista_clientes(request):
    lista = Clientes.objects.all()

    return render(request, "lista_clientes.html", {"lista_clientes":lista})

def lista_meseros(request):
    lista = Meseros.objects.all()

    return render(request, "lista_meseros.html", {"lista_meseros":lista})

def lista_mesas(request):
    lista = Mesas.objects.all()

    return render(request, "lista_mesas.html", {"lista_mesas":lista})


def inicio(request):
    return render(request, "inicio.html")




def cliente(request):
    lista = Clientes.objects.all()
    return render(request, "cliente.html", {"lista_clientes":lista})


def meseros(request):
    lista = Meseros.objects.all()
    return render(request, "meseros.html", {"lista_meseros":lista})


def mesas(request):
    lista = Mesas.objects.all()
    return render(request, "mesas.html", {"lista_mesas":lista})


def clientesFormulario(request):
    if request.method =="POST":
        clientes=Clientes(nombre=request.POST["nombre"], apellido=request.POST["apellido"])
        clientes.save()

        return redirect("/Restobar/cliente")

    return render(request, "clientesFormulario.html")

def meserosFormulario(request):

    if request.method =="POST":
        meseros=Meseros(nombre=request.POST["nombre"], apellido=request.POST["apellido"], dni=request.POST["dni"])
        meseros.save()

        return redirect("/Restobar/meseros")

    return render(request, "meserosFormulario.html")

def mesasFormulario(request):

    if request.method =="POST":
        mesas=Mesas(nombre=request.POST["nombre"], numero=request.POST["numero"])
        mesas.save()

        return redirect("/Restobar/mesas")

    return render(request, "mesasFormulario.html")