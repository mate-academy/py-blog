from django.urls import path

from blog.views import PostListView, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/create-comment", CommentaryCreateView.as_view(), name="comment-create"),

]

app_name = "blog"