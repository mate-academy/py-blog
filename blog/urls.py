from django.urls import path

from blog.views import (PostListView,
                        PostDetailView,
                        UserDetailView,
                        PostCreateView)


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail")
]

app_name = "blog"
