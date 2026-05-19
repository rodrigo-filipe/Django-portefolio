from django.contrib import admin
from .models import (
    Licenciatura, Docente, UnidadeCurricular, Tecnologia, CategoriaTecnologia,
    Projeto, TFC, Competencia, Formacao, MakingOf
)


# ====================== REGISTO DOS MODELOS ======================

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'codigo', 'duracao_anos']
    search_fields = ['nome', 'codigo']
    ordering = ['nome']


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'pagina_pessoal']
    search_fields = ['nome', 'email']
    ordering = ['nome']


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'ano', 'semestre', 'ects', 'get_docentes_count']
    list_filter = ['ano', 'semestre', 'licenciatura']
    search_fields = ['nome', 'codigo']
    filter_horizontal = ['docentes']
    ordering = ['ano', 'semestre', 'nome']

    def get_docentes_count(self, obj):
        return obj.docentes.count()
    get_docentes_count.short_description = 'Nº de Docentes'


@admin.register(CategoriaTecnologia)
class CategoriaTecnologiaAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria_relacionada', 'nivel_interesse']
    list_filter = ['categoria_relacionada']
    search_fields = ['nome']
    ordering = ['categoria_relacionada', 'nome']


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'unidade_curricular', 'descricao']   # campos que realmente existem
    list_filter = ['unidade_curricular']
    search_fields = ['titulo']
    filter_horizontal = ['tecnologias']
    ordering = ['titulo']


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'alunos', 'orientador', 'ano', 'rating']
    list_filter = ['ano', 'licenciatura']
    search_fields = ['titulo', 'alunos', 'orientador']
    ordering = ['-ano']


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nivel']
    search_fields = ['nome']
    filter_horizontal = ['projetos', 'tecnologias', 'formacoes']
    ordering = ['nome']


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'instituicao', 'data_inicio', 'data_fim']
    list_filter = ['instituicao']
    search_fields = ['titulo']
    date_hierarchy = 'data_inicio'
    ordering = ['-data_inicio']


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ['entidade_relacionada', 'titulo', 'data']
    list_filter = ['entidade_relacionada', 'data']
    search_fields = ['titulo']
    date_hierarchy = 'data'
    ordering = ['-data']