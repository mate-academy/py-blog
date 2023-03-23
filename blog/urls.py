from django.urls import path

from blog.views import (
    index,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentaryCreateView,
    )

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("createpost/", PostCreateView.as_view(), name="create-post"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="update-post"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="delete-post"),
    path("commentarycreate/", CommentaryCreateView.as_view(), name="create-comment")
]

app_name = "blog"
