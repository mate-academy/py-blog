from django.urls import path
from blog.views import (
    index,
    PostDetailView,
    create_comment,
)

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create_comment/",
        create_comment,
        name="create-comment"
    )
]
