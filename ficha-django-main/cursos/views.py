from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def curos_view(request):
    cursos = Curso.objects.all()

    context = {"cursos":cursos}

    return render(request, "cursos/cursos.html", context)

def aluno_view(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)

    context = {"alunos"}

    return render(request, "cursos/")

def novo_curso(request):

    form = CursoForm(request.POST or None)

    if request.POST:
        if forms.is_valid:
            form.save()
            return redirect("cursos")

    context = {"form":form}

    return render(request, "cursos/novo_curso.html", context)


def edita_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    form = CursoForm(request.POST or None, instance=curso)

    if request.POST:
        if forms.is_valid:
            form.save()
            return redirect("cursos")

    context = {"form":form}

    return render(request, "cursos/novo_curso.html", context)