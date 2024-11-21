from django.urls import path
from .views import AdministradorView, PedidosView, VentasView, ClientesView, MiPerfilView, PreguntasFrecuentesView, ProductosView

urlpatterns = [
    path('', AdministradorView.as_view(), name='administrador'),
    path('pedidos/', PedidosView.as_view(), name='pedidos'),
    path('productos/', ProductosView.as_view(), name='productos'),
    path('ventas/', VentasView.as_view(), name='ventas'),
    path('clientes/', ClientesView.as_view(), name='clientes'),
    path('miPerfil/', MiPerfilView.as_view(), name='miPerfil'),
    path('preguntasFrecuentes/', PreguntasFrecuentesView.as_view(), name='preguntasFrecuentes'),
]
