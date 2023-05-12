from django.urls import path

from blog.views import index, PostDetailView, PostListView, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail",),
    path(
        "posts/<int:pk>/comment/",
        CommentaryCreateView.as_view(),
        name="post-create-comment",
    ),
]

app_name = 'blog'
