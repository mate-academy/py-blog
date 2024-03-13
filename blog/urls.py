from django.urls import path

from blog.views import index, PostListView, PostDetailView

urlpatterns = [
    path("", index, name="index"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
