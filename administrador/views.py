from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from administrador.models import Cliente, Producto,Pedido, Venta
from administrador.forms import ClienteForm, ProductoForm, PedidoForm, VentaForm
from django.shortcuts import render, redirect, get_object_or_404

@method_decorator(login_required, name='dispatch')
class AdministradorView(View):
    def get(self, request):
        return render(request, 'dashboard.html')

@method_decorator(login_required, name='dispatch')
class PedidosView(View):
    def get(self, request):
        # Filtrar pedidos por el usuario autenticado
        pedidos = Pedido.objects.filter(user=request.user)
        context = {'pedidos': pedidos} 
        return render(request, 'pedidos.html', context)

@method_decorator(login_required, name='dispatch')
class PedidosClientesView(View):
    def get(self, request, cliente_id):
        # Obtener el cliente y asegurar que pertenece al usuario autenticado
        cliente = get_object_or_404(Cliente, id=cliente_id, user=request.user)
        # Filtrar pedidos por el cliente y el usuario autenticado
        pedidos = Pedido.objects.filter(cliente=cliente, user=request.user)
        context = {'pedidos': pedidos, 'cliente': cliente} 
        return render(request, 'pedidos.html', context)
    
@method_decorator(login_required, name='dispatch')
class VentasView(View):
    def get(self, request):
        # Filtrar ventas por el usuario autenticado
        ventas = Venta.objects.filter(user=request.user)
        context = {'ventas': ventas} 
        return render(request, 'ventas.html', context)
class VentasClientesView(View):
    def get(self, request, cliente_id):
        # Obtener el cliente y asegurar que pertenece al usuario autenticado
        cliente = get_object_or_404(Cliente, id=cliente_id, user=request.user)
        # Filtrar ventas por el usuario autenticado
        ventas = Venta.objects.filter(cliente=cliente,user=request.user)
        context = {'ventas': ventas,'cliente': cliente} 
        return render(request, 'ventas.html', context)
@method_decorator(login_required, name='dispatch')
class ClientesView(View):
    def get(self, request):
        # Filtrar los clientes por el usuario autenticado
        clientes = Cliente.objects.filter(user=request.user)
        context = {'clientes': clientes} 
        return render(request, 'clientes.html', context)
    
@method_decorator(login_required, name='dispatch')
class ProductosView(View):
    def get(self, request):
        # Filtrar productos por el usuario autenticado
        productos = Producto.objects.filter(user=request.user)
        context = {'productos': productos} 
        return render(request, 'productos.html', context)
    
@method_decorator(login_required, name='dispatch')
class MiPerfilView(View):
    def get(self, request):
        return render(request, 'miPerfil.html')
    
@method_decorator(login_required, name='dispatch')
class PreguntasFrecuentesView(View):
    def get(self, request):
        return render(request, 'faq.html')


#VISTAS CLIENTE
@login_required
def clienteCreate(request):
    if request.method == 'POST':  # Se quiere guardar form lleno
        form = ClienteForm(request.POST)  # Se envía form con método POST
        if form.is_valid():  # Si está bien el form (lleno apropiadamente)
            cliente = form.save(commit=False)
            cliente.user = request.user  # Asignar el usuario autenticado
            cliente.save()  # Guarda en un registro en la tabla de la BD
            return redirect('clientes')  # Redirige al listado de clientes
    else:
        form = ClienteForm()  # Se pinta formulario al que ingresar
    return render(request, 'clientesCreate.html', {'form': form})

@login_required
def clienteUpdate(request, id):
    cliente = get_object_or_404(Cliente, id=id, user=request.user)  # Asegurarse de que el cliente pertenezca al usuario
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
        return redirect('clientes')
    return render(request, 'clientesCreate.html', {'form': form})

@login_required
def clienteDelete(request, id):
    cliente = get_object_or_404(Cliente, id=id, user=request.user)  # Asegurarse de que el cliente pertenezca al usuario
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    return render(request, 'clienteDelete.html', {'cliente': cliente})


#VISTAS PRODUCTOS
@login_required
def productoCreate(request):
    if request.method == 'POST':  # Se quiere guardar form lleno
        form = ProductoForm(request.POST)  # Se envía form con método POST
        if form.is_valid():  # Si está bien el form (lleno apropiadamente)
            producto = form.save(commit=False)
            producto.user = request.user  # Asignar el usuario autenticado
            producto.save()  # Guarda en un registro en la tabla de la BD
            return redirect('productos')  # Redirige al listado de productos
    else:
        form = ProductoForm()  # Se pinta formulario al que ingresar
    return render(request, 'productosCreate.html', {'form': form})

@login_required
def productoUpdate(request, id):
    producto = get_object_or_404(Producto, id=id, user=request.user)  # Asegurarse de que el cliente pertenezca al usuario
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('productos')
    return render(request, 'productosCreate.html', {'form': form})

@login_required
def productoDelete(request, id):
    producto = get_object_or_404(Producto, id=id, user=request.user)  # Asegurarse de que el cliente pertenezca al usuario
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    return render(request, 'productosDelete.html', {'producto': producto})


#VISTAS PEDIDOS
@login_required
def pedidoCreate(request):
    if request.method == 'POST':  # Se quiere guardar form lleno
        form = PedidoForm(request.POST, user=request.user)  # Pasar el usuario autenticado
        if form.is_valid():  # Si está bien el form (lleno apropiadamente)
            pedido = form.save(commit=False)
            pedido.user = request.user  # Asignar el usuario autenticado
            pedido.save()  # Guarda en un registro en la tabla de la BD
            return redirect('pedidos')  # Redirige al listado de pedidos
    else:
        form = PedidoForm(user=request.user)  # Pasar el usuario autenticado
    return render(request, 'pedidosCreate.html', {'form': form})

@login_required
def pedidoUpdate(request, id):
    pedido = get_object_or_404(Pedido, id=id, user=request.user)  # Asegurarse de que el pedido pertenezca al usuario
    if request.method == 'GET':
        form = PedidoForm(instance=pedido, user=request.user)  # Pasar el usuario autenticado
    else:
        form = PedidoForm(request.POST, instance=pedido, user=request.user)  # Pasar el usuario autenticado
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.user = request.user  # Asegurar que el usuario autenticado se mantenga
            pedido.save()
        return redirect('pedidos')
    return render(request, 'pedidosCreate.html', {'form': form})

@login_required
def pedidoDelete(request, id):
    pedido = get_object_or_404(Pedido, id=id, user=request.user)  # Asegurarse de que el cliente pertenezca al usuario
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedidos')
    return render(request, 'pedidosDelete.html', {'pedido': pedido})


#VISTAS VENTAS
@login_required
def ventaUpdate(request, id):
    venta = get_object_or_404(Venta, id=id, user=request.user)  # Asegurarse de que el cliente pertenezca al usuario
    if request.method == 'GET':
        form = VentaForm(instance=venta)
    else:
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
        return redirect('ventas')
    return render(request, 'ventasUpdate.html', {'form': form})

@login_required
def ventaPagada(request, id):
    venta = get_object_or_404(Venta, id=id)
    venta.importeRestante = 0
    venta.save()
    return redirect('ventas')

