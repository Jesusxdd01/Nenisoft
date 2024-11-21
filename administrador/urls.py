from django.urls import path
from .views import AdministradorView, PedidosView, VentasView, ClientesView

urlpatterns = [
    path('', AdministradorView.as_view(), name='administrador'),
    path('pedidos/', PedidosView.as_view(), name='pedidos'),
    path('ventas/', VentasView.as_view(), name='ventas'),
    path('clientes/', ClientesView.as_view(), name='clientes')
]
