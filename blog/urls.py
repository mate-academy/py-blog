from django.urls import path

from blog.views import PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail")
]

app_name = "blog"
