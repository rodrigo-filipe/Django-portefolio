from django.db import models
from django.utils.timezone import now
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.PositiveIntegerField(default=260, unique=True)
    instituicao = models.CharField(max_length=200, default="Universidade Lusófona")
    descricao = models.TextField(blank=True)
    duracao_anos = models.PositiveIntegerField(default=3)
    data_inicio = models.DateField(default=datetime.date.today)
    lic_link = models.URLField(default="https://www.ulusofona.pt/lisboa/licenciaturas/engenharia-informatica")

    def __str__(self):
        return self.nome


class Docente(models.Model):
    nome = models.CharField(unique=True, max_length=150)
    email = models.EmailField(blank=True, null=True)
    pagina_pessoal = models.URLField(blank=True)
    foto = models.ImageField(upload_to='docentes/', blank=True, null=True)

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50, unique=True)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='ucs', default=260)
    ano = models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3)])
    semestre = models.PositiveIntegerField(choices=[(1, 1), (2, 2)])
    ects = models.PositiveIntegerField(default=6)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    docentes = models.ManyToManyField(Docente, related_name='ucs')

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class CategoriaTecnologia(models.Model):
    nome = models.CharField(max_length=100, unique=True) # Frontend, Backend, Base de Dados, Storage, Outros

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    site_oficial = models.URLField(blank=True)
    descricao = models.TextField(blank=True, help_text="O que esta tecnologia faz e permite")
    aspectos_positivos = models.TextField(blank=True, help_text="Aspetos que gostou")
    aspectos_negativos = models.TextField(blank=True, help_text="Aspetos que não gostou")
    nivel_interesse = models.PositiveIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    categoria_relacionada = models.ForeignKey(CategoriaTecnologia, on_delete=models.SET_NULL, null=True, blank=True, related_name='tecnologias')
    # Mantemos categoria como CharField por agora para não quebrar queries antigas até migração completa
    categoria = models.CharField(max_length=50, blank=True) 

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.TextField()
    objetivo = models.TextField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    video_demo = models.CharField(max_length=500, blank=True, help_text="Link para o vídeo de demonstração (ex: YouTube)")
    github = models.CharField(max_length=500, blank=True, help_text="Link para o repositório GitHub")

    def __str__(self):
        return self.titulo


class TFC(models.Model):
    titulo = models.CharField(max_length=300)
    alunos = models.CharField(max_length=300)
    orientador = models.CharField(max_length=200)
    ano = models.IntegerField(default=2025)
    licenciatura = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    descricao = models.TextField()
    palavras_chave = models.TextField()
    areas = models.TextField()
    tecnologias_usadas = models.TextField()
    pdf = models.FileField(upload_to='tfc/', blank=True, null=True)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.titulo


class Formacao(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    instituicao = models.CharField(max_length=150)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    certificado = models.FileField(upload_to='formacoes/', blank=True, null=True)

    class Meta:
        ordering = ['-data_inicio']

    def __str__(self):
        return f"{self.titulo} - {self.instituicao}"


class Competencia(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    descricao = models.TextField(blank=True)
    nivel = models.PositiveIntegerField(choices=[(1, 'Básico'), (2, 'Intermédio'), (3, 'Avançado')], default=2)
    projetos = models.ManyToManyField(Projeto, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)
    formacoes = models.ManyToManyField(Formacao, blank=True)

    def __str__(self):
        return self.nome


# === ENTIDADE OBRIGATÓRIA: MAKING OF ===
class MakingOf(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField(default=now)
    foto = models.ImageField(upload_to='makingof/', blank=True, null=True)
    entidade_relacionada = models.CharField(max_length=100)
    justificacao = models.TextField(blank=True)
    erro_correcao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.entidade_relacionada} - {self.titulo}"
