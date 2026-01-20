from django.urls import path
from .views import index, PostListView, PostDetailView


urlpatterns = [
    path("blog/", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/", PostListView.as_view(), name="post-list"),
]

app_name = "blog"
