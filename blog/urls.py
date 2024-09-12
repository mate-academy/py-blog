from django.urls import path

from blog.views import PostListView, PostDetailViewWithComment

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path(
        "posts/<int:pk>/",
        PostDetailViewWithComment.as_view(),
        name="post-detail"
    ),
]

app_name = "blog"
