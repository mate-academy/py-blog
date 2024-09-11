from django.urls import path

from blog.views import (
    BlogListView,
    PostDetailView,
)


urlpatterns = [
    path("", BlogListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
