import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings

from portefolio_app.models import (
    UnidadeCurricular,
    Licenciatura
)


class Command(BaseCommand):
    help = "Importar UCs a partir dos ficheiros JSON na pasta /files"

    def handle(self, *args, **kwargs):
        self.import_ucs_from_files()
        self.stdout.write(self.style.SUCCESS("Importação concluída!"))


    def import_ucs_from_files(self):
        folder = os.path.join(settings.BASE_DIR, 'files')

        # garantir que existe uma licenciatura
        licenciatura, _ = Licenciatura.objects.get_or_create(
            codigo="260",
            defaults={"nome": "Engenharia Informática"}
        )

        for filename in os.listdir(folder):
            if not filename.endswith('.json'):
                continue

            path = os.path.join(folder, filename)

            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.stdout.write(f"A importar: {filename}")

            # --- EXTRAÇÃO FLEXÍVEL ---
            nome = data.get('curricularUnitName') or data.get('nome') or "Sem nome"

            # código baseado no ficheiro
            codigo = filename.replace('.json', '')

            # valores default (ajusta depois se quiseres)
            ano = data.get('curricularYear')
            semestre = 1
            ects = data.get('ects', 6)

            # --- CRIAR OU ATUALIZAR ---
            uc, created = UnidadeCurricular.objects.update_or_create(
                codigo=codigo,
                defaults={
                    'nome': nome,
                    'licenciatura': licenciatura,
                    'ano': ano,
                    'semestre': semestre,
                    'ects': ects,
                    'descricao': data.get('presentation', '')
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"✔ Criado: {nome}"))
            else:
                self.stdout.write(self.style.WARNING(f"↺ Atualizado: {nome}"))