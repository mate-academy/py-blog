from blog.views import PostListView, PostDetailView, CommentaryCreateView
from django.urls import path


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/comment/",
        CommentaryCreateView.as_view(),
        name="post-comment"
    ),
]

app_name = "blog"
