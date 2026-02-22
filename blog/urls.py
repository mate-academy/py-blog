from django.urls import path

from blog.views import PostsView, PostDetailView

app_name = "blog"

urlpatterns = [
    path("", PostsView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
