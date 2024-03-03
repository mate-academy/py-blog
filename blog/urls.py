from django.urls import path
from .views import (
    index,
    PostDetailView,
    CreateCommentView,
    UpdateCommentView,
    DeleteCommentView,
)

app_name = "blog"


urlpatterns = [
    path("", index, name="index"),
    path("blog/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "blog/<int:pk>/comment/create/",
        CreateCommentView.as_view(),
        name="comment-create",
    ),
    path(
        "blog/comment/<int:comment_pk>/update/",
        UpdateCommentView.as_view(),
        name="comment-update",
    ),
    path(
        "blog/comment/<int:comment_pk>/delete/",
        DeleteCommentView.as_view(),
        name="comment-delete",
    ),
]
