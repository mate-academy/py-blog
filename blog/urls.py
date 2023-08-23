from django.urls import path

from blog.views import (
    index,
    CommentaryCreateView,
    CommentaryUpdateView,
    CommentaryDeleteView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,

)

urlpatterns = [
    path("", index, name="index"),
    path(
        "posts/",
        PostListView.as_view(),
        name="post-list"
    ),
    path(
        "posts/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
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
    path(
        "commentary/create/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
    path(
        "commentary/<int:pk>/update/",
        CommentaryUpdateView.as_view(),
        name="commentary-update"
    ),
    path(
        "commentary/<int:pk>/delete/",
        CommentaryDeleteView.as_view(),
        name="commentary-delete"
    ),
]

app_name = "blog"
