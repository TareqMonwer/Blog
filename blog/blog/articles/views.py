from django.http import Http404
from django.shortcuts import redirect
from django.views import View
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView)

from braces.views import LoginRequiredMixin

from .models import Article, Like
from .mixins import AuthorArticleEditMixin


class ArticleList(ListView):
    """
    Returns a list of published articles.
    """
    model = Article
    paginate_by = 10
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_article = Article.published.latest()
        context['last_article'] = last_article
        return context

    def get_queryset(self):
        qs = Article.published.select_related('author').select_related().all()
        return qs


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/detail.html'

    def get_object(self, qs=None):
        obj = super().get_object(queryset=qs)
        # If user is not the author of article
        if obj.status == 'draft' and obj.author != self.request.user:
            raise Http404()
        return obj

    def get_context_data(self, **kwargs):
        obj = super().get_object()
        context = super().get_context_data(**kwargs)
        likes = Like.objects.filter(article=obj)
        context['likes'] = likes
        return context


class ArticleCreate(AuthorArticleEditMixin, CreateView):
    model = Article
    fields = ['title', 'content', 'featured_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdate(AuthorArticleEditMixin, UpdateView):
    model = Article
    fields = ['title', 'content', 'featured_image']


class ArticleLike(View):
    def post(self, request, slug):
        user = request.user
        article = Article.objects.get(slug=slug)
        Like.objects.create(user=user, article=article)
        return redirect(article.get_absolute_url())
