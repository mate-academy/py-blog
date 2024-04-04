from django.urls import path


from .views import CommentaryCreateView, PostDetailView, PostListView


urlpatterns = [
    path("posts/", PostListView.as_view(), name="index"),
    path(
        "posts/<int:pk>/comment/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "comment/create/",
        CommentaryCreateView.as_view(),
        name="comment-create"
    ),
]


app_name = "blog"
