import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portefolio.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from portefolio_app.models import Projeto, Tecnologia, UnidadeCurricular, Docente, Formacao, Competencia, MakingOf

def setup_groups():
    group, created = Group.objects.get_or_create(name='gestor-portfolio')
    
    models = [Projeto, Tecnologia, UnidadeCurricular, Docente, Formacao, Competencia, MakingOf]
    
    for model in models:
        content_type = ContentType.objects.get_for_model(model)
        permissions = Permission.objects.filter(content_type=content_type)
        for perm in permissions:
            group.permissions.add(perm)
            
    print("Group 'gestor-portfolio' created/updated with permissions.")

if __name__ == "__main__":
    setup_groups()
