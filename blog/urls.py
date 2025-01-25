from django.contrib import admin
from django.urls import path, include

from .views import IndexView, PostDetailView, CommentCreateView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/add-comment/", CommentCreateView.as_view(), name="comment-create"
    ),
]

app_name = "blog"
