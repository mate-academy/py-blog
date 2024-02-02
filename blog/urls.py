from django.urls import path, include

from blog.views import (
    IndexView,
    UserListView,
    UserDetailView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentaryCreateView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("users/",
         UserListView.as_view(),
         name="user-list"),
    path("users/<int:pk>/",
         UserDetailView.as_view(),
         name="user-detail"),
    path("post/<int:pk>/",
         PostDetailView.as_view(),
         name="post-detail"),
    path("post/create/",
         PostCreateView.as_view(),
         name="post-create"),
    path("post/<int:pk>/update/",
         PostUpdateView.as_view(),
         name="post-update"),
    path("post/<int:pk>/delete/",
         PostDeleteView.as_view(),
         name="post-delete"),
    path("post/<int:pk>/commentary-create/",
         CommentaryCreateView.as_view(),
         name="comment-create",),
]

app_name = "blog"
