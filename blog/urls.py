from django.urls import path

from blog.views import (
    index,
    PostDetailView,
    CommentCreateView,
    PostListView,
    UserCreateView,
    UserListView,
)


urlpatterns = [
    path(
        "",
        PostListView.as_view(),
        name="index"),
    # path("post-list/", PostListView.as_view(), name="post-list"),
    path(
        "post/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"),
    path(
        "post/<int:pk>/comment/",
        CommentCreateView.as_view(),
        name="comment-create"),
    path(
        "user-create/",
        UserCreateView.as_view(),
        name="user-create"),
    path(
        "user-list/",
        UserListView.as_view(),
        name="user-list"
    ),
]

app_name = "blog"
