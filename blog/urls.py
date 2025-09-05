from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView)

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/comment/create/",
        CommentCreateView.as_view(),
        name="comment-create"
    ),
    path(
        "comment/<int:pk>/update/",
        CommentUpdateView.as_view(),
        name="comment-update"
    ),
    path(
        "comment/<int:pk>/delete/",
        CommentDeleteView.as_view(),
        name="comment-delete")
]
