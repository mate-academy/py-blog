from django.urls import path, include
from django.views.generic import detail

from blog.views import PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
