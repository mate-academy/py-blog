from django.urls import path
from blog.views import (
    PostDetailView,
    PostListView,
    CommentDeleteView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "comments/delete/<int:pk>/",
        CommentDeleteView.as_view(),
        name="comment-delete"
    ),
]

app_name = "blog"
