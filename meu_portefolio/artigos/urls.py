from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.ArtigoListView.as_view(), name='artigo_list'),
    path('<int:pk>/', views.ArtigoDetailView.as_view(), name='artigo_detail'),
    path('novo/', views.ArtigoCreateView.as_view(), name='artigo_create'),
    path('<int:pk>/editar/', views.ArtigoUpdateView.as_view(), name='artigo_update'),
    path('<int:pk>/like/', views.like_artigo, name='like_artigo'),
    path('<int:pk>/comentar/', views.add_comment, name='add_comment'),
    path('<int:pk>/votar/', views.rate_artigo, name='rate_artigo'),
]
