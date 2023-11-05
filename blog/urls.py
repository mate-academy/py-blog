from django.urls import path
from .views import (
    index,
    PostDetailView,
    PostListView,
    UserLogoutView,
    UserLoginView,
    PostAddComment
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/add-comment/",
        PostAddComment.as_view(),
        name="add-comment"
    ),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]

app_name = "blog"
