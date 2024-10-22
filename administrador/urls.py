from django.urls import path

from administrador.views import dashboard, pedidos, ventas, clientes

urlpatterns=[
    path('', dashboard, name='dashboard'),
    path('pedidos/', pedidos, name='pedidos'),
    path('ventas/', ventas, name='ventas'),
    path('clientes/', clientes, name='clientes')
]