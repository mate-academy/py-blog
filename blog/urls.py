from django.urls import path

from blog.views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path("blog/create/", PostCreateView.as_view(), name="post-create"),
    path("blog/", PostListView.as_view(), name="index"),
    path("blog/<int:pk>", PostDetailView.as_view(), name="post-detail"),

]

app_name = "blog"