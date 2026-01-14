import profile

from django.urls import path

from blog.views import (
    index,
    UserDetailView,
    UserUpdateView,
    PostListView,
    PostDetailView,
    CommentaryCreateView,
    CommentaryDeleteView,
    PostCreateView,
    PostDeleteView
)

app_name = "blog"
urlpatterns = [
    path("", index, name="index"),
    path(
        "profile/<int:pk>",
        UserDetailView.as_view(),
        name="profile"
    ),
    path(
        "profile/<int:pk>/update",
        UserUpdateView.as_view(),
        name="update"
    ),
    path(
        "posts/",
        PostListView.as_view(),
        name="post-list"
    ),
    path(
        "posts/<int:pk>",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "posts/create/",
        PostCreateView.as_view(),
        name="post-create"
    ),
    path(
        "posts/<int:pk>/delete",
        PostDeleteView.as_view(),
        name="post-delete"
    ),
    path(
        "posts/<int:pk>/create_commentary/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
    path(
        "posts/<int:pk>/delete_commentary/",
        CommentaryDeleteView.as_view(),
        name="commentary-delete"
    ),
]
