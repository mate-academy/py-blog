from django.urls import path, include

from blog.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    CommentaryCreateView,
)


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("post/create", PostCreateView.as_view(), name="post-create"),
    path(
        "post/<int:pk>/comment/",
        CommentaryCreateView.as_view(),
        name="post-add-comment",
    ),
]

app_name = "blog"
