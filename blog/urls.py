from django.urls import path

from blog.views import PostListView, PostDetailView, commentary_create

app_name = "blog"


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/create-comment",
        commentary_create,
        name="comment-create"
    ),
]
