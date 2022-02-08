from operator import index
from textwrap import indent
from django.urls import path
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
    path("travel/", views.travel, name="travel"),
    path("news_post/<int:n_id>", views.news_post, name="news_post"),
    path("banner1/", views.banner1, name="banner1"),
    path("banner1/", views.banner2, name="banner2"),
    path("banner1/", views.banner3, name="banner3"),
    path("banner4/", views.banner1, name="banner1"),
]