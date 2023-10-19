from django.urls import path

from blog.views import (
    index,
    PostDetailView,
    comment_create,
    redirecttomain,
)

urlpatterns = [
    path("", redirecttomain, name="redirect"),
    path("posts/", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create-comment", comment_create, name="comment-create"),
]

app_name = "blog"