from django.contrib import admin
from django.urls import path, include

from blog.views import PostListView, PostDetailView, create_comment_view

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/comment", create_comment_view, name="create-comment"),
]

app_name = "blog"
