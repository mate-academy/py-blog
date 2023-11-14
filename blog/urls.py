from django.urls import path
from .views import Index, PostDetailView, CommentCreateView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/comment/create",
        CommentCreateView.as_view(),
        name="comment-create"
    ),
]

app_name = "blog"
