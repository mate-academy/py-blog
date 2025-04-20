from django.urls import path

from blog.views import PostListView, PostDetailView, CommentaryCreateView

app_name = "blog"
urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/commentary-create/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
]
