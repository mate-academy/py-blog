from django.urls import path

from .views import PostListView, PostDetailView, profile_view, RegisterView
from .models import Post, User, Commentary

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("profile/", profile_view, name="profile"),
    path("register/", RegisterView.as_view(), name="register"),
]
