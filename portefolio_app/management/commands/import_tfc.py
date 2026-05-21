import json
from django.core.management.base import BaseCommand
from portefolio_app.models import TFC


class Command(BaseCommand):
    help = 'Importa TFCs do ficheiro tfcs_2024_2025.json'

    def handle(self, *args, **options):
        json_path = 'tfcs_2024_2025.json'

        try:
            with open(json_path, encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'❌ Ficheiro não encontrado: {json_path}'))
            self.stdout.write(self.style.WARNING('Coloca o ficheiro tfcs_2024_2025.json na raiz do projeto (ao lado de manage.py)'))
            return
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('❌ Erro ao ler o JSON. Verifica se o ficheiro está bem formatado.'))
            return

        imported = 0
        skipped = 0

        for item in data:
            try:
                # Tratamento dos campos (alguns TFCs têm "ano" como string)
                ano = int(item.get('ano')) if item.get('ano') else 2025

                # rating vem como 6 ou 9, mas o teu modelo aceita no máximo 5 → vamos limitar
                rating = min(int(item.get('rating', 5)), 5)

                # palavras_chave, areas e tecnologias_usadas são listas → juntamos em texto
                palavras_chave = ", ".join(item.get('palavras_chave', []))
                areas = ", ".join(item.get('areas', []))
                tecnologias = ", ".join(item.get('tecnologias_usadas', []))

                tfc, created = TFC.objects.update_or_create(
                    titulo=item.get('titulo'),
                    defaults={
                        'alunos': item.get('alunos', ''),
                        'orientador': item.get('orientador', ''),
                        'ano': ano,
                        'licenciatura': item.get('licenciatura', 'Não especificado'),
                        'email': item.get('email', ''),
                        'descricao': item.get('resumo', ''),
                        'palavras_chave': palavras_chave,
                        'areas': areas,
                        'tecnologias_usadas': tecnologias,
                        'pdf': '',                    # link_pdf não usamos por agora
                        'rating': rating,
                    }
                )

                if created:
                    imported += 1
                    self.stdout.write(f"✅ Importado: {tfc.titulo[:60]}...")
                else:
                    self.stdout.write(f"🔄 Atualizada: {tfc.titulo[:60]}...")

            except Exception as e:
                skipped += 1
                self.stdout.write(self.style.WARNING(f"⚠️  Erro ao importar: {item.get('titulo', 'Sem título')} → {e}"))

        # Resumo final
        self.stdout.write(self.style.SUCCESS(f"\n🎉 Importação terminada!"))
        self.stdout.write(self.style.SUCCESS(f"   Novos TFCs importados: {imported}"))
        self.stdout.write(self.style.SUCCESS(f"   Atualizados: {len(data) - imported - skipped}"))
        if skipped:
            self.stdout.write(self.style.WARNING(f"   Ignorados com erro: {skipped}"))