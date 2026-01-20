from django.urls import path
from .views import PostDetailView, CommentaryCreateView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("create/", CommentaryCreateView.as_view(), name="comment-create"),
]

app_name = "blog"
