from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render (request, 'index.html')

def planes(request):
    return render (request, 'planes.html')

def blog(request):
    return render (request, 'blog.html')

def login(request):
    return render (request, 'login.html')

def crearCuenta(request):
    return render (request, 'crearCuenta.html')