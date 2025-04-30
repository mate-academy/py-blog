from django.urls import path
from .views import index, PostDetailView, CommentCreateView

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/comment/",
        CommentCreateView.as_view(),
        name="comment-create"
    ),
]

app_name = "blog"
