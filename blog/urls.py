from blog.views import PostListView, PostDetailView, CommentCreateView
from django.urls import path

urlpatterns = [
    path("index/", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/comment/",
        CommentCreateView.as_view(),
        name="post-comment"
    ),
]

app_name = "blog"
