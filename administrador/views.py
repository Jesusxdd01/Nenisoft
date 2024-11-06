from django.shortcuts import render, HttpResponse

# Create your views here.
def administrador(request):
    return render (request, 'dashboard.html')

def pedidos(request):
    return render (request, 'pedidos.html')

def ventas(request):
    return render (request, 'ventas.html')

def clientes(request):
    return render (request, 'clientes.html')