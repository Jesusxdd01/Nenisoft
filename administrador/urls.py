from django.urls import path
from .views import AdministradorView, PedidosView, VentasView, ClientesView, MiPerfilView, PreguntasFrecuentesView, ProductosView, PedidosClientesView, VentasClientesView
from administrador.views import clienteCreate, clienteUpdate, clienteDelete, productoCreate, productoDelete, productoUpdate, pedidoCreate, pedidoDelete, pedidoUpdate, ventaUpdate, ventaPagada

urlpatterns = [
    path('', AdministradorView.as_view(), name='administrador'),
    path('pedidos/', PedidosView.as_view(), name='pedidos'),
    path('productos/', ProductosView.as_view(), name='productos'),
    path('ventas/', VentasView.as_view(), name='ventas'),
    path('clientes/', ClientesView.as_view(), name='clientes'),
    path('miPerfil/', MiPerfilView.as_view(), name='miPerfil'),
    path('preguntasFrecuentes/', PreguntasFrecuentesView.as_view(), name='preguntasFrecuentes'),
    path('pedidos/cliente/<int:cliente_id>/', PedidosClientesView.as_view(), name='pedidosCliente'),
    path('ventas/cliente/<int:cliente_id>/', VentasClientesView.as_view(), name='ventasCliente'),
    path('cliente/create', clienteCreate, name='clienteCreate'),
    path('cliente/update/<int:id>', clienteUpdate, name='clienteUpdate'),
    path('cliente/delete/<int:id>', clienteDelete, name='clienteDelete'),
    path('producto/create', productoCreate, name='productoCreate'),
    path('producto/update/<int:id>', productoUpdate, name='productoUpdate'),
    path('producto/delete/<int:id>', productoDelete, name='productoDelete'),
    path('pedido/create', pedidoCreate, name='pedidoCreate'),
    path('pedido/update/<int:id>', pedidoUpdate, name='pedidoUpdate'),
    path('pedido/delete/<int:id>', pedidoDelete, name='pedidoDelete'),
    path('venta/update/<int:id>', ventaUpdate, name='ventaUpdate'),
    path('venta/ventaPagada/<int:id>/', ventaPagada, name='ventaPagada'),
    
]
