from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(login_required, name='dispatch')
class AdministradorView(View):
    def get(self, request):
        return render(request, 'dashboard.html')

@method_decorator(login_required, name='dispatch')
class PedidosView(View):
    def get(self, request):
        return render(request, 'pedidos.html')

@method_decorator(login_required, name='dispatch')
class VentasView(View):
    def get(self, request):
        return render(request, 'ventas.html')

@method_decorator(login_required, name='dispatch')
class ClientesView(View):
    def get(self, request):
        return render(request, 'clientes.html')
    
@method_decorator(login_required, name='dispatch')
class ProductosView(View):
    def get(self, request):
        return render(request, 'productos.html')
    
@method_decorator(login_required, name='dispatch')
class MiPerfilView(View):
    def get(self, request):
        return render(request, 'miPerfil.html')
    
@method_decorator(login_required, name='dispatch')
class PreguntasFrecuentesView(View):
    def get(self, request):
        return render(request, 'faq.html')

