from django.urls import path
from . import views

app_name = 'portefolio_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos', views.projetos, name='projects'),
    path('tecnologias', views.tecnologias, name='technologies'),
    path('contacto', views.contacto, name='contact'),
]