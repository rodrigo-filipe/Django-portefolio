from django.urls import path
from . import views

app_name = 'portefolio_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='about'),
    
    path('projetos/', views.projetos, name='projects'),
    path('projeto/<int:pk>/', views.projeto_detalhe, name='project_detail'),
    path('projeto/novo/', views.novo_projeto, name='novo_projeto'),
    path('projeto/<int:pk>/editar/', views.edita_projeto, name='edita_projeto'),

    path('tecnologias/', views.tecnologias, name='technologies'),
    path('tecnologia/<int:pk>/', views.tecnologia_detalhe, name='technology_detail'),
    path('tecnologia/nova/', views.novo_tecnologia, name='nova_tecnologia'),
    path('tecnologia/<int:pk>/editar/', views.edita_tecnologia, name='edita_tecnologia'),

    path('contacto/', views.contacto, name='contact'),
    path('faculdade/', views.faculdade, name='faculdade'),

    path('docentes/', views.docentes, name='docentes'),
    path('docente/<int:pk>/', views.docente_detalhe, name='docente_detail'),
    path('docente/novo/', views.novo_docente, name='novo_docente'),
    path('docente/<int:pk>/editar/', views.edita_docente, name='edita_docente'),

    path('ucs/', views.ucs, name='ucs'),
    path('uc/<int:pk>/', views.uc_detalhe, name='uc_detail'),
    path('uc/nova/', views.novo_uc, name='novo_uc'),
    path('uc/<int:pk>/editar/', views.edita_uc, name='edita_uc'),

    path('tfcs/', views.tfcs, name='tfcs'),
    path('tfc/<int:pk>/', views.tfc_detalhe, name='tfc_detail'),
    path('tfc/novo/', views.novo_tfc, name='novo_tfc'),
    path('tfc/<int:pk>/editar/', views.edita_tfc, name='edita_tfc'),
]