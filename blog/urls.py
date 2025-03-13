from django.urls import path

from blog.views import PostDetailView, Index

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
