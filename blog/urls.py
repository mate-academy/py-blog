from django.urls import path

from .views import (
    CommentaryCreateView,
    PostListView,
    PostDetailView,
    UserCreateView
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("comment/create/", CommentaryCreateView.as_view(), name="comment-create"),
    path("user/create/", UserCreateView.as_view(), name="user-create")
]

app_name = "blog"
