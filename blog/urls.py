from django.urls import path

from blog.views import PostListView, post_detail_view

urlpatterns = [
    path("index/", PostListView.as_view(), name="index"),
    path("post/<int:pk>", post_detail_view, name="post-detail"),
]

app_name = "blog"
