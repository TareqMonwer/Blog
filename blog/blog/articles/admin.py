from django.contrib import admin

from .models import Article, Like


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    # TODO: Display obj __str__ representation in list display.
    list_display = ['__str__', 'created']
