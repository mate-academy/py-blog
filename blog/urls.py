from django.urls import path

from .views import index, PostDetailView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("blog/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
