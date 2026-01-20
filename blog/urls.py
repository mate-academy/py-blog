from django.urls import path, include

from blog.views import PostListView, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/new_comment/",
        CommentaryCreateView.as_view(),
        name="new-comment",
    ),
]

app_name = "blog"
