from django.urls import path

from .views import (
    IndexView,
    PostDetailView,
    CommentaryUpdateView,
    CommentaryDeleteView
)


app_name = "blog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "comments/<int:pk>/update/",
        CommentaryUpdateView.as_view(),
        name="comment-update",
    ),
    path(
        "comments/<int:pk>/delete/",
        CommentaryDeleteView.as_view(),
        name="comment-delete",
    ),
]
