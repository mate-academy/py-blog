from django.urls import path

from .views import PostListView, PostDetailView, commentary_create_view


app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create-comment/",
        commentary_create_view,
        name="post-create-comment",
    ),
]
