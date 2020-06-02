from django.views.generic import ListView, DetailView

from .models import Article, Like


class ArticleList(ListView):
    model = Article
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_article = Article.published.first()
        context['last_article'] = last_article
        return context

    def get_queryset(self):
        qs = Article.published.all()
        return qs


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/detail.html'

    def get_context_data(self, **kwargs):
        obj = super().get_object()
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        likes = Like.objects.filter(article=obj)
        context['likes'] = likes
        return context
