from django.urls import path

from blog.views import PostsListView, post_detail_view

urlpatterns = [
    path("", PostsListView.as_view(), name="index"),
    path("posts/<int:pk>/", post_detail_view, name="post-detail"),
]

app_name = "blog"
