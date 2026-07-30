from django.urls import path

from blog.views import PostListView, PostDetailView, CommentCreateView

urlpatterns = [
    path("index/", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/comment/",
        CommentCreateView.as_view(),
        name="create-comment"
    ),

]

app_name = "blog"
