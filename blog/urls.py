from blog.views import PostListView, PostDetailView, PostCreateView
from django.urls import path

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),

]

app_name = "blog"
