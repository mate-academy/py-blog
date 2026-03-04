from django.urls import path
from blog.views import PostCreateView, PostDetailView, IndexListView

app_name = "blog"

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
]
