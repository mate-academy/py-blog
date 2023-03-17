from django.urls import path

from blog.views import PostListView, PostListDetail, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostListDetail.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/comment/",
        CommentaryCreateView.as_view(),
        name="post-create-comment"
    ),
]

app_name = "blog"
