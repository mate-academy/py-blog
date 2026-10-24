from django.urls import path

from . import views
from .views import PostDetailView, CommentaryCreateView

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/comments/",
        CommentaryCreateView.as_view(),
        name="comment-create"
    )
]
