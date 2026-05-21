from django.db import models
from django.contrib.auth.models import User

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fotografia = models.ImageField(upload_to='artigos/', blank=True, null=True)
    link_externo = models.URLField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artigos')
    likes = models.ManyToManyField(User, related_name='artigos_curtidos', blank=True)
    likes_anonimos = models.PositiveIntegerField(default=0)

    def total_likes(self):
        return self.likes.count() + self.likes_anonimos

    def average_rating(self):
        ratings = self.ratings.all()
        if not ratings:
            return 0
        return sum(r.valor for r in ratings) / ratings.count()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.autor.username} em {self.artigo.titulo}'

class Rating(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='ratings')
    valor = models.IntegerField(default=0) # 1 to 5
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        unique_together = ('artigo', 'user', 'session_key')

