from django.urls import path
from blog.views import (
    PostListView,
    PostDetailView,
    CommentaryCreateView,
    CommentaryUpdateView,
    CommentaryUpdateView
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("commentarys/create/", CommentaryCreateView.as_view(), name="commentary-create"),
    path("commentarys/<int:pk>/update/", CommentaryUpdateView.as_view(), name="commentary-update"),
    path("commentarys/<int:pk>/delete/", CommentaryUpdateView.as_view(), name="commentary-delete"),
]

app_name = "blog"
