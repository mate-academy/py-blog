from django.urls import path, re_path

from blog.views import (
    index,
    PostDetailView,
    PostCreateView,
    CommentaryCreateView,
)

urlpatterns = [
    path("post/", index, name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path(
        "post/<int:pk>/create/",
        CommentaryCreateView.as_view(),
        name="commentary-create",
    ),
]

app_name = "blog"
