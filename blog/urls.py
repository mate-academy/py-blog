from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    CommentaryCreateView
)

urlpatterns = [
    path("blog/", PostListView.as_view(), name="index"),
    path(
        "blog/post/<int:pk>",
        PostDetailView.as_view(),
        name="post-detail"),
    path(
        "create/comment/<int:pk>",
        CommentaryCreateView.as_view(),
        name="commentary-create")
]

app_name = "blog"
