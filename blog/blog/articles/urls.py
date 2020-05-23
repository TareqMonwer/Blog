from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('',
         views.ArticleList.as_view(),
         name='home'
    ),
    path('<slug:slug>/',
         views.ArticleDetail.as_view(),
         name='detail'
    ),
]
