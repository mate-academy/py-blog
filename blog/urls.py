from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
)

urlpatterns = [
    path(
        "",
        PostListView.as_view(),
        name="index"
    ),
    path(
        "post/create/",
        PostCreateView.as_view(),
        name="post-create"
    ),
    path(
        "post/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
]

app_name = "blog"
