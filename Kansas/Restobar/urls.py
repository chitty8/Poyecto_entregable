from django.urls import path, include
from .views import cliente, clientes, clientesFormulario, inicio, lista_clientes, lista_mesas, lista_meseros, mesa, mesas, mesasFormulario, mesero, meseros, meserosFormulario


urlpatterns = [
    path('agrega-cliente/<nombre>/<apellido>', clientes),
    path('lista_clientes', lista_clientes),
    path('agrega-mesero/<nombre>/<apellido>/<dni>', mesero),
    path('agrega-mesa/<nombre>/<numero>', mesa),
    path('lista_meseros', lista_meseros),
    path('lista_mesas', lista_mesas),
    path("", inicio, name="Inicio"),
    path("cliente/",cliente,name="Cliente"),
    path("meseros/", meseros,name="Meseros"), 
    path("mesas/", mesas,name="Mesas"),
    path("clientesFormulario", clientesFormulario,name="ClientesFormulario"),
    path("meserosFormulario", meserosFormulario,name="MeserosFormulario"),
    path("mesasFormulario", mesasFormulario,name="MesasFormulario"),
]