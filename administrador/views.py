from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from administrador.models import Cliente, Producto,Pedido, Venta
from administrador.forms import ClienteForm
from django.shortcuts import render, redirect

@method_decorator(login_required, name='dispatch')
class AdministradorView(View):
    def get(self, request):
        return render(request, 'dashboard.html')

@method_decorator(login_required, name='dispatch')
class PedidosView(View):
    def get(self, request):
        pedidos = Pedido.objects.all()
        context = {'pedidos': pedidos} 
        return render(request, 'pedidos.html', context)

@method_decorator(login_required, name='dispatch')
class VentasView(View):
    def get(self, request):
        ventas = Venta.objects.all()
        context = {'ventas': ventas} 
        return render(request, 'ventas.html',context)

@method_decorator(login_required, name='dispatch')
class ClientesView(View):
    def get(self, request):
        clientes = Cliente.objects.all()
        context = {'clientes': clientes} 
        return render(request, 'clientes.html', context) 
    
@method_decorator(login_required, name='dispatch')
class ProductosView(View):
    def get(self, request):
        productos = Producto.objects.all()
        context = {'productos': productos} 
        return render(request, 'productos.html',context)
    
@method_decorator(login_required, name='dispatch')
class MiPerfilView(View):
    def get(self, request):
        return render(request, 'miPerfil.html')
    
@method_decorator(login_required, name='dispatch')
class PreguntasFrecuentesView(View):
    def get(self, request):
        return render(request, 'faq.html')



def clienteCreate(request):
    if request.method == 'POST': #Se quiere guardar form lleno
        form = ClienteForm(request.POST) #Se envia form con metodo post
        if form.is_valid(): #Si esta bien el form(lleno apropiadamente)
            form.save() #Guarda en un registro en la tabla de la BD
            return redirect('clientes') #Redirige al listado de carreras
    else:
        form = ClienteForm() #Se pinta formulario al que ingresar
    return render (request, 'clientesCreate.html', {'form':form}) 

def clienteUpdate(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance = cliente)
    else:
        form = ClienteForm(request.POST, instance = cliente)
        if form.is_valid():
            form.save()
        return redirect('clientes')
    return render (request, 'clientesCreate.html', {'form':form}) 

def clienteDelete(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    return render (request, 'clienteDelete.html', {'cliente':cliente})