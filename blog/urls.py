from django.urls.conf import path
from blog.views import (
    index,
    PostListView,
    PostDetailView,
    my_posts_view,
    CommentaryCreateView
)

urlpatterns = [
    path("", index, name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("my-posts/", my_posts_view, name="my-posts-view"),
    # path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "post/<int:pk>/comment/",
        CommentaryCreateView.as_view(),
        name="comment-create"
    ),
]

app_name = "blog"
