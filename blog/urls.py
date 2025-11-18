from django.urls import path

from blog.views import IndexView, PostDetailView, CommentaryCreate


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/comment/",
        CommentaryCreate.as_view(),
        name="comment_create"),
]

app_name = "blog"
