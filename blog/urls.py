from django.urls import path

from blog.views import index, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("comment_create/<int:pk>/", CommentaryCreateView.as_view(), name="comment-create"),
]

app_name = "blog"