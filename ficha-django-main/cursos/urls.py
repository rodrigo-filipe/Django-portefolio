from . import views
from django import path

urlpatterns = [
    path("aluno/<int: aluno_id>", views.aluno_view, name = "aluno"),
    path("novo-curso", views.novo_curso, name = "novo-curso"),
    path("edita-curso/<int:curso_id>", views.edita_curso, name = "edita-curso"),
]