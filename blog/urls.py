from django.urls import path

from blog.views import (
    index,
    PostListView,
    PostDetailView,
    PostDeleteView,
    CommentaryDeleteView,
)

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/delete/",
         PostDeleteView.as_view(),
         name="post-delete"),
    path(
        "/commentaries/<int:pk>/delete/",
        CommentaryDeleteView.as_view(),
        name="commentary-delete",
    ),
]
