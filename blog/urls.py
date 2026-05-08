from django.urls import path

from .views import (
    index,
    PostDetailView,
    CommentaryCreateView,
    CommentaryUpdateView,
    CommentaryDeleteView,
)

app_name = "blog"
urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/comments/create/",
         CommentaryCreateView.as_view(),
         name="comment-create"
         ),
    path("comments/<int:pk>/update/",
         CommentaryUpdateView.as_view(),
         name="comment-update"
         ),
    path("comments/<int:pk>/delete/",
         CommentaryDeleteView.as_view(),
         name="comment-delete"
         ),
]
