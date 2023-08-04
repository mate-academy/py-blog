from django.contrib import admin
from django.urls import path

from blog.views import PostListView, commentary_create_view


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", commentary_create_view, name="post-detail"),
]

app_name = "blog"
