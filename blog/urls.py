from django.urls import path

from blog.views import (
    PostDetailView,
    PostListView,
    add_comment_to_post,
    comment_remove,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/comment/", add_comment_to_post, name="add-comment-to-post"),
    path("comment/<int:pk>/remove/", comment_remove, name="comment-remove"),
]


app_name = "blog"
