from django.urls import path
from .views import index, PostListView, PostDetailView, comment_form


urlpatterns = [
    path("blog/", index, name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/comment/", comment_form, name="comment-create"),
]

app_name = "blog"
