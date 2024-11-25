from django.urls import path
from .views import AdministradorView, PedidosView, VentasView, ClientesView, MiPerfilView, PreguntasFrecuentesView, ProductosView
from administrador.views import clienteCreate, clienteUpdate, clienteDelete

urlpatterns = [
    path('', AdministradorView.as_view(), name='administrador'),
    path('pedidos/', PedidosView.as_view(), name='pedidos'),
    path('productos/', ProductosView.as_view(), name='productos'),
    path('ventas/', VentasView.as_view(), name='ventas'),
    path('clientes/', ClientesView.as_view(), name='clientes'),
    path('miPerfil/', MiPerfilView.as_view(), name='miPerfil'),
    path('preguntasFrecuentes/', PreguntasFrecuentesView.as_view(), name='preguntasFrecuentes'),
    path('cliente/create', clienteCreate, name='clienteCreate'),
    path('cliente/update/<int:id>', clienteUpdate, name='clienteUpdate'),
    path('cliente/delete/<int:id>', clienteDelete, name='clienteDelete'),
]
