from django.urls import path
from .views import PostDetailView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
