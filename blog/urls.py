from django.urls import path

from blog.views import PostListView, CommentaryListView, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", CommentaryListView.as_view(), name="post-detail"),
    path(
        "posts/commentary-create/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
]

app_name = "blog"
