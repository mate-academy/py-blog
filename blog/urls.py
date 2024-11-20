from blog.views import PostDetailView, IndexListView, CommentaryCreateView
from django.urls import path

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/comment/create",
         CommentaryCreateView.as_view(),
         name="comment-create")
]

app_name = "blog"
