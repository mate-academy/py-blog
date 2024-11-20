from blog.views import PostList, post_detail_and_create
from django.urls import path

urlpatterns = [
    path("", PostList.as_view(), name="index"),
    path("posts/<int:pk>/", post_detail_and_create, name="post-detail")
]

app_name = "blog"
