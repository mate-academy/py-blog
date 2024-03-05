from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentaryListView,
    CommentaryCreateView,
    CommentaryUpdateView,
    CommentaryDeleteView,
)

app_name = "blog"

url_posts = [
    path("", PostListView.as_view(), name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/user/<int:user_pk>/",
        UserPostListView.as_view(),
        name="user-post-list"
    ),
    path(
        "posts/create/",
        PostCreateView.as_view(),
        name="post-create"
    ),
    path(
        "posts/<int:pk>/update/",
        PostUpdateView.as_view(),
        name="post-update"
    ),
    path(
        "posts/<int:pk>/delete/",
        PostDeleteView.as_view(),
        name="post-delete"
    ),
]

url_comments = [
    path(
        "posts/<int:pk>/comments/",
        CommentaryListView.as_view(),
        name="comment-list"
    ),
    path(
        "posts/<int:pk>/comments/create/",
        CommentaryCreateView.as_view(),
        name="comment-create",
    ),
    path(
        "posts/comments/<int:pk>/update/",
        CommentaryUpdateView.as_view(),
        name="comment-update",
    ),
    path(
        "post/comments/<int:pk>/delete/",
        CommentaryDeleteView.as_view(),
        name="comment-delete",
    ),
]

urlpatterns = url_posts + url_comments
