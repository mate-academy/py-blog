from django.urls import path

from .views import PostListView, PostDetailView, CommentCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "<int:pk>/comment/",
        CommentCreateView.as_view(),
        name="comment-create"),
]

app_name = "blog"
