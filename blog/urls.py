from django.urls import path

from blog.views import (
    PostListViews,
    PostDetailView
)
urlpatterns = [
    path("", PostListViews.as_view(), name="index"),
    path("post/", PostListViews.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
