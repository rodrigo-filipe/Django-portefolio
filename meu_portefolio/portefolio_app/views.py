from django.shortcuts import render, get_object_or_404
from .models import Tecnologia

# Create your views here.

def home(request):
    return render(request, 'home.html')

def projetos(request):
    return render(request, 'projetos.html')

def tecnologias(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'tecnologias.html', {'tecnologias': tecnologias})

def tecnologia_detalhe(request, pk):
    tecnologia = get_object_or_404(Tecnologia, pk=pk)
    return render(request, 'tecnologia_detalhe.html', {'tecnologia': tecnologia})

def contacto(request):
    return render(request, 'contacto.html')

def faculdade(request):
    return render(request, 'faculdade.html')