from django.urls import path

from .views import PostDetailView, CommentaryCreateView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create_comment/",
        CommentaryCreateView.as_view(),
        name="commentary-create",
    ),
]

app_name = "blog"
