from django.contrib import admin
from django.urls import path

from blog.views import PostList, post_detail

urlpatterns = [
    path("", PostList.as_view(), name="index"),
    path("posts/<int:pk>/", post_detail, name="post-detail"),
    path("posts/<int:pk>/comment/create/", post_detail, name="comment-create"),
]

app_name = "blog"
