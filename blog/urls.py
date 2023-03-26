from django.urls import path

from .views import (
    index,
    PostListView,
    PostDetailView,
    CommentaryListView,
    CommentaryDetailView,
)

urlpatterns = [

    path("", index, name="index"),
    path(
        "posts/",
        PostListView.as_view(),
        name="post-list",
    ),
    path(
        "posts/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail",
    ),
    path(
        "commentaries/",
        CommentaryListView.as_view(),
        name="commentary-list",
    ),
    path(
        "commentaries/<int:pk>/",
        CommentaryDetailView.as_view(),
        name="commentary-detail",
    ),
    ]

app_name = "blog"
