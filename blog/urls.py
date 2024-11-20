from django.urls import path
from blog.views import (
    IndexListView,
    PostDetailView,
)


urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create-comment",
        PostDetailView.create_comment_view,
        name="post-create-comment",
    ),
]

app_name = "blog"
