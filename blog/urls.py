from django.urls import path

from .views import (
    PostDetailView,
    PostListView, CommentCreateView
)

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/comment-create/",
        CommentCreateView.as_view(),
        name="comment-create"
    ),
]
