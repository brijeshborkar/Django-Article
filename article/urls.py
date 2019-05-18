from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('detail/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
    path('article/', views.ArticleCreateView.as_view(), name='article_new'),
    path('article/<int:pk>/edit', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article_delete'),

]
