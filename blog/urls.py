from django.urls import path
from django.views.generic import DetailView

from blog.views import (
    PostListView,
    PostDetailView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/pk/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    # path(
    #     "posts/pk/<int:pk>/create_comment",
    #     post_commentary_create_view,
    #     name="comment-create",
    # ),
]

app_name = "blog"
