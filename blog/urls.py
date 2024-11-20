from django.urls import path

from blog.views import (
    IndexListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserDetailView,
)

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path(
        "posts/update/<int:pk>/", PostUpdateView.as_view(), name="post-update"
    ),
    path(
        "posts/delete/<int:pk>/", PostDeleteView.as_view(), name="post-delete"
    ),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]

app_name = "blog"
