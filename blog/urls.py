from django.urls import path

from blog.models import Commentary
from blog.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentaryCreateView,
)

urlpatterns = [
    path("blog/create/", PostCreateView.as_view(), name="post-create"),
    path("blog/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("blog/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("", PostListView.as_view(), name="index"),
    path("blog/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("blog/<int:pk>/create_comment", CommentaryCreateView.as_view(), name="comment-create"),

]

app_name = "blog"