from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length=50)

    def str(self):
        return


class Aluno(models.Model):
    nome = models.CharField(max_length=50)


    def str(self):
        return




class Curso(models.Model):
    nome = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="cursos")
    alunos = models.ManyToMany(Aluno, related_name="cursos")

    def str(self):
        return self.nome