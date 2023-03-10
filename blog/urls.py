from django.contrib import admin
from django.urls import path, include

from blog.views import PostListView, PostDetailView, PostCreateView, CommentaryCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("posts/", PostListView.as_view(), name="index"),
    path("detail/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path(
        "posts/<int:pk>/comment/",
        CommentaryCreateView.as_view(),
        name="write-commentary")

]

app_name = "blog"
