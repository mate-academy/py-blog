from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, CreateCommentView


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/create_comment/",
        CreateCommentView.as_view(),
        name="create-comment",
    ),
]

app_name = "blog"
