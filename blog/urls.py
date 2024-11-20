from django.urls import path
from .views import IndexView, PostDetailView, CommentCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/comments",
         PostDetailView.as_view(),
         name="post-detail"),
    path("posts/<int:pk>/comments/create",
         CommentCreateView.as_view(),
         name="comment-create")
]

app_name = "blog"
