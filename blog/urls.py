from django.urls import path
from django.views.generic import ListView

from blog.models import Post, User, Commentary
from blog.views import (
    PostListView,
    PostDetailView
)

urlpatterns = [
    path("posts/", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail")
]

app_name = "blog"
