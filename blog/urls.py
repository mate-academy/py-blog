from django.urls import path, include
from blog.views import PostListView, PostDetailView

post_urls = [
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/", include(post_urls)),
]

app_name = "blog"
