from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    CommentaryCreateView,
    CommentaryDeleteView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "comments/create/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
    path(
        "comments/<int:pk>/delete/",
        CommentaryDeleteView.as_view(),
        name="commentary-delete",
    ),
]

app_name = "blog"
