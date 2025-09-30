from django.urls import path

from .views import (
    index,
    PostDetailView,
)

urlpatterns = [
    path("blog/", index, name="index"),
    path("blog/posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
