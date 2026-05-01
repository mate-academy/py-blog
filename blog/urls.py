from django.urls import path

from .views import PostListView, PostDetailView, add_comment

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("<int:pk>/comment/", add_comment, name="comment-create"),
]

app_name = "blog"
