from django.urls import path
from . import views

app_name = 'portefolio_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.projetos, name='projects'),
    path('tecnologias/', views.tecnologias, name='technologies'),
    path('tecnologia/<int:pk>/', views.tecnologia_detalhe, name='technology_detail'),
    path('contacto/', views.contacto, name='contact'),
    path('faculdade/', views.faculdade, name='faculdade'),
    path('docentes/', views.docentes, name='docentes'),
    path('docente/<int:pk>/', views.docente_detalhe, name='docente_detail'),
    path('ucs/', views.ucs, name='ucs'),
    path('uc/<int:pk>/', views.uc_detalhe, name='uc_detail'),
]