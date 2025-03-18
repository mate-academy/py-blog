from django.urls import path, include

from .views import PostListView, PostDetailView, SignUpView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/sign-up/", SignUpView.as_view(), name="sign-up"),
]

app_name = "blog"