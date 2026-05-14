from django.urls import path
from . import views

app_name = 'portefolio_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos', views.projetos, name='projects'),
    path('tecnologias', views.tecnologias, name='technologies'),
    path('tecnologia/<int:pk>/', views.tecnologia_detalhe, name='technology_detail'),
    path('contacto', views.contacto, name='contact'),
    path('faculdade', views.faculdade, name='faculdade'),
]