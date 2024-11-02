from django.urls import path
from blog.views import PostDetailView, CommentCreateView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("comments/create/", CommentCreateView.as_view(), name="comment-create"),
]

app_name = "blog"
