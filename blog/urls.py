from django.urls import path
from blog.views import PostListView, post_detail


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", post_detail, name="post-detail"),
]

app_name = "blog"
