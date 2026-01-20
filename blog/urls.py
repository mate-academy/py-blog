from django.urls import path

from .views import PostListView, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/new_comment/",
        CommentaryCreateView.as_view(),
        name="comment_create",
    ),
]

app_name = "blog"
