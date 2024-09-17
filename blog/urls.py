from django.urls import path
from blog.views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/", PostCreateView.as_view(), name="post-create"),
]

app_name = "blog"
