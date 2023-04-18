from django.urls import path

from blog.forms import CommentaryForm
from blog.views import PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/comment/", CommentaryForm, name="post-comment"),
]

app_name = "blog"
