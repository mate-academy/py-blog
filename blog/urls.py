from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    CommentaryCreateView,
    CommentaryDeleteView,
    CommentaryUpdateView,
    PostCreateView,
    DashboardListView,
    PostDeleteView,
    PostUpdateView,
    UserDetailView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post_create/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts_delete/<int:pk>/",
        PostDeleteView.as_view(),
        name="post-delete"
    ),
    path(
        "post_update/<int:pk>/",
        PostUpdateView.as_view(),
        name="post-update"
    ),
    path(
        "comment_create/<int:post_id>/",
        CommentaryCreateView.as_view(),
        name="comment-create",
    ),
    path(
        "comment_update/<int:pk>/",
        CommentaryUpdateView.as_view(),
        name="comment-update",
    ),
    path(
        "comment_delete/<int:pk>/",
        CommentaryDeleteView.as_view(),
        name="comment-delete",
    ),
    path("dashboard/", DashboardListView.as_view(), name="dashboard"),
    path(
        "user_detail/<int:pk>/",
        UserDetailView.as_view(),
        name="user-detail"
    ),
]

app_name = "blog"
