from django.urls import path
from .views import ArticleListView, ArticleDetailView
from . import views

urlpatterns = [
    path("parser/", views.parser),
    path("", ArticleListView.as_view(), name="article_list"),
    path("<slug:slug>", ArticleDetailView.as_view(), name="article_detail"),
]