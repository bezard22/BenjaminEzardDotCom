from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<str:article>', views.article, name='article'),
    path('articleAPI/<str:article>', views.articleAPI, name='articleAPI'),
]