from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    CommentaryCreateView,
    CommentaryDeleteView,
    CommentaryUpdateView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/comment/", CommentaryCreateView.as_view(), name="comment-create"),
    path("post/<int:post_pk>/comment/<int:pk>/delete/", CommentaryDeleteView.as_view(), name="comment-delete"),
    path("post/<int:post_pk>/comment/<int:pk>/update/", CommentaryUpdateView.as_view(), name="comment-update"),
]
