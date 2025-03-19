from django.urls import path
from blog.views import (
    PostListView, post_detail_view,
)

app_name = "blog"
urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", post_detail_view, name="post-detail")
]
