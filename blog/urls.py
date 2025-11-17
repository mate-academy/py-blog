from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView,
    create_commentary_view
)


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create-commentary",
        create_commentary_view,
        name="post-create-commentary"
    ),
]

app_name = "blog"
