from django.urls import path

from .views import (
    IndexView,
    PostDetailView, CommentCreateView,
)


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:post_id>/add-comment/", CommentCreateView.as_view(), name="add-comment"),
]

app_name = "blog"
