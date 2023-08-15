from django.urls import path

from blog.views import (
    IndexView,
    PostListView,
    add_comment,
    PostDetailView,
    PostCreateView,
    UserListView,
    UserCreateView,
    CommentaryListView,
    CommentaryDetailView,
    CommentaryCreateView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path(
        "commentaries/",
        CommentaryListView.as_view(),
        name="commentary-list"
    ),
    path(
        "commentaries/create/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
    path(
        "commentaries/<int:pk>/",
        CommentaryDetailView.as_view(),
        name="commentary-detail",
    ),
    path("add_comment/<int:pk>/", add_comment, name="add-comment"),
]

app_name = "blog"
