from django.urls import path
from .views import HomeView, PlanesView, BlogView, LoginView, CrearCuentaView, LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('planes/', PlanesView.as_view(), name='planes'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('login/', LoginView.as_view(), name='login'),
    path('crearCuenta/', CrearCuentaView.as_view(), name='crearCuenta'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
