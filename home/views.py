from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

class PlanesView(View):
    def get(self, request):
        return render(request, 'planes.html')

class BlogView(View):
    def get(self, request):
        return render(request, 'blog.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('administrador')
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})

class CrearCuentaView(View):
    def get(self, request):
        return render(request, 'crearCuenta.html')
    
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            return render(request, 'crearCuenta.html', {'error': 'El usuario ya existe'})
        else:
            user = User.objects.create_user(username=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            return redirect('login')


class LogoutView(View): 
    def get(self, request): 
        logout(request) 
        return redirect('login')