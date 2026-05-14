from django.shortcuts import render, get_object_or_404
from .models import Tecnologia, Docente, UnidadeCurricular

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

def docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes.html', {'docentes': docentes})

def docente_detalhe(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    return render(request, 'docente_detalhe.html', {'docente': docente})

def ucs(request):
    ucs = UnidadeCurricular.objects.all().order_by('ano', 'semestre')
    return render(request, 'unidades_curriculares.html', {'ucs': ucs})

def uc_detalhe(request, pk):
    uc = get_object_or_404(UnidadeCurricular, pk=pk)
    return render(request, 'unidade_curricular_detalhe.html', {'uc': uc})