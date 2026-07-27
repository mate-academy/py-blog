from django.urls import path

from blog.views import (
    index,
    PostDetailView,
    CommentaryCreateView,
    CommentaryDeleteView,
)

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/",
         PostDetailView.as_view(),
         name="post-detail"),
    path(
        "posts/<int:pk>/comment/",
        CommentaryCreateView.as_view(),
        name="comment-create",
    ),
    path(
        "comments/<int:pk>/delete/",
        CommentaryDeleteView.as_view(),
        name="comment-delete",
    ),
]
