from django.urls import path, include

from .views import PostListView, post_detail_plus_create_comment

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>",
         post_detail_plus_create_comment,
         name="post-detail"),
]

app_name = "blog"
