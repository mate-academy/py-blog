from django.urls import path
from .views import (
    BlogListView,
    PostDetailView,
    CommentCreateView,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/comment/",
         CommentCreateView.as_view(),
         name="add-comment")
]

app_name = "blog"
