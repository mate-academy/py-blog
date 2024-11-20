from django.urls import path

from blog.views import PostListView, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/add_commentary/",
        CommentaryCreateView.as_view(),
        name="add-commentary"
    )
]

app_name = "blog"
