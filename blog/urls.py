from django.urls import path

from blog.views import PostListView, PostListDetail

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostListDetail.as_view(), name="post-detail"),
]
