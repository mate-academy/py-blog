from django.urls import path

from .views import (
    index,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserListView,
    UserDetailView,
    CommentaryListView,
    CommentaryDetailView,
    CommentaryCreateView,
    CommentaryUpdateView,
    CommentaryDeleteView,
)

urlpatterns = [

    path("", index, name="index"),
    path(
        "posts/",
        PostListView.as_view(),
        name="post-list",
    ),
    path(
        "posts/create/",
        PostCreateView.as_view(),
        name="post-create",
    ),
    path(
        "posts/<int:pk>/update/",
        PostUpdateView.as_view(),
        name="post-update",
    ),
    path(
        "posts/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail",
    ),
    path(
        "posts/<int:pk>/delete/",
        PostDeleteView.as_view(),
        name="post-delete",
    ),
    path(
        "users/",
        UserListView.as_view(),
        name="user-list",
    ),
    path(
        "user/<int:pk>/",
        UserDetailView.as_view(),
        name="user-detail",
    ),
    path(
        "commentaries/",
        CommentaryListView.as_view(),
        name="commentary-list",
    ),
    path(
        "commentaries/create/",
        CommentaryCreateView.as_view(),
        name="commentary-create",
    ),
    path(
        "commentaries/<int:pk>/update/",
        CommentaryUpdateView.as_view(),
        name="commentary-update",
    ),
    path(
        "commentaries/<int:pk>/",
        CommentaryDetailView.as_view(),
        name="commentary-detail",
    ),
    path(
        "commentaries/<int:pk>/delete/",
        CommentaryDeleteView.as_view(),
        name="commentary-delete",
    ),
    ]

app_name = "blog"
