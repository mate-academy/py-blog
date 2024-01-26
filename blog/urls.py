from django.urls import path

from .views import (
    PostListView,
    PostCreateView,
    UserDetailView,
    PostDetailView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path(
        "post/<int:pk>/detail/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "user/<int:pk>/detail/",
        UserDetailView.as_view(),
        name="user-detail"
    )
]

app_name = "blog"
