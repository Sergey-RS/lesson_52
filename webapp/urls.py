from django.contrib import admin
from django.urls import path
from webapp.views import ArticleView, ArticleDetailView, ArticleCreateView, article_update_view, article_delete_view

urlpatterns =[
    path('', ArticleView.as_view(), name='article_list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/update/', article_update_view, name='article_update'),
    path('article/<int:pk>/delete/', article_delete_view, name='article_delete')
]