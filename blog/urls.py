from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    CommentaryCreateView,
    IndexView
)

app_name = "blog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "comment/create/",
        CommentaryCreateView.as_view(),
        name="comment-create"
    )

]
