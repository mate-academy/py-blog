from .views import PostDetailView, IndexView, CommentaryCreateView
from django.urls import path

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/comment/",
         CommentaryCreateView.as_view(),
         name="comment-create")
    ]

app_name = "blog"
