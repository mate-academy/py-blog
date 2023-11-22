from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    UserLoginView,
    UserLogoutView
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]

app_name = "blog"
