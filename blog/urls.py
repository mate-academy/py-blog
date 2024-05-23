from django.urls import path

from .views import index, PostListView, PostDetailView

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
