from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    create_comment,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "commentary/<int:pk>/create/",
        create_comment,
        name="commentary-create"
    ),
]

app_name = "blog"
