from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def projetos(request):
    return render(request, 'projetos.html')

def tecnologias(request):
    return render(request, 'tecnologias.html')

def contacto(request):
    return render(request, 'contacto.html')