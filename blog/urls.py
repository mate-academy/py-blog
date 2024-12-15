from django.urls import path

from blog.views import index, PostDetailView, CommentCreateView

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/comment/", CommentCreateView.as_view(),
         name="comment-create"),
]
