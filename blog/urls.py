from django.urls import path, include

from blog.views import IndexView, PostList, PostDetail

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/", PostList.as_view(), name="posts-list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="post-detail"),
]

app_name = "blog"
