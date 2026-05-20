from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Artigo, Comentario, Rating
from .forms import ArtigoForm, ComentarioForm

class ArtigoListView(ListView):
    model = Artigo
    template_name = 'artigos/artigo_list.html'
    context_object_name = 'artigos'
    ordering = ['-data_criacao']

class ArtigoDetailView(DetailView):
    model = Artigo
    template_name = 'artigos/artigo_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = ComentarioForm()
        
        # Get current user/session rating
        user_rating = None
        if self.request.user.is_authenticated:
            user_rating = Rating.objects.filter(artigo=self.object, user=self.request.user).first()
        else:
            session_key = self.request.session.session_key
            if session_key:
                user_rating = Rating.objects.filter(artigo=self.object, session_key=session_key).first()
        
        context['user_rating'] = user_rating.valor if user_rating else 0
        return context

class ArtigoCreateView(LoginRequiredMixin, CreateView):
    model = Artigo
    form_class = ArtigoForm
    template_name = 'artigos/artigo_form.html'
    success_url = reverse_lazy('artigos:artigo_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ArtigoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Artigo
    form_class = ArtigoForm
    template_name = 'artigos/artigo_form.html'
    success_url = reverse_lazy('artigos:artigo_list')

    def test_func(self):
        artigo = self.get_object()
        return self.request.user == artigo.autor

@login_required
def like_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if artigo.likes.filter(id=request.user.id).exists():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)
    return HttpResponseRedirect(reverse('artigos:artigo_detail', args=[str(pk)]))

def add_comment(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == 'POST' and request.user.is_authenticated:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
    return redirect('artigos:artigo_detail', pk=pk)

def rate_artigo(request, pk):
    if request.method == 'POST':
        artigo = get_object_or_404(Artigo, pk=pk)
        valor = int(request.POST.get('valor', 0))
        if 1 <= valor <= 5:
            if request.user.is_authenticated:
                Rating.objects.update_or_create(
                    artigo=artigo, user=request.user,
                    defaults={'valor': valor}
                )
            else:
                if not request.session.session_key:
                    request.session.create()
                session_key = request.session.session_key
                Rating.objects.update_or_create(
                    artigo=artigo, session_key=session_key, user=None,
                    defaults={'valor': valor}
                )
    return redirect('artigos:artigo_detail', pk=pk)
