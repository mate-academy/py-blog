from django.urls import path, include

from .views import (
    PostListView, PostDetailView, SignUpView, CommentaryCreateView,
    PostCreateView, PostUpdateView, PostDeleteView,
    MyPostsListView, about_view
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("my-posts/", MyPostsListView.as_view(), name="my-posts"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/update", PostUpdateView.as_view(), name="post-update"
    ),
    path(
        "posts/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"
    ),
    path(
        "posts/<int:pk>/post-comment",
        CommentaryCreateView.as_view(), name="commentary-create"
    ),
    path("posts/create", PostCreateView.as_view(), name="post-create"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/sign-up/", SignUpView.as_view(), name="sign-up"),
    path("about/", about_view, name="about")
]

app_name = "blog"
