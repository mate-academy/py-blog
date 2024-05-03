from django.urls import path

from blog.views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    MyPostListView,
    PostDetailView,
    PostDeleteView,
    CommentCreateView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/create", PostCreateView.as_view(), name="post-create"),
    path(
        "posts/<int:pk>/update",
        PostUpdateView.as_view(),
        name="post-update"
    ),
    path("my-post", MyPostListView.as_view(), name="my-post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/delete",
        PostDeleteView.as_view(),
        name="post-delete"
    ),
    path(
        "posts/comment/create/",
        CommentCreateView.as_view(),
        name="comment-create"
    ),
]

app_name = "blog"
