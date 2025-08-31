from django.urls import path
from blog.views import PostListView, PostDetailView, CommentCreateView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "comments-create/<int:pk>/",
        CommentCreateView.as_view(),
        name="commentary-create"
    ),
]
