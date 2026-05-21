import os
import django
from django.core.files import File

# Configuração do ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portefolio.settings')
django.setup()

from portefolio_app.models import Projeto, Tecnologia, Docente, UnidadeCurricular, TFC, Formacao, MakingOf
from artigos.models import Artigo

def migrate_images(model_class, image_field_name):
    print(f"\n--- Migrando {model_class.__name__} (campo: {image_field_name}) ---")
    from django.conf import settings
    for obj in model_class.objects.all():
        field = getattr(obj, image_field_name)
        if field and field.name:
            try:
                # Construímos o caminho local manualmente usando o MEDIA_ROOT
                # já que o field.path falha quando o Cloudinary está ativo
                local_path = os.path.join(settings.MEDIA_ROOT, field.name)
                
                if os.path.exists(local_path):
                    with open(local_path, 'rb') as f:
                        # O Django vai enviar para o Cloudinary porque é o storage padrão
                        field.save(
                            os.path.basename(local_path),
                            File(f),
                            save=True
                        )
                    print(f"Sucesso: {obj}")
                else:
                    print(f"Aviso: Ficheiro não encontrado localmente em {local_path} para {obj}")
            except Exception as e:
                print(f"Erro ao migrar {obj}: {e}")

# Lista de migrações a executar: (Modelo, Nome_do_Campo)
migrations = [
    (Projeto, 'imagem'),
    (Tecnologia, 'logo'),
    (Docente, 'foto'),
    (UnidadeCurricular, 'imagem'),
    (Artigo, 'fotografia'),
    (MakingOf, 'foto'),
    (TFC, 'pdf'),           
    (Formacao, 'certificado') 
]

if __name__ == "__main__":
    print("Iniciando migração de media...")
    for model, field in migrations:
        migrate_images(model, field)
    print("\nMigração terminada!")
