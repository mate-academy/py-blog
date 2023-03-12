from django.urls import path, include
from blog.views import (
    PostListView,
    PostDetailView,
    CommentaryCreateView,
    PostCreateView
)


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("accounts/", include('django.contrib.auth.urls')),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/commentary/", CommentaryCreateView.as_view(), name="commentary-create"),
]

app_name = "blog"
