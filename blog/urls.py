from django.urls import path
from blog.views import (PostListView,
                        PostDetailView,
                        CommentUpdateView,
                        CommentDeleteView,
                        )

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("comments/<int:pk>/update/",
         CommentUpdateView.as_view(),
         name="comment-update"),
    path("comments/<int:pk>/delete/",
         CommentDeleteView.as_view(),
         name="comment-delete"),
]
app_name = "blog"
