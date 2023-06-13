from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    CommentaryCreateView
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create_comment/",
        CommentaryCreateView.as_view(),
        name="create-comment",
    )
]

app_name = "blog"
