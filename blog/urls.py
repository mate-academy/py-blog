from django.urls import path

from blog.views import (
    PostDetailView,
    comment_create,
    IndexListView,
)

urlpatterns = [
    path("", IndexListView.as_view(), name="redirect"),
    path("posts/", IndexListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create-comment", comment_create, name="comment-create"),
]

app_name = "blog"
