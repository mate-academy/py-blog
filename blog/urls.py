from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    CommentCreateView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/add_comment/",
        CommentCreateView.as_view(),
        name="comment-create"
    ),
]
app_name = "blog"
