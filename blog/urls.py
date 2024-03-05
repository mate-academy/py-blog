from django.urls import path

from .views import (IndexListView,
                    PostDetailView,
                    comment_create_view,
                    post_create_view
                    )

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("post/create/", post_create_view, name="create-post"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create-comment/",
        comment_create_view,
        name="comment-create"
    ),
]


app_name = "blog"
