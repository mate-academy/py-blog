from django.urls import path

from .views import (
    PostListView, PostDetailView, CommentCreateView,
)

urlpatterns = [
    path("posts/", PostListView.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/comment/create/",
        CommentCreateView.as_view(),
        name="comment-create"
    ),
]

app_name = "blog"
