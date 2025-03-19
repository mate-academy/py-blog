from django.urls import path, include

from .views import PostListView, PostDetailView, SignUpView, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/post-comment", CommentaryCreateView.as_view(), name="commentary-create"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/sign-up/", SignUpView.as_view(), name="sign-up"),
]

app_name = "blog"