from django.urls import path
from blog.views import (
    index,
    PostDetailView,
    CommentDeleteView
)


app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "comment/delete/<int:pk>/",
        CommentDeleteView.as_view(),
        name="comment-delete"
    ),
]
