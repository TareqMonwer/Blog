from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Article


class ArticleList(ListView):
  model = Article
  template_name = 'pages/index.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    last_article = Article.objects.last()
    context['last_article'] = last_article
    return context
    

class ArticleDetail(DetailView):
  model = Article
  template_name = 'articles/detail.html'