from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    AddCommentView,
    CommentaryDeleteView
)

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("blog/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "blog/<int:pk>/add-comment/",
        AddCommentView.as_view(),
        name="add-comment"
    ),
    path(
        "commentary/<int:pk>/delete/",
        CommentaryDeleteView.as_view(),
        name="commentary-delete",
    ),
]
