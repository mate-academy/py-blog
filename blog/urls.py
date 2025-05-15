from django.urls import path
from . import views
from .views import PostListView, post_detail

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", post_detail, name="post-detail"),
]
