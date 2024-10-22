from django.urls import path

from home.views import home, planes, blog, login, crearCuenta

urlpatterns=[
    path('', home, name='home'),
    path('planes/', planes, name='planes'),
    path('blog/', blog, name='blog'),
    path('login/', login, name='login'),
    path('crearCuenta/', crearCuenta, name='crearCuenta'),
]