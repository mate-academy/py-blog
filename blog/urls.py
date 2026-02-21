from django.urls import path

from blog.views import PostsView, PostsDetailView, PostsCreateComment

app_name = "blog"

urlpatterns = [
    path("", PostsView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostsDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/comments", PostsCreateComment.as_view(), name="create-comment"),
    path("index/", PostsView.as_view(), name="index"),
]
