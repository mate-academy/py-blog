from django.urls import path

from blog.views import IndexView, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create-comment/",
        CommentaryCreateView.as_view(),
        name="create-comment",
    ),
]

app_name = "blog"
