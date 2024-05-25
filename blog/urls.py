from django.urls import path
from blog.views import (
    IndexListView,
    PostListView,
    PostDetailView,
    CommentaryCreateView,
)


urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/create/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
]

app_name = "blog"
