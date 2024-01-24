from django.urls import path

from .views import (
    IndexView,
    PostDetailView,
    CommentaryCreateView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/comment/add/",
        CommentaryCreateView.as_view(),
        name="add-comment"
    )
]

app_name = "blog"
