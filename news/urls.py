from operator import index
from textwrap import indent
from django.urls import path
from . import views
from .views import *



urlpatterns = [
    path('', views.index, name="index"),
    path("author/", views.author, name="author"),
    path("author/<int:p_id>", views.author, name="author"),
    path("politics/", views.politics, name="politics"),
    path("economy/", views.economy, name="economy"),
    path("society/", views.society, name="society"),
    path("life/", views.life, name="life"),
    path("IT/", views.IT, name="IT"),
    path("world/", views.world, name="world"),
    path("memberinfo/", views.memberinfo, name="memberinfo"),
    path("news_post/<int:n_id>", views.news_post, name="news_post"),
    path("memberinfo/", views.memberinfo, name="memberinfo"),
    path('recommend/', views.recommend, name='recommend'),
]

