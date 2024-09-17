from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    UserDetailView,
)

urlpatterns = [
    path(
        "",
        PostListView.as_view(),
        name="index"
    ),
    path(
        "posts/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "users/<int:pk>/",
        UserDetailView.as_view(),
        name="user-detail"
    )
]

app_name = "blog"
