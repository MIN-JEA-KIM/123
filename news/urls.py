from operator import index
from textwrap import indent
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path("author/", views.author, name="author"),
    path("politics/", views.politics, name="politics"),
    path("economy/", views.economy, name="economy"),
    path("society/", views.society, name="society"),
    path("life/", views.life, name="life"),
    path("IT/", views.IT, name="IT"),
    path("world/", views.world, name="world"),
    path("news_post/<int:n_id>", views.news_post, name="news_post"),
    path("memberinfo/", views.memberinfo, name="memberinfo"),
]

