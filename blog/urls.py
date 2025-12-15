from django.urls import path
from blog.views import (
    Index,
    PostDetailView,
    CommentCreateView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserDetailView,
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("comment_create/",
         CommentCreateView.as_view(),
         name="comment-create"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/",
         PostUpdateView.as_view(),
         name="post-update"),
    path("post/<int:pk>/delete/",
         PostDeleteView.as_view(),
         name="post-delete"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]

app_name = "blog"
