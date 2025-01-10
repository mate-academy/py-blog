from blog.views import PostListView, PostDetailView, CommentaryCreateView
from django.urls import path

app_name = "blog"
urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/commentary-create/",
        CommentaryCreateView.as_view(),
        name="commentary-create",
    ),
]
