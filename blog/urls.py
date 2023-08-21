from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    CommentaryDeleteView,
    AddCommentView
)

urlpatterns = [
    path(
        "",
        PostListView.as_view(),
        name="post-list"
    ),
    path(
        "post/<int:pk>/detail/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "posts/<int:pk>/add_comment/",
        AddCommentView.as_view(),
        name="post-add-comment"
    ),
    path(
        "commentary/<int:pk>/delete/",
        CommentaryDeleteView.as_view(),
        name="commentary-delete"
    )
]

app_name = "blog"
