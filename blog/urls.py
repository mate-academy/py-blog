from django.urls import path
from blog.views import Posts, PostDetailView


app_name = "blog"

urlpatterns = [
    path("index/", Posts.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
