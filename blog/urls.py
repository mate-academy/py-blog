from .views import PostListView, PostDetailView
from django.urls import path


urlpatterns = [
    path("posts/", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]


app_name = "blog"
