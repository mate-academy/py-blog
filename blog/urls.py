from django.urls import path

from blog.views import PostsView, PostsDetailView

app_name = "blog"

urlpatterns = [
    path("", PostsView.as_view(), name="index"),
    path("posts/<int:pk>/", PostsDetailView.as_view(), name="post-detail"),
]
