from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    AddCommentView,
    UserLoginView,
    UserLogoutView
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/add_comment/",
        AddCommentView.as_view(),
        name="add-comment"
    ),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]


app_name = "blog"
