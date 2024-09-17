from django.urls import path

from .views import (
    CommentaryCreateView,
    PostListView,
    PostCreateView,
    PostDetailView,
    UserCreateView
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/comment/",
        CommentaryCreateView.as_view(),
        name="commentary-create"),
    path("user/create/", UserCreateView.as_view(), name="user-create")
]

app_name = "blog"
