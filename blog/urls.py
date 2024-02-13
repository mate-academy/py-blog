from django.urls import path

from blog.views import IndexView, PostDetailView, add_comment

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:post_id>/add-comment/", add_comment, name="add-comment")
]

app_name = "blog"
