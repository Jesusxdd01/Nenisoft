from django.urls import path

from administrador.views import administrador, pedidos, ventas, clientes

urlpatterns=[
    path('', administrador, name='administrador'),
    path('pedidos/', pedidos, name='pedidos'),
    path('ventas/', ventas, name='ventas'),
    path('clientes/', clientes, name='clientes')
]