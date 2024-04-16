from django.contrib.auth import login, logout
from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
)

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
