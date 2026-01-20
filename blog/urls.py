from django.urls import path

from blog.views import IndexListView, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "comment/",
        CommentaryCreateView.as_view(),
        name="comment-create"
    ),
]

app_name = "blog"
