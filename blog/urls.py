from django.contrib.auth import login, logout
from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    CommentaryCreateView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/",
         CommentaryCreateView.as_view(),
         name="commentary-create"
         ),
    path("login/", login),
    path("logout/", logout),
]

app_name = "blog"
