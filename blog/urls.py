from django.urls import path

from blog.views import PostDetailView, PostListView, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "comments/create/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
]

app_name = "blog"
