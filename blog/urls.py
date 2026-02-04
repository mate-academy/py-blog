from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create", PostCreateView.as_view(), name="post-create"),
]

app_name = "blog"
