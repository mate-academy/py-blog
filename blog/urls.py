from django.urls import path

from blog.views import IndexView, PostDetailView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView, name="post-detail"),
]

app_name = "blog"
