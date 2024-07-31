from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    CommentaryCreateView,
    UserDetailView,
    UserUpdateView
)

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/comment",
        CommentaryCreateView.as_view(),
        name="comment-create"
    ),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("user/<int:pk>/edit/", UserUpdateView.as_view(), name="user-update"),
]
