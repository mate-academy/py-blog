from django.urls import path
from .views import (
    index,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserListView,
    UserDetailView,
    CommentaryListView,
    CommentaryUpdateView,
    CommentaryDeleteView,
    CommentaryCreateView,

)


app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("users/", UserListView.as_view(), name="user-list"),
    path(
        "users/<int:pk>/", UserDetailView.as_view(), name="user-detail"
    ),
    path(
        "comments/",
        CommentaryListView.as_view(),
        name="commentary-list"
    ),
    path("comments/create/", CommentaryCreateView.as_view(),
         name="commentary-create"),
    path("comments/<int:pk>/update/", CommentaryUpdateView.as_view(),
         name="commentary-update"),
    path("comments/<int:pk>/delete/", CommentaryDeleteView.as_view(),
         name="commentary-delete"),
]