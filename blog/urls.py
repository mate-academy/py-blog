from django.urls import path, include
from blog.views import PostList, PostDetail

app_name = "blog"


urlpatterns = [
    path("", PostList.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="post-detail"),
]