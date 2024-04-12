from django.urls import path, include

from .views import (AuthorCreateView,
                    PostDetailView,
                    CreateCommentView,
                    PostListView,
                    IndexListView
                    )

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("post/", PostListView.as_view(), name="post-list"),
    path("create/", AuthorCreateView.as_view(), name="create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create_comment/",
        CreateCommentView.as_view(),
        name="create_comment",
    ),
]

app_name = "blog"
