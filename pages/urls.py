from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('articles/', ArticleListView, name='article'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/edit/<int:pk>', ArticleEditView.as_view(), name='article_edit'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/delete/<int:pk>', ArticleDeleteView.as_view(), name='article_delete'),
    path('like/<int:pk>', LikeView, name='like_post'),
]