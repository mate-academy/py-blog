from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(),
         name="post-update"),
]

app_name = "blog"
