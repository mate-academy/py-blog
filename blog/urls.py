from django.urls import path

from blog.views import (
    PostListView,
    UserListView,
    PostDetailView,
    CommentaryCreateView
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("users/", UserListView.as_view(), name="user-list"),
    path(
        "posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"
    ),
    path(
        "posts/<int:pk>/add_comment/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
]

app_name = "blog"
