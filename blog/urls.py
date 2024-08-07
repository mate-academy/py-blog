from django.urls import path

from blog.views import PostListView, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "commentary/<int:post_id>/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
]

app_name = "blog"
