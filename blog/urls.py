from django.urls import path

from blog.views import PostListView, PostDetailView

index = PostListView.as_view()

urlpatterns = [
    path("index/", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
