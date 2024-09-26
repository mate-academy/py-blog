from django.urls import path

from blog.views import (
    IndexListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
)
#
urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path(
        "posts/delete/<int:pk>/",
        PostDeleteView.as_view(),
        name="post-delete"
    ),
]

app_name = "blog"
