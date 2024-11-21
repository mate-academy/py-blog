from django.urls import path

from blog.views import PostCreateView, PostDetailView, comment_create, index

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/comment/", comment_create, name="comment-create"),
]

app_name = "blog"
