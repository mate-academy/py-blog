from django.urls import path
from django.views.generic import detail

from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
]

app_name = "blog"
