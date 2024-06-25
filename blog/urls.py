from django.urls import path
from .views import IndexView, PostDetailView, CommentCreateView


app_name = "blog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "posts/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "posts/<int:pk>/create/",
        CommentCreateView.as_view(),
        name="comment-create"
    ),
]
