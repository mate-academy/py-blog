from django.urls import path

from .views import PostListView, PostCommentView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostCommentView.as_view(), name="post-detail"),
]

app_name = "blog"
