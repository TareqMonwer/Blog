from django.contrib import admin

from .models import Article, Like


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
