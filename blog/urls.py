from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    CommentaryCreateView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/comment/",
        CommentaryCreateView.as_view(),
        name="comment-create"
    ),
    path("posts/<int:pk>/comment/", CommentaryCreateView.as_view(),
         name="comment-create"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
]
