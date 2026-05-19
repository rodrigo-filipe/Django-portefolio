from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Tecnologia, Docente, UnidadeCurricular, Projeto, TFC, MakingOf, CategoriaTecnologia
from .forms import ProjetoForm, TecnologiaForm, UnidadeCurricularForm, DocenteForm, TFCForm

def is_staff(user):
    return user.is_staff

# Create your views here.

def home(request):
    return render(request, 'home.html')

def sobre(request):
    # Procuramos as tecnologias associadas a este projeto "Meu Portefólio"
    # Assumindo que o projeto tem o título "Meu Portefólio" ou similar
    projeto_portfolio = Projeto.objects.filter(titulo__icontains='Portefólio').first()
    
    context = {
        'projeto': projeto_portfolio,
        'categorias': CategoriaTecnologia.objects.all().prefetch_related('tecnologias'),
        'making_ofs': MakingOf.objects.all().order_by('-data')
    }
    return render(request, 'sobre.html', context)

def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos.html', {'projetos': projetos})

def projeto_detalhe(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'projeto_detalhe.html', {'projeto': projeto})

@user_passes_test(is_staff)
def novo_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            projeto = form.save()
            return redirect('portefolio_app:project_detail', pk=projeto.pk)
    else:
        form = ProjetoForm()
    return render(request, 'generic_form.html', {'form': form, 'titulo': 'Novo Projeto'})

@user_passes_test(is_staff)
def edita_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == "POST":
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            projeto = form.save()
            return redirect('portefolio_app:project_detail', pk=projeto.pk)
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'generic_form.html', {'form': form, 'titulo': f'Editar Projeto: {projeto.titulo}'})

def tecnologias(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'tecnologias.html', {'tecnologias': tecnologias})

def tecnologia_detalhe(request, pk):
    tecnologia = get_object_or_404(Tecnologia, pk=pk)
    return render(request, 'tecnologia_detalhe.html', {'tecnologia': tecnologia})

@user_passes_test(is_staff)
def novo_tecnologia(request):
    if request.method == "POST":
        form = TecnologiaForm(request.POST, request.FILES)
        if form.is_valid():
            tecnologia = form.save()
            return redirect('portefolio_app:technology_detail', pk=tecnologia.pk)
    else:
        form = TecnologiaForm()
    return render(request, 'generic_form.html', {'form': form, 'titulo': 'Nova Tecnologia'})

@user_passes_test(is_staff)
def edita_tecnologia(request, pk):
    tecnologia = get_object_or_404(Tecnologia, pk=pk)
    if request.method == "POST":
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)
        if form.is_valid():
            tecnologia = form.save()
            return redirect('portefolio_app:technology_detail', pk=tecnologia.pk)
    else:
        form = TecnologiaForm(instance=tecnologia)
    return render(request, 'generic_form.html', {'form': form, 'titulo': f'Editar Tecnologia: {tecnologia.nome}'})

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

@user_passes_test(is_staff)
def novo_docente(request):
    if request.method == "POST":
        form = DocenteForm(request.POST, request.FILES)
        if form.is_valid():
            docente = form.save()
            return redirect('portefolio_app:docente_detail', pk=docente.pk)
    else:
        form = DocenteForm()
    return render(request, 'generic_form.html', {'form': form, 'titulo': 'Novo Docente'})

@user_passes_test(is_staff)
def edita_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == "POST":
        form = DocenteForm(request.POST, request.FILES, instance=docente)
        if form.is_valid():
            docente = form.save()
            return redirect('portefolio_app:docente_detail', pk=docente.pk)
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'generic_form.html', {'form': form, 'titulo': f'Editar Docente: {docente.nome}'})

def ucs(request):
    ucs = UnidadeCurricular.objects.all().order_by('ano', 'semestre')
    return render(request, 'unidades_curriculares.html', {'ucs': ucs})

def uc_detalhe(request, pk):
    uc = get_object_or_404(UnidadeCurricular, pk=pk)
    return render(request, 'unidade_curricular_detalhe.html', {'uc': uc})

@user_passes_test(is_staff)
def novo_uc(request):
    if request.method == "POST":
        form = UnidadeCurricularForm(request.POST, request.FILES)
        if form.is_valid():
            uc = form.save()
            return redirect('portefolio_app:uc_detail', pk=uc.pk)
    else:
        form = UnidadeCurricularForm()
    return render(request, 'generic_form.html', {'form': form, 'titulo': 'Nova Unidade Curricular'})

@user_passes_test(is_staff)
def edita_uc(request, pk):
    uc = get_object_or_404(UnidadeCurricular, pk=pk)
    if request.method == "POST":
        form = UnidadeCurricularForm(request.POST, request.FILES, instance=uc)
        if form.is_valid():
            uc = form.save()
            return redirect('portefolio_app:uc_detail', pk=uc.pk)
    else:
        form = UnidadeCurricularForm(instance=uc)
    return render(request, 'generic_form.html', {'form': form, 'titulo': f'Editar UC: {uc.nome}'})

def tfcs(request):
    tfcs = TFC.objects.all()
    return render(request, 'tfcs.html', {'tfcs': tfcs})

def tfc_detalhe(request, pk):
    tfc = get_object_or_404(TFC, pk=pk)
    return render(request, 'tfc_detalhe.html', {'tfc': tfc})

@user_passes_test(is_staff)
def novo_tfc(request):
    if request.method == "POST":
        form = TFCForm(request.POST, request.FILES)
        if form.is_valid():
            tfc = form.save()
            return redirect('portefolio_app:tfc_detail', pk=tfc.pk)
    else:
        form = TFCForm()
    return render(request, 'generic_form.html', {'form': form, 'titulo': 'Novo TFC'})

@user_passes_test(is_staff)
def edita_tfc(request, pk):
    tfc = get_object_or_404(TFC, pk=pk)
    if request.method == "POST":
        form = TFCForm(request.POST, request.FILES, instance=tfc)
        if form.is_valid():
            tfc = form.save()
            return redirect('portefolio_app:tfc_detail', pk=tfc.pk)
    else:
        form = TFCForm(instance=tfc)
    return render(request, 'generic_form.html', {'form': form, 'titulo': f'Editar TFC: {tfc.titulo}'})
