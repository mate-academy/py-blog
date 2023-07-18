from django.urls import path

from blog.views import Index, PostDetailView, CommentCreateView


urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create_comment",
        CommentCreateView.as_view(),
        name="post-create-comment"
    ),
]

app_name = "blog"
